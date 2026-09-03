#!/usr/bin/env python3
"""Enlarged-sample (before arm = 4c2bd54 reho_prefix, NaN voxels; after arm = reho_postfix) (proc_v1 + proc) demographics, per-subject before/after statistics and global-mean tests."""
import nibabel as nib, numpy as np, os, subprocess, csv
from scipy import stats
R='/home/user/reho-pilot/'; G=R+'group_ext/'; N=R+'nifti_ext/'; os.makedirs(N,exist_ok=True)
env=dict(os.environ,PATH='/home/user/afni-bin/linux_ubuntu_24_64:'+os.environ['PATH'],LD_LIBRARY_PATH='/home/user/afni-bin/linux_ubuntu_24_64')
part={r['participant_id']:r for r in csv.DictReader(open(R+'participants.tsv'),delimiter='\t')}
ld=lambda p: np.asarray(nib.load(p).dataobj,float)
rows=[]
for grp in ('CONTROL','SCHZ'):
    for d in open(G+'list_%s.txt'%grp).read().split():
        s=os.path.basename(d).replace('.results',''); d+='/'; src='ext' if '/proc/' in d else 'pilot'
        for arm,f in [('mid','reho_prefix'),('fixed','reho_postfix'),('mask','mask_epi_anat.'+s),('sd','errts_sd')]:
            o=N+s+'_'+arm+'.nii.gz'
            if not os.path.exists(o): subprocess.run(['3dAFNItoNIFTI','-prefix',o,d+f+'+tlrc'],env=env,capture_output=True)
        m=ld(N+s+'_mask.nii.gz')>0; h=ld(N+s+'_mid.nii.gz'); b=ld(N+s+'_fixed.nii.gz'); sd=ld(N+s+'_sd.nii.gz')
        en=np.loadtxt(d+'motion_%s_enorm.1D'%s); cen=np.loadtxt(d+'censor_%s_combined_2.1D'%s)
        cf=float([l for l in open(d+'out.ss_review.%s.txt'%s) if 'censor fraction' in l][0].split(':')[1])
        hok=m&~np.isnan(h); pr=part[s]
        rows.append(dict(subject=s,group=grp,source=src,age=float(pr['age']),sex=pr['gender'],motion_all=en.mean(),motion_ret=en[cen>0].mean(),
            censor_frac=cf,errts_sd=sd[m].mean(),hist_nan_frac=(m&np.isnan(h)).sum()/m.sum(),
            hist_ratio=(h[hok]/b[hok]).mean(),hist_rel_err=(np.abs(h[hok]-b[hok])/b[hok]).mean(),hist_corr=np.corrcoef(h[hok],b[hok])[0,1],
            hist_mean0=np.nan_to_num(h[m]).mean(),hist_mean_valid=h[hok].mean(),fixed_mean=b[m].mean()))
keys=list(rows[0].keys())
with open(G+'subjects_summary_ext.tsv','w') as f:
    f.write('\t'.join(keys)+'\n')
    for r in rows: f.write('\t'.join(r[k] if isinstance(r[k],str) else '%.4f'%r[k] for k in keys)+'\n')
def report(sel,label):
    C=[r for r in rows if r['group']=='CONTROL' and sel(r)]; S=[r for r in rows if r['group']=='SCHZ' and sel(r)]
    print('\n== %s: CONTROL n=%d SCHZ n=%d'%(label,len(C),len(S)))
    for k in ('age','motion_all','motion_ret','censor_frac','errts_sd','hist_nan_frac','hist_ratio','hist_rel_err','hist_corr'):
        c=np.array([r[k] for r in C]); s=np.array([r[k] for r in S]); t,pv=stats.ttest_ind(s,c)
        print('%-14s CONTROL %.3f±%.3f (%.3f-%.3f)  SCHZ %.3f±%.3f (%.3f-%.3f)  p=%.3f'%(k,c.mean(),c.std(ddof=1),c.min(),c.max(),s.mean(),s.std(ddof=1),s.min(),s.max(),pv))
    fc=sum(r['sex']=='F' for r in C); fs=sum(r['sex']=='F' for r in S)
    print('sex F/M        CONTROL %d/%d  SCHZ %d/%d  Fisher p=%.3f'%(fc,len(C)-fc,fs,len(S)-fs,stats.fisher_exact([[fc,len(C)-fc],[fs,len(S)-fs]])[1]))
    a=np.array([r['hist_nan_frac'] for r in C+S]); print('all: hist_nan_frac mean %.3f range %.3f-%.3f; hist_corr mean %.3f; hist_ratio mean %.3f'%(a.mean(),a.min(),a.max(),np.mean([r['hist_corr'] for r in C+S]),np.mean([r['hist_ratio'] for r in C+S])))
    for k in ('hist_mean0','hist_mean_valid','fixed_mean'):
        c=np.array([r[k] for r in C]); s=np.array([r[k] for r in S]); t,pv=stats.ttest_ind(s,c); d=(s.mean()-c.mean())/np.sqrt((s.var(ddof=1)+c.var(ddof=1))/2)
        print('SCZ-CTRL global mean %-16s diff %.4f t(%d)=%.2f p=%.3f d=%.2f'%(k,s.mean()-c.mean(),len(C)+len(S)-2,t,pv,d))
report(lambda r: True,'ALL 73')
report(lambda r: r['source']=='ext','EXTENSION ONLY')
report(lambda r: r['source']=='pilot','ORIGINAL 40 (check)')
