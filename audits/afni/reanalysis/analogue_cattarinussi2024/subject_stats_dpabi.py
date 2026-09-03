#!/usr/bin/env python3
"""Per-subject before/after statistics and demographics for the DPABI-analogous pipeline (unsmoothed ReHo, before z-normalisation)."""
import nibabel as nib, numpy as np, os, subprocess, csv
from scipy import stats
R='/home/user/reho-pilot/'; G=R+'dpabi/group/'; N=R+'dpabi/nifti/'; os.makedirs(N,exist_ok=True)
env=dict(os.environ,PATH='/home/user/afni-bin/linux_ubuntu_24_64:'+os.environ['PATH'],LD_LIBRARY_PATH='/home/user/afni-bin/linux_ubuntu_24_64')
part={r['participant_id']:r for r in csv.DictReader(open(R+'participants.tsv'),delimiter='\t')}
ld=lambda p: np.asarray(nib.load(p).dataobj,float)
rows=[]
for grp in ('CONTROL','SCHZ'):
    for d in open(G+'list_%s.txt'%grp).read().split():
        s=os.path.basename(d).replace('.results',''); d+='/'
        for arm,f in [('pre','reho_prefix'),('post','reho_postfix'),('hist','reho_hist'),('mask','mask_epi_anat.'+s),('sd','errts_sd')]:
            o=N+s+'_'+arm+'.nii.gz'
            if not os.path.exists(o): subprocess.run(['3dAFNItoNIFTI','-prefix',o,d+f+'+tlrc'],env=env,capture_output=True)
        m=ld(N+s+'_mask.nii.gz')>0; a=ld(N+s+'_pre.nii.gz'); b=ld(N+s+'_post.nii.gz'); h=ld(N+s+'_hist.nii.gz'); sd=ld(N+s+'_sd.nii.gz')
        en=np.loadtxt(d+'motion_%s_enorm.1D'%s); pr=part[s]; ok=m&(a>0)
        rows.append(dict(subject=s,group=grp,age=float(pr['age']),sex=pr['gender'],motion=en.mean(),errts_sd=sd[m].mean(),
            pre_zero_frac=(m&(a==0)).sum()/m.sum(),pre_ratio_all=a[m].mean()/b[m].mean(),pre_ratio_nonzero=(a[ok]/b[ok]).mean(),
            pre_rel_err=(np.abs(a[m]-b[m])/b[m]).mean(),pre_corr=np.corrcoef(a[m],b[m])[0,1],hist_ratio=h[m].mean()/b[m].mean(),hist_corr=np.corrcoef(h[m],b[m])[0,1],
            pre_mean=a[m].mean(),post_mean=b[m].mean(),hist_mean=h[m].mean()))
keys=list(rows[0].keys())
with open(G+'subjects_summary_dpabi.tsv','w') as f:
    f.write('\t'.join(keys)+'\n')
    for r in rows: f.write('\t'.join(r[k] if isinstance(r[k],str) else '%.4f'%r[k] for k in keys)+'\n')
C=[r for r in rows if r['group']=='CONTROL']; S=[r for r in rows if r['group']=='SCHZ']
print('CONTROL n=%d SCHZ n=%d'%(len(C),len(S)))
for k in ('age','motion','errts_sd','pre_zero_frac','pre_ratio_all','pre_ratio_nonzero','pre_rel_err','pre_corr','hist_ratio','hist_corr'):
    c=np.array([r[k] for r in C]); s=np.array([r[k] for r in S]); t,pv=stats.ttest_ind(s,c)
    print('%-16s CONTROL %.3f±%.3f (%.3f-%.3f)  SCHZ %.3f±%.3f (%.3f-%.3f)  p=%.3f'%(k,c.mean(),c.std(ddof=1),c.min(),c.max(),s.mean(),s.std(ddof=1),s.min(),s.max(),pv))
fc=sum(r['sex']=='F' for r in C); fs=sum(r['sex']=='F' for r in S)
print('sex F/M          CONTROL %d/%d  SCHZ %d/%d  Fisher p=%.3f'%(fc,len(C)-fc,fs,len(S)-fs,stats.fisher_exact([[fc,len(C)-fc],[fs,len(S)-fs]])[1]))
a=np.array([r['pre_zero_frac'] for r in rows]); print('all: pre zero-frac mean %.3f range %.3f-%.3f; pre_corr mean %.3f; pre_ratio_all %.3f; corr(pre_rel_err, sd)=%.2f'%(a.mean(),a.min(),a.max(),np.mean([r['pre_corr'] for r in rows]),np.mean([r['pre_ratio_all'] for r in rows]),np.corrcoef([r['pre_rel_err'] for r in rows],[r['errts_sd'] for r in rows])[0,1]))
for k in ('pre_mean','hist_mean','post_mean'):
    c=np.array([r[k] for r in C]); s=np.array([r[k] for r in S]); t,pv=stats.ttest_ind(s,c); d=(s.mean()-c.mean())/np.sqrt((s.var(ddof=1)+c.var(ddof=1))/2)
    print('SCZ-CTRL global mean %-10s CONTROL %.4f SCHZ %.4f diff %+.4f t(%d)=%.2f p=%.3f d=%.2f'%(k,c.mean(),s.mean(),s.mean()-c.mean(),len(C)+len(S)-2,t,pv,d))
