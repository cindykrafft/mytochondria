# Figure: the defect's amplitude dependence at the group level. Rows: t(residual SD, SCZ-CON), t(pre-fix z-ReHo), t(post-fix z-ReHo); right: voxelwise scatter.
import numpy as np, nibabel as nib
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
F='./fig_inputs/'
def load(n):
    im=nib.as_closest_canonical(nib.load(F+n)); return np.asarray(im.dataobj,float)
mni=load('mni_3mm.nii.gz'); gm=load('gmask90.nii.gz')>0
tsd=load('t90_sd.nii.gz'); tpre=load('t90_pre.nii.gz'); tpost=load('t90_post.nii.gz')
xs=np.where(mni.max(axis=(1,2))>0)[0]; ys=np.where(mni.max(axis=(0,2))>0)[0]; x0,x1,y0,y1=xs[0]-1,xs[-1]+2,ys[0]-1,ys[-1]+2
def slab(v,z): return np.rot90(v[x0:x1,y0:y1,z])
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.titlesize':9,'axes.labelsize':8})
INK='#0b0b0b'; INK2='#52514e'; RULE='#d9d8d3'
div=LinearSegmentedColormap.from_list('div',['#104281','#2a78d6','#9ec5f4','#f0efec','#f2a09f','#e34948','#8e1d1c'])
fig=plt.figure(figsize=(7.2,5.6),dpi=300); gs=fig.add_gridspec(1,2,width_ratios=[1.55,1.0],wspace=0.18)
zs=[18,24,30,36]; gL=gs[0].subgridspec(3,len(zs),wspace=0.03,hspace=0.06); lim=4.5
rows=[(tsd,'Residual amplitude\nSCZ vs control'),(tpre,'ReHo, before fix\nSCZ vs control'),(tpost,'ReHo, after fix\nSCZ vs control')]
for r,(t,lab) in enumerate(rows):
    for c,z in enumerate(zs):
        ax=fig.add_subplot(gL[r,c]); u=slab(mni,z); ax.imshow(u,cmap='gray',vmin=0,vmax=u.max()*1.15,interpolation='nearest'); ax.set_facecolor('black'); ax.axis('off')
        m=slab(t*gm,z); m=np.ma.masked_where(np.abs(m)<1.96,m); im=ax.imshow(m,cmap=div,vmin=-lim,vmax=lim,interpolation='nearest')
        if c==0: ax.text(-0.06,0.5,lab,transform=ax.transAxes,rotation=90,va='center',ha='right',color=INK,fontsize=7.5)
        if r==0: ax.set_title('z = %+d mm'%((z-32)*3+8),color=INK2,fontsize=7,pad=2)
fig.text(0.02,0.96,'A',fontsize=12,fontweight='bold',color=INK)
cax=fig.add_axes([0.13,0.06,0.32,0.012]); cb=fig.colorbar(im,cax=cax,orientation='horizontal',ticks=[-4,-2,0,2,4]); cb.set_label('t (|t| > 1.96 shown)',color=INK2,fontsize=7); cb.ax.tick_params(labelsize=6.5,colors=INK2,length=2); cb.outline.set_edgecolor(RULE)
# B: voxelwise scatter, 2D histograms
gR=gs[1].subgridspec(2,1,hspace=0.45)
for i,(t,lab) in enumerate([(tpre,'ReHo t, before fix'),(tpost,'ReHo t, after fix')]):
    ax=fig.add_subplot(gR[i]); x=tsd[gm]; y=t[gm]; r=np.corrcoef(x,y)[0,1]
    ax.hexbin(x,y,gridsize=45,cmap=LinearSegmentedColormap.from_list('s',['#ffffff','#9ec5f4','#256abf','#0d366b']),mincnt=1,linewidths=0.1)
    ax.set_xlim(-6,6); ax.set_ylim(-6,6); ax.set_xlabel('residual-amplitude t, SCZ vs control'); ax.set_ylabel(lab)
    ax.axhline(0,color=RULE,lw=0.6); ax.axvline(0,color=RULE,lw=0.6)
    for s in ['top','right']: ax.spines[s].set_visible(False)
    for s in ['left','bottom']: ax.spines[s].set_color(RULE)
    ax.tick_params(colors=INK2,length=2); ax.text(0.03,0.95,'r = %.2f across %s voxels'%(r,format(gm.sum(),',')),transform=ax.transAxes,color=INK2,fontsize=7,va='top')
    ax.set_aspect('equal')
fig.text(0.60,0.96,'B',fontsize=12,fontweight='bold',color=INK)
fig.savefig(F+'amplitude.png',dpi=300,bbox_inches='tight',facecolor='white'); fig.savefig(F+'amplitude.pdf',bbox_inches='tight',facecolor='white'); print('saved')
