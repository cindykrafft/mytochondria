#!/usr/bin/env python3
"""Score each build's SCZ-vs-HC map against the nine regions Cattarinussi et al. 2024 report (Neuromorphometrics labels)."""
import numpy as np, nibabel as nib, subprocess, os, csv
R='/home/user/reho-pilot/dpabi/'; G=R+'group/'
env=dict(os.environ,PATH='/home/user/afni-bin/linux_ubuntu_24_64:'+os.environ['PATH'],LD_LIBRARY_PATH='/home/user/afni-bin/linux_ubuntu_24_64')
def nii(src,dst):
    if not os.path.exists(dst): subprocess.run(['3dAFNItoNIFTI','-prefix',dst,src],env=env,capture_output=True)
    return np.asarray(nib.load(dst).dataobj,float)
atlas=np.asarray(nib.load(R+'atlas/neuromorph_3mm.nii.gz').dataobj,float)
mask=nii(G+'mask90+tlrc',G+'mask90.nii.gz')>0
targets=list(csv.DictReader(open(R+'targets.tsv'),delimiter='\t'))
print('\n== Scoring against Cattarinussi 2024 (SCZ vs HC): region | build | mean t in region | frac voxels p<.001 same sign | corrected cluster (p<.001 / p<.01) of same sign overlaps region')
tcrit=float(open(G+'tcrit.txt').read()) if os.path.exists(G+'tcrit.txt') else 3.4
summary={}
for arm in ('prefix','postfix','hist'):
    t=nii(G+'clust_%s/tt+tlrc[1]'%arm,G+'t_%s.nii.gz'%arm)
    cl={p:(nii(G+'clust_%s/clmap_p%s+tlrc'%(arm,p),G+'cl_%s_p%s.nii.gz'%(arm,p))>0 if os.path.exists(G+'clust_%s/clmap_p%s+tlrc.HEAD'%(arm,p)) else np.zeros_like(mask)) for p in ('0.001','0.01')}
    hits={'0.001':0,'0.01':0}; unc=0
    for tg in targets:
        reg=(atlas==float(tg['label_index']))&mask; sgn=1 if tg['sign']=='pos' else -1
        if reg.sum()==0: print('  %-22s %-8s region empty in mask'%(tg['region'],arm)); continue
        mt=t[reg].mean(); frac=((sgn*t[reg])>tcrit).mean()
        c1=(cl['0.001']&reg&((sgn*t)>0)).sum()>0; c2=(cl['0.01']&reg&((sgn*t)>0)).sum()>0
        hits['0.001']+=c1; hits['0.01']+=c2; unc+= (sgn*mt>0)
        print('  %-22s %-8s expected %s  mean t %+5.2f  frac p<.001 %.3f  cluster %s / %s'%(tg['region'],arm,tg['sign'],mt,frac,'YES' if c1 else 'no','YES' if c2 else 'no'))
    summary[arm]=(unc,hits)
print('\n== Summary: build | regions with mean t of the reported sign (of 9) | regions with a corrected cluster of the reported sign at p<.001 | at p<.01')
for arm,(unc,h) in summary.items(): print('  %-8s %d/9   %d/9   %d/9'%(arm,unc,h['0.001'],h['0.01']))
