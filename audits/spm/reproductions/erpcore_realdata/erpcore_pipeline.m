% erpcore_pipeline.m -- SP3 (@meeg/badsamples) impact on ERP CORE, real SPM code in Octave.
% Caller sets: SUB (numeric), TASK ('P3'|'ERN'), BUILD ('prefix'|'merged'), ROOT (erpcore dir).
% Stage A (build-independent, done once per subject/task): convert -> shift stimulus codes by
%   26 ms (ERP CORE Script1) -> montage (P9/P10 reference, bipolar VEOG/HEOG) -> resample to
%   256 Hz (exact, 'resample') -> 0.1 Hz high-pass -> 30 Hz low-pass -> epoch -> baseline.
% Stage B (per build): artefact 'mark' mode (threshchan 100 uV, 200 ms excision) -> bad-sample
%   mask -> bad channels -> 'events' rejection -> plain average; robust average with removebad.
raw  = fullfile(ROOT, ['raw_' TASK], sprintf('%d_%s.set', SUB, TASK));
work = fullfile(ROOT, 'work', TASK, sprintf('%02d', SUB)); if ~exist(work,'dir'), mkdir(work); end
resd = fullfile(ROOT, 'results', TASK); if ~exist(resd,'dir'), mkdir(resd); end
Afile = fullfile(work, 'A.mat');
fs_new = 256;
%% ---------------- Stage A ----------------
if ~exist(Afile, 'file')
    S=[]; S.dataset=raw; S.mode='continuous'; S.outfile=fullfile(work,'c'); S.checkboundary=0;
    D = spm_eeg_convert(S);
    % channel types: all scalp channels EEG, the three raw EOG channels EOG
    lab = chanlabels(D);
    D = chantype(D, find(~ismember(lab, {'HEOG_left','HEOG_right','VEOG_lower'})), 'EEG');
    D = chantype(D, find( ismember(lab, {'HEOG_left','HEOG_right','VEOG_lower'})), 'EOG');
    % shift stimulus event codes by 26 ms (LCD delay), as ERP CORE Script1 does
    if strcmp(TASK,'P3'), stimcodes = [11:15 21:25 31:35 41:45 51:55]; else stimcodes = [11 12 21 22]; end
    ev = events(D, 1);
    for i = 1:numel(ev)
        if isnumeric(ev(i).value) && ismember(ev(i).value, stimcodes), ev(i).time = ev(i).time + 0.026; end
    end
    D = events(D, 1, ev); save(D);
    % montage: EEG re-referenced to (P9+P10)/2 (P9/P10 dropped), bipolar VEOG = VEOG_lower - FP2, HEOG = HEOG_left - HEOG_right
    eeg = setdiff(lab(strcmp(chantype(D),'EEG')), {'P9','P10'}, 'stable');
    n = numel(lab); M = numel(eeg) + 2; tra = zeros(M, n);
    ip9 = find(strcmp(lab,'P9')); ip10 = find(strcmp(lab,'P10'));
    for k = 1:numel(eeg), tra(k, strcmp(lab, eeg{k})) = 1; tra(k, ip9) = -0.5; tra(k, ip10) = -0.5; end
    tra(M-1, strcmp(lab,'VEOG_lower')) = 1; tra(M-1, strcmp(lab,'FP2')) = -1;
    tra(M,   strcmp(lab,'HEOG_left')) = 1; tra(M,   strcmp(lab,'HEOG_right')) = -1;
    S=[]; S.D=D; S.montage.tra=tra; S.montage.labelorg=lab(:); S.montage.labelnew=[eeg(:); {'VEOG'; 'HEOG'}];
    S.keepothers=0; S.prefix='M';
    D = spm_eeg_montage(S);
    D = chantype(D, indchannel(D, eeg), 'EEG'); D = chantype(D, indchannel(D, {'VEOG','HEOG'}), 'EOG'); save(D);
    S=[]; S.D=D; S.fsample_new=fs_new; S.method='resample'; D = spm_eeg_downsample(S);
    S=[]; S.D=D; S.band='high'; S.freq=0.1; D = spm_eeg_filter(S);
    S=[]; S.D=D; S.band='low';  S.freq=30;  D = spm_eeg_filter(S);
    % trial definition, ERP CORE bins
    ev = events(D, 1); fs = fsample(D);
    isnum = arrayfun(@(e) isnumeric(e.value) && ~isempty(e.value), ev);
    ev = ev(isnum); vals = [ev.value]; times = [ev.time];
    trl = []; lab_c = {};
    if strcmp(TASK,'P3')
        pretrig = -200; posttrig = 800;
        for i = find(vals >= 11 & vals <= 55)
            f = find(vals == 201 & times > times(i)+0.2 & times < times(i)+1.0, 1);
            if isempty(f), continue; end
            t0 = times(i); tens = floor(vals(i)/10); ones_ = mod(vals(i),10);
            if tens == ones_, cl = 'target'; else cl = 'standard'; end
            trl(end+1,:) = [indsample(D,t0)+round(pretrig/1000*fs), 0, round(pretrig/1000*fs)]; lab_c{end+1} = cl;
        end
    else
        pretrig = -600; posttrig = 400;
        for i = find(ismember(vals, [111 112 121 122 211 212 221 222]))
            f = find(ismember(vals, [11 12 21 22]) & times < times(i)-0.2 & times > times(i)-1.0, 1, 'last');
            if isempty(f), continue; end
            t0 = times(i);
            if ismember(vals(i), [211 112 221 122]), cl = 'error'; else cl = 'correct'; end
            trl(end+1,:) = [indsample(D,t0)+round(pretrig/1000*fs), 0, round(pretrig/1000*fs)]; lab_c{end+1} = cl;
        end
    end
    trldur = round((posttrig-pretrig)/1000*fs); trl(:,2) = trl(:,1) + trldur - 1;
    ok = trl(:,1) >= 1 & trl(:,2) <= nsamples(D); trl = trl(ok,:); lab_c = lab_c(ok);
    S=[]; S.D=D; S.trl=trl; S.conditionlabels=lab_c; S.bc = strcmp(TASK,'P3'); D = spm_eeg_epochs(S);
    if strcmp(TASK,'ERN'), S=[]; S.D=D; S.timewin=[-400 -200]; D = spm_eeg_bc(S); end
    fprintf('[A] %s sub %d: %d trials (%s), %d samples at %g Hz, timeOnset %g\n', TASK, SUB, ntrials(D), ...
        strjoin(cellfun(@(c) sprintf('%s=%d', c, sum(strcmp(conditions(D),c))), unique(conditions(D)), 'UniformOutput', false), ', '), ...
        nsamples(D), fsample(D), timeonset(D));
    D = copy(D, fullfile(work, 'A'));
    % remove intermediates
    delete(fullfile(work, 'c.*')); delete(fullfile(work, 'Mc.*')); delete(fullfile(work, 'dMc.*')); delete(fullfile(work, 'fdMc.*')); delete(fullfile(work, 'ffdMc.*'));
    delete(fullfile(work, 'effdMc.*')); if strcmp(TASK,'ERN'), delete(fullfile(work, 'beffdMc.*')); end
end
%% ---------------- Stage B ----------------
D = spm_eeg_load(Afile);
S=[]; S.D=D; S.mode='mark'; S.badchanthresh=0.2; S.append=false; S.prefix=['a' BUILD '_'];
S.methods(1).channels={'EEG','EOG'}; S.methods(1).fun='threshchan'; S.methods(1).settings.threshold=100; S.methods(1).settings.excwin=200;
Da = spm_eeg_artefact(S);
bad = badsamples(Da, ':', ':', ':');
res = struct();
res.sub = SUB; res.task = TASK; res.build = BUILD;
res.bad = uint8(bad); res.chanlabels = chanlabels(Da); res.chantype = chantype(Da); res.time = time(Da);
res.conditions = conditions(Da); res.badchannels = badchannels(Da);
res.timeonset = timeonset(Da); res.fsample = fsample(Da);
% the detector's own event list (build-independent): where each artefact was found
evs = {};
for i = 1:ntrials(Da), e = events(Da, i); if iscell(e), e = e{1}; end
    e = e(strncmp({e.type}, 'artefact', 8));
    for k = 1:numel(e), evs(end+1,:) = {i, e(k).value, e(k).time - trialonset(Da,i), e(k).duration}; end
end
res.artefact_events = evs;   % {trial, channel label, onset rel. trial onset (s), duration (s)}
% events-based rejection in reject mode (any bad sample on any EEG/EOG channel -> trial bad)
S=[]; S.D=Da; S.mode='reject'; S.badchanthresh=0.2; S.prefix=['r' BUILD '_'];
S.methods(1).channels={'EEG','EOG'}; S.methods(1).fun='events'; S.methods(1).settings.whatevents.artefacts=1;
Dr = spm_eeg_artefact(S);
res.badtrials = badtrials(Dr); res.badchannels_reject = badchannels(Dr);
% plain average of the good trials
S=[]; S.D=Dr; S.robust=0; S.prefix=['m' BUILD '_']; Dm = spm_eeg_average(S);
res.erp_plain = Dm(:,:,:); res.erp_conditions = conditions(Dm); res.ntrials_plain = cellfun(@(c) sum(strcmp(conditions(Dr),c) & ~ismember(1:ntrials(Dr), res.badtrials)), conditions(Dm));
% robust average with removebad on the marked (not rejected) data
S=[]; S.D=Da; S.robust.ks=3; S.robust.bycondition=false; S.robust.savew=false; S.robust.removebad=true; S.prefix=['mr' BUILD '_']; Dmr = spm_eeg_average(S);
res.erp_robust = Dmr(:,:,:);
save(fullfile(resd, sprintf('sub%02d_%s.mat', SUB, BUILD)), '-struct', 'res', '-v7');
fprintf('[B] %s sub %d %s: bad samples %d, trials with bad %d, bad channels %d (%s), rejected trials %d\n', TASK, SUB, BUILD, ...
    nnz(bad), nnz(squeeze(any(any(bad,1),2))), numel(res.badchannels), strjoin(cellstr(char(chanlabels(Da, res.badchannels))), ','), numel(res.badtrials));
for f = {Da, Dr, Dm, Dmr}, delete(fullfile(f{1}.path, [spm_file(f{1}.fname,'basename') '.*'])); end
