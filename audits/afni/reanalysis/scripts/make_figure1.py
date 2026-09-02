# Builds results/figure1.{png,pdf}. Inputs: NIfTI exports of one subject's pre/post ReHo maps, the group t-maps,
# the 90 %-coverage group mask, the MNI template resampled to 3 mm, and results/subjects_summary_v2.tsv,
# placed in ./fig_inputs/ (see README "Reproducing").
import numpy as np, nibabel as nib, csv
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
F='./fig_inputs/'
def load(n):
    im=nib.as_closest_canonical(nib.load(F+n)); return np.asarray(im.dataobj, float)
mni=load('mni_3mm.nii.gz'); gm=load('gmask90.nii.gz')>0
tpre=load('t90_pre.nii.gz'); tpost=load('t90_post.nii.gz')
rpre=load('reho_pre_sub-10159.nii.gz'); rpost=load('reho_post_sub-10159.nii.gz')
# crop to brain bounding box (in-plane)
xs=np.where(mni.max(axis=(1,2))>0)[0]; ys=np.where(mni.max(axis=(0,2))>0)[0]
x0,x1,y0,y1=xs[0]-1,xs[-1]+2,ys[0]-1,ys[-1]+2
def slab(vol,z): return np.rot90(vol[x0:x1,y0:y1,z])
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.titlesize':9,'axes.labelsize':8})
BLUE='#2a78d6'; ORANGE='#eb6834'; INK='#0b0b0b'; INK2='#52514e'; RULE='#d9d8d3'
seq=LinearSegmentedColormap.from_list('seq',['#e4eefb','#9ec5f4','#5598e7','#256abf','#104281','#0d366b'])
div=LinearSegmentedColormap.from_list('div',['#104281','#2a78d6','#9ec5f4','#f0efec','#f2a09f','#e34948','#8e1d1c'])
W=7.2; fig=plt.figure(figsize=(W,7.0),dpi=300)
gs=fig.add_gridspec(2,1,height_ratios=[1.0,1.15],hspace=0.36)
top=gs[0].subgridspec(1,2,width_ratios=[1.15,1.0],wspace=0.30)
und_kw=dict(cmap='gray',vmin=0,vmax=None,interpolation='nearest')
def underlay(ax,z):
    u=slab(mni,z); ax.imshow(u,cmap='gray',vmin=0,vmax=u.max()*1.15,interpolation='nearest'); ax.set_facecolor('black'); ax.axis('off')
# ---- A: one subject, same slice, old vs fixed
gA=top[0].subgridspec(1,2,wspace=0.03)
z=32; vmax=0.9
for i,(v,lab) in enumerate([(rpre,'Old 3dReHo'),(rpost,'Fixed 3dReHo')]):
    ax=fig.add_subplot(gA[i]); underlay(ax,z)
    m=slab(v,z); m=np.ma.masked_where(m<=0,m)
    im=ax.imshow(m,cmap=seq,vmin=0,vmax=vmax,interpolation='nearest')
    ax.set_title(lab,color=INK,pad=3)
    ax.text(0.5,-0.04,'whole-brain mean %.2f'%np.mean(v[v>0]),transform=ax.transAxes,color=INK2,fontsize=7,ha='center',va='top')
axA=[a for a in fig.axes]; fig.canvas.draw(); p0=axA[0].get_position(); p1=axA[1].get_position()
cax=fig.add_axes([p0.x0,p0.y0-0.075,p1.x1-p0.x0,0.011]); cb=fig.colorbar(im,cax=cax,orientation='horizontal'); cb.set_label('ReHo (Kendall W), one subject, identical input',color=INK2,fontsize=7); cb.ax.tick_params(labelsize=6.5,colors=INK2); cb.outline.set_edgecolor(RULE)
fig.text(0.02,0.955,'A',fontsize=12,fontweight='bold',color=INK)
# ---- B: spatial correlation vs residual SD
rows=list(csv.DictReader(open(F+'subjects_summary_v2.tsv'),delimiter='\t'))
ax=fig.add_subplot(top[1])
for grp,col,lab in [('CONTROL',BLUE,'Control (n = 20)'),('SCHZ',ORANGE,'Schizophrenia (n = 20)')]:
    x=[float(r['errts_sd']) for r in rows if r['group']==grp]; y=[float(r['spatial_corr_nan_as_zero']) for r in rows if r['group']==grp]
    ax.scatter(x,y,s=26,c=col,edgecolors='white',linewidths=0.8,label=lab,zorder=3)
ax.set_xlabel('SD of residual time series (% signal)'); ax.set_ylabel('Correlation of old and fixed ReHo maps')
ax.set_ylim(0.2,0.85); ax.set_xlim(0.1,0.56)
for s in ['top','right']: ax.spines[s].set_visible(False)
for s in ['left','bottom']: ax.spines[s].set_color(RULE)
ax.tick_params(colors=INK2,length=2); ax.grid(axis='y',color=RULE,lw=0.5,zorder=0)
ax.legend(frameon=False,loc='lower right',fontsize=7,handletextpad=0.2)
rr=np.corrcoef([float(r['errts_sd']) for r in rows],[float(r['spatial_corr_nan_as_zero']) for r in rows])[0,1]
ax.text(0.02,0.97,'r = %.2f across subjects'%rr,transform=ax.transAxes,color=INK2,fontsize=7,va='top')
fig.text(0.53,0.955,'B',fontsize=12,fontweight='bold',color=INK)
# ---- C: group contrast t-maps old vs fixed, 4 slices
zs=[24,30,36,42]
gC=gs[1].subgridspec(2,len(zs),wspace=0.03,hspace=0.04)
lim=4.5
for r,(t,lab) in enumerate([(tpre,'Old 3dReHo'),(tpost,'Fixed 3dReHo')]):
    for c,z in enumerate(zs):
        ax=fig.add_subplot(gC[r,c]); underlay(ax,z)
        m=slab(t*gm,z); m=np.ma.masked_where(np.abs(m)<1.96,m)
        im=ax.imshow(m,cmap=div,vmin=-lim,vmax=lim,interpolation='nearest')
        if c==0: ax.text(-0.04,0.5,lab,transform=ax.transAxes,rotation=90,va='center',ha='right',color=INK,fontsize=8)
        if r==0: ax.set_title('z = %+d mm'%((z-32)*3+8),color=INK2,fontsize=7,pad=2)
cax=fig.add_axes([0.35,0.045,0.3,0.011]); cb=fig.colorbar(im,cax=cax,orientation='horizontal',ticks=[-4,-2,0,2,4]); cb.set_label('t, schizophrenia vs control, 20 vs 20 (|t| > 1.96 shown)',color=INK2,fontsize=7); cb.ax.tick_params(labelsize=6.5,colors=INK2); cb.outline.set_edgecolor(RULE)
fig.text(0.02,0.475,'C',fontsize=12,fontweight='bold',color=INK)
fig.savefig(F+'figure1.png',dpi=300,bbox_inches='tight',facecolor='white'); fig.savefig(F+'figure1.pdf',bbox_inches='tight',facecolor='white'); fig.savefig(F+'figure1.tiff',dpi=300,bbox_inches='tight',facecolor='white',pil_kwargs={'compression':'tiff_lzw'})
print('saved')
