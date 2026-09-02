% SP3 impact pipeline: SPM's "Advanced topics in M/EEG artefact removal" chapter
% (mark mode + robust averaging with Remove-bad-data) on the MMN tutorial data.
% Usage: TAG = 'prefix' | 'postfix' set by caller; badsamples.m swapped by caller.
S0 = '/tmp/claude-0/-home-user-afni/d65df75e-7d82-531d-babc-bc1cc192b046/scratchpad/mmn';
if ~exist('TAG','var'), TAG = 'run'; end
D = spm_eeg_load(fullfile(S0,'spmeeg_subject1.mat'));
if ~exist(fullfile(S0,'bedfdspmeeg_subject1.mat'),'file')
  % shared preprocessing (independent of the fix): downsample, filter, epoch, baseline
  S=[]; S.D=D; S.fsample_new=200; S.method='resample';       D=spm_eeg_downsample(S);   % 512->200 exact
  S=[]; S.D=D; S.band='high'; S.freq=0.5;  D=spm_eeg_filter(S);
  S=[]; S.D=D; S.band='low';  S.freq=30;   D=spm_eeg_filter(S);
  ev = events(D,1); vals = unique([ev(strcmp({ev.type},'STATUS')).value]);
  fprintf('event values present: %s\n', mat2str(vals));
  S=[]; S.D=D; S.timewin=[-100 400]; S.bc=1;
  S.trialdef(1).conditionlabel='standard'; S.trialdef(1).eventtype='STATUS'; S.trialdef(1).eventvalue=65152;
  S.trialdef(2).conditionlabel='deviant';  S.trialdef(2).eventtype='STATUS'; S.trialdef(2).eventvalue=65216;
  D=spm_eeg_epochs(S);
  fprintf('epoched: %d trials, %d samples/trial, timeOnset=%g, fs=%g\n', ntrials(D), nsamples(D), timeonset(D), fsample(D));
  save(D); D = spm_eeg_load(fullfile(D.path, D.fname));
  copyfile(fullfile(D.path,D.fname), fullfile(S0,'bedfdspmeeg_subject1.mat')); copyfile(fullfile(D.path,[spm_file(D.fname,'basename') '.dat']), fullfile(S0,'bedfdspmeeg_subject1.dat'));
end
D = spm_eeg_load(fullfile(S0,'bedfdspmeeg_subject1.mat'));
% --- artefact MARK mode, as in the chapter: z-scored difference threshold, 100 ms excision, badchanthresh 1
S=[]; S.D=D; S.mode='mark'; S.badchanthresh=1; S.append=false; S.prefix=['a' TAG '_'];
S.methods(1).channels={'EEG'}; S.methods(1).fun='zscorediff'; S.methods(1).settings.threshold=5; S.methods(1).settings.excwin=100;
Da = spm_eeg_artefact(S);
% --- the quantity the fix changes: which samples badsamples() marks
bad = badsamples(Da, ':', ':', ':');                   % chan x samp x trial
nbad_per_trial = squeeze(sum(sum(bad,1),2));
fprintf('[%s] artefact events written: %d; bad samples total=%d; trials with any bad=%d; channels flagged bad=%d\n', ...
   TAG, sum(cellfun(@(e) numel(e), {events(Da)})), nnz(bad), nnz(nbad_per_trial), numel(badchannels(Da)));
% first artefact event: where the detector says it is vs where badsamples marks it
for i=1:ntrials(Da)
  ev = events(Da,i); if iscell(ev), ev=ev{1}; end
  ev = ev(strncmp({ev.type},'artefact',8));
  if ~isempty(ev)
     e = ev(1); n_written = round((e.time - trialonset(Da,i))*fsample(Da));   % detector convention: trialonset + idx/fs
     marked = find(any(bad(:,:,i),1));
     fprintf('[%s] trial %d: detector wrote sample idx %d (dur %.0f ms); badsamples marks %d..%d (shift %+d samples; timeOnset*fs = %g)\n', ...
        TAG, i, n_written, 1000*e.duration, marked(1), marked(end), marked(1)-n_written, timeonset(Da)*fsample(Da));
     break
  end
end
% --- robust average with Remove bad data = yes, then MMN
S=[]; S.D=Da; S.robust.ks=3; S.robust.bycondition=false; S.robust.savew=false; S.robust.removebad=true; S.prefix=['m' TAG '_'];
Dm = spm_eeg_average(S);
X = Dm(:,:,:); cl = conditions(Dm);
mmn = squeeze(X(:,:,strcmp(cl,'deviant')) - X(:,:,strcmp(cl,'standard')));
eeg = indchantype(Dm,'EEG','GOOD'); mmn = mmn(eeg,:);
t = time(Dm)*1000; gfp = std(mmn,0,1); win = t>=100 & t<=300;
[~,k] = max(gfp.*win); [~,ch] = max(abs(mmn(:,k)));
fprintf('[%s] MMN GFP peak %.1f ms; max chan %s %+.2f uV; GFP@peak %.3f\n', TAG, t(k), char(chanlabels(Dm,eeg(ch))), mmn(ch,k), gfp(k));
save(fullfile(S0,['sp3_' TAG '.mat']), 'mmn','t','gfp','bad','nbad_per_trial','-v7');
