% FT1b: cluster p-values use strict '>' against the randomization distribution.
% For clusterstatistic='maxsize' (integer-valued) ties are common and are all
% excluded, so p is anti-conservative. For 'maxsum' on continuous t-values ties
% do not occur and the strict/non-strict definitions agree (exoneration).
pkg load statistics
addpath(getenv('FIELDTRIP')); ft_defaults
addpath([pwd '/shims']);
warning('off','all');
rand('seed',7); randn('seed',7);
T = 60; nsubj = 12; nrand = 500; ndata = 200;
design = [ones(1,nsubj) 2*ones(1,nsubj); 1:nsubj 1:nsubj];
base = [];
base.statistic = 'ft_statfun_depsamplesT'; base.ivar = 1; base.uvar = 2;
base.correctm = 'cluster'; base.clusteralpha = 0.05; base.clustertail = 1; base.tail = 1;
base.numrandomization = nrand; base.feedback = 'no';
base.dim = [1 T]; base.dimord = 'chan_time'; base.channel = {'c1'}; base.neighbours = [];
base.spmversion = 'spm12';
for cs = {'maxsize', 'maxsum'}
  cfg = base; cfg.clusterstatistic = cs{1};
  nties = 0; nclus = 0; rej_ft = 0; rej_ge = 0; pdiff = [];
  for d = 1:ndata
    % null data with temporal autocorrelation so that clusters form
    x = randn(T+10, 2*nsubj); x = filter(ones(1,8)/8, 1, x); dat = x(11:end,:);
    evalc('stat = ft_statistics_montecarlo(cfg, dat, design);');
    if isfield(stat, 'posclusters') && ~isempty(stat.posclusters)
      for j = 1:numel(stat.posclusters)
        s = stat.posclusters(j).clusterstat; dist = stat.posdistribution;
        p_ft = stat.posclusters(j).prob;
        p_ge = (sum(dist >= s) + 1) / (nrand + 1);
        nclus = nclus + 1; nties = nties + sum(dist == s);
        pdiff(end+1) = p_ge - p_ft;
        if j == 1
          rej_ft = rej_ft + (p_ft <= 0.05); rej_ge = rej_ge + (p_ge <= 0.05);
        end
      end
    end
  end
  printf('\nclusterstatistic = %-7s | %d null datasets, %d randomizations each, %d observed clusters\n', cs{1}, ndata, nrand, nclus);
  printf('  randomizations tied with an observed cluster statistic: %d (mean %.1f per cluster)\n', nties, nties/max(nclus,1));
  printf('  mean (p_ge - p_ft) = %.4f, max = %.4f\n', mean(pdiff), max(pdiff));
  printf('  datasets with largest cluster p<=0.05: FieldTrip %d/%d (%.1f%%) vs tie-inclusive %d/%d (%.1f%%)\n', rej_ft, ndata, 100*rej_ft/ndata, rej_ge, ndata, 100*rej_ge/ndata);
end
