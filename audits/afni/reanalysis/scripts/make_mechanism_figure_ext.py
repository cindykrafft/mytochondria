import sys, numpy as np, csv
sys.path.insert(0,'../../reproductions')
import reho_tie_sim as S
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
rng=np.random.default_rng(1); M,N=27,148; TR=2.0
def make_bp(M,N,rho=0.6):
    x=np.sqrt(rho)*rng.standard_normal(N)+np.sqrt(1-rho)*rng.standard_normal((M,N))
    f=np.fft.rfftfreq(N,TR); X=np.fft.rfft(x,axis=1); X[:,(f<0.01)|(f>0.1)]=0
    y=np.fft.irfft(X,n=N,axis=1); return y/y.std()
sds=np.array([0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.6,0.75,1,1.5,2,3,5,10])
res={}
for lab,gen in [('white',lambda: S.make(M,N)),('band-passed',lambda: make_bp(M,N))]:
    ratio=[];err=[]
    for sd in sds:
        r=[];e=[]
        for _ in range(60):
            blk=sd*gen(); t=S.reho(blk,False); b=S.reho(blk,True,True); b=0.0 if np.isnan(b) else b   # before-fix arm: guard returns 0
            r.append(b/t); e.append(abs(b-t)/t)
        ratio.append(np.mean(r)); err.append(np.mean(e))
    res[lab]=(np.array(ratio),np.array(err))
    print(lab,' '.join('%.2f:%.2f'%(s,r) for s,r in zip(sds,res[lab][0])))
rows=list(csv.DictReader(open('fig_inputs/subjects_summary_ext73.tsv'),delimiter='\t'))
sd_r=np.array([float(r['errts_sd']) for r in rows]); ratio_r=np.array([float(r['A_mean'])/float(r['B_mean']) for r in rows]); err_r=np.array([float(r['rel_err_all']) for r in rows])
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.titlesize':9,'axes.labelsize':8})
BLUE='#2a78d6'; ORANGE='#eb6834'; AQUA='#1baf7a'; INK='#0b0b0b'; INK2='#52514e'; RULE='#d9d8d3'
fig,axs=plt.subplots(1,2,figsize=(7.2,2.9),dpi=300); plt.subplots_adjust(wspace=0.32,left=0.08,right=0.98,top=0.9,bottom=0.2)
for ax,(idx,ylabel,yr,real) in zip(axs,[(0,'ReHo before fix / after fix',(0,1.05),ratio_r),(1,'Relative error of ReHo before fix',(0,1.05),err_r)]):
    for lab,col in [('white',BLUE),('band-passed',AQUA)]:
        ax.plot(sds,res[lab][idx],'-',color=col,lw=2,label='Simulation, %s Gaussian input'%lab)
    ax.scatter(sd_r,real,s=18,c=ORANGE,edgecolors='white',linewidths=0.6,zorder=4,label='ds000030 participants (n = 73), whole-brain mean')
    ax.set_xscale('log'); ax.set_xlim(0.04,12); ax.set_ylim(*yr); ax.set_xlabel('SD of the time series handed to 3dReHo'); ax.set_ylabel(ylabel)
    ax.set_xticks([0.05,0.1,0.3,1,3,10]); ax.set_xticklabels(['0.05','0.1','0.3','1','3','10'])
    for s in ['top','right']: ax.spines[s].set_visible(False)
    for s in ['left','bottom']: ax.spines[s].set_color(RULE)
    ax.tick_params(colors=INK2,length=2); ax.grid(axis='y',color=RULE,lw=0.5,zorder=0); ax.axvspan(0.3,2,color='#f0efec',zorder=0)
axs[0].text(0.78,0.08,'percent-signal /\nz-scored data',ha='center',va='bottom',color=INK2,fontsize=7)
axs[0].text(5.5,0.08,'raw scanner\nunits',ha='center',va='bottom',color=INK2,fontsize=7)
axs[1].legend(frameon=False,fontsize=6.5,loc='upper right')
for ax,l in zip(axs,'AB'): ax.text(-0.18,1.04,l,transform=ax.transAxes,fontsize=12,fontweight='bold')
P='fig_inputs/'
fig.savefig(P+'mechanism.pdf',bbox_inches='tight'); fig.savefig(P+'mechanism.png',bbox_inches='tight',dpi=300); print('saved')
