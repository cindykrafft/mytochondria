#!/usr/bin/env python3
"""Per-subject pre-fix vs post-fix 3dReHo statistics with NaN accounted for explicitly.
The pre-fix 3dReHo returns NaN in voxels where its tie correction zeroes the denominator;
AFNI tools silently read NaN as 0, so both views are reported."""
import nibabel as nib, numpy as np, csv, sys
from scipy import stats
R='/home/user/reho-pilot/'; N=R+'nifti/'
rows=list(csv.DictReader(open(R+'group/subjects_summary.tsv'),delimiter='\t'))
ld=lambda p: np.asarray(nib.load(p).dataobj,float)
hdr=['subject','group','errts_sd','censor_frac','nan_frac_old','reho_old_mean_valid','reho_fixed_mean','rel_err_valid_mean','rel_err_valid_max','spatial_corr_valid','rel_err_nan_as_zero','spatial_corr_nan_as_zero']
out=[]
for r in rows:
    s=r['subject']; m=ld(N+s+'_mask.nii.gz')>0; a=ld(N+s+'_pre.nii.gz'); b=ld(N+s+'_post.nii.gz')
    nanm=m&np.isnan(a); ok=m&~np.isnan(a)
    rel=np.abs(a[ok]-b[ok])/b[ok]; corr=np.corrcoef(a[ok],b[ok])[0,1]
    a0=np.where(np.isnan(a),0.0,a); rel0=np.abs(a0[m]-b[m])/b[m]; corr0=np.corrcoef(a0[m],b[m])[0,1]
    out.append([s,r['group'],float(r['errts_sd']),float(r['censor_frac']),nanm.sum()/m.sum(),a[ok].mean(),b[m].mean(),rel.mean(),rel.max(),corr,rel0.mean(),corr0])
with open(R+'group/subjects_summary_v2.tsv','w') as f:
    f.write('\t'.join(hdr)+'\n')
    for o in out: f.write('\t'.join([o[0],o[1]]+['%.4f'%v for v in o[2:]])+'\n')
A=np.array([o[2:] for o in out]); g=np.array([o[1] for o in out]); names=hdr[2:]
def show(lbl,mask): print(lbl, ' '.join('%s=%.3f'%(n,A[mask,i].mean()) for i,n in enumerate(names)))
show('ALL ', np.ones(len(g),bool)); show('CTRL', g=='CONTROL'); show('SCHZ', g=='SCHZ')
print('ranges: nan_frac %.3f-%.3f ; rel_err_valid %.3f-%.3f ; corr_valid %.3f-%.3f ; corr_nan0 %.3f-%.3f'%(A[:,2].min(),A[:,2].max(),A[:,5].min(),A[:,5].max(),A[:,7].min(),A[:,7].max(),A[:,9].min(),A[:,9].max()))
print('corr(nan_frac, errts_sd)=%.3f  corr(corr_valid, errts_sd)=%.3f  corr(rel_err_valid, errts_sd)=%.3f'%(np.corrcoef(A[:,2],A[:,0])[0,1],np.corrcoef(A[:,7],A[:,0])[0,1],np.corrcoef(A[:,5],A[:,0])[0,1]))
s=g=='SCHZ'; c=g=='CONTROL'
for i,n in enumerate(names):
    if n in ('nan_frac_old','reho_old_mean_valid','reho_fixed_mean','errts_sd'):
        t,p=stats.ttest_ind(A[s,i],A[c,i]); d=(A[s,i].mean()-A[c,i].mean())/np.sqrt((A[s,i].var(ddof=1)+A[c,i].var(ddof=1))/2); print('SCZ-CTRL %s: diff %.4f t=%.2f p=%.3f d=%.2f'%(n,A[s,i].mean()-A[c,i].mean(),t,p,d))
# global mean ReHo as AFNI would compute it from the old maps (NaN->0), i.e. what a paper's pipeline sees
old0=[]; 
for r in rows:
    sname=r['subject']; m=ld(N+sname+'_mask.nii.gz')>0; a=ld(N+sname+'_pre.nii.gz'); old0.append(np.nan_to_num(a[m]).mean())
old0=np.array(old0); t,p=stats.ttest_ind(old0[s],old0[c]); print('SCZ-CTRL global old ReHo with NaN->0: diff %.4f t=%.2f p=%.3f'%(old0[s].mean()-old0[c].mean(),t,p))
print('old/fixed ratio (valid voxels) mean %.3f range %.3f-%.3f'%((A[:,3]/A[:,4]).mean(),(A[:,3]/A[:,4]).min(),(A[:,3]/A[:,4]).max()))
