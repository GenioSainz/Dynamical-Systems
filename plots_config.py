import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

plt.ioff()

def get_filename(name,extension):
    now  = datetime.now()
    date = now.strftime("%Y-%m-%d_%H-%M-%S")
    return f"{name}_{date}{extension}"

def plot_sets(ax,gr=False,ti='',xla=False,yla=False,zla=False,xli=False,yli=False,zli=False,ticks_off=False,xticks_off=False,yticks_off=False,zticks_off=False, ba=False, ar=False,leg=False,view=False):
    
    ax.set_title(ti)
    if gr:  ax.grid(gr);ax.set_axisbelow(True)
    if xla: ax.set_xlabel(xla)
    if yla: ax.set_ylabel(yla)
    if zla: ax.set_zlabel(zla)

    if xticks_off: ax.set_xticklabels([])
    if yticks_off: ax.set_yticklabels([])
    if zticks_off: ax.set_zticklabels([])

    if   ticks_off==1: ax.set_xticklabels([]); ax.set_xticks([]);ax.set_yticklabels([]); ax.set_yticks([])
    elif ticks_off==2: ax.set_xticklabels([])
    elif ticks_off==3: ax.set_yticklabels([])

    if ba: ax.set_box_aspect(ba)
    if ar: ax.set_aspect(ar)

    if xli: ax.set_xlim(xli)
    if yli: ax.set_ylim(yli)
    if zli: ax.set_zlim(zli)

    if leg: ax.legend(**leg)

    if view:ax.view_init(**view)
 
px2inch = 1/plt.rcParams['figure.dpi']

## Custom styles
##################
plt.rcdefaults()

FS = 14

plt.rc('axes'  ,titlesize=FS) # title
plt.rc('axes'  ,labelsize=FS+1) # xy-labels font
plt.rc('grid'  ,linewidth=0.5) 
plt.rc('grid'  ,alpha=0.5)
plt.rc('grid'  ,linestyle='-.') 

#plt.rc('axes'  ,facecolor='whitesmoke')
plt.rc('xtick' ,labelsize=FS) # x-ticks font
plt.rc('ytick' ,labelsize=FS) # x-ticks font 

plt.rc('legend',fontsize =FS-1) # legend font
plt.rc('legend',facecolor='w')
plt.rc('lines' ,linewidth=1)   

plt.rcParams.update({
    "text.usetex": False,
    "font.family": "serif",
    "font.serif": "Times New Roman",
    "font.size":FS-2
})

