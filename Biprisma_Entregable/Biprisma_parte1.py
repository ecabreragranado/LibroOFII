import warnings
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
plt.style.use('bmh')
import ipywidgets as widgets
from IPython.display import display
import io
import base64
from IPython.display import clear_output
#Datos fijos
###################33
D = 1 # Distancia fuente-pantalla
Lambda = 6.33e-7 # longitud de onda de la radiación
k = 2.0*np.pi/Lambda
n = 1.33 # agua
alpha = 0.7*np.pi/180 # ang. del biprisma
y0 = 3.5# tamaño vertical biprisma
yrepres = 4.5 # in mm. Parametro de representación
I1 = 1 # Consideramos irradiancias normalizadas a un cierto valor.
I2 = 1
###########################

fig,ax = plt.subplots(1,1)
ax.plot(0,0,'o',lw=2)
ax.set_xlim(-0.1,D+0.1)
ax.set_ylim(-yrepres*1.5,yrepres*1.5)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (mm)")
ax.set_title('Esquema del montaje experimental')
line1, = ax.plot(np.linspace(-1,D,50),np.zeros(50),'k')
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
figwidg = widgets.HTML("""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf.getvalue()).decode('ascii')))
plt.close(fig)

fig2,ax2 = plt.subplots(1,1)
ax2.set_xlabel("x (mm)")
ax2.set_ylabel("y (mm)")
ax2.set_title('Pantalla')
ax2.pcolormesh(np.zeros((500,500)))
buf2 = io.BytesIO()
plt.savefig(buf2, format='png')
buf2.seek(0)
figwidg2 = widgets.HTML("""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf2.getvalue()).decode('ascii')))
plt.close(fig2)
clear_output()

fig3,ax3 = plt.subplots(1,1)
ax3.set_ylabel("y (mm)")
ax3.set_title('Zoom (3 mm)')
ax3.pcolormesh(np.zeros((50,50)))
buf3 = io.BytesIO()
plt.savefig(buf3, format='png')
buf3.seek(0)
figwidg3 = widgets.HTML("""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf3.getvalue()).decode('ascii')))
figbox = widgets.HBox([figwidg,figwidg2,figwidg3])
plt.close(fig3)
clear_output()

#########
Interfwidg = widgets.FloatText(0,description='Int. (mm)',color='#C13535')

def changeBiprism(x0=0.1):
    a = 2*x0*np.tan((n-1)*alpha) #separacion entre fuentes virtuales
    interfranja = Lambda*D/a 
    xlimit = (D-x0)*np.tan((n-1)*alpha) # distancia desde el eje que ocupa el patron de interferencias
    Pasoespacial = interfranja/20
    xpantalla = np.linspace(-xlimit*1.2,xlimit*1.2,int(xlimit/Pasoespacial))
    X,Y = np.meshgrid(xpantalla,xpantalla)
    delta = (k*a*X/D)
    Itotal = I1 + I2 + (2.0*np.sqrt(I1*I2)*np.cos(delta))*(np.abs(X)<xlimit)
    figwidg.observe(repsetup(x0),names='new')
    figwidg2.observe(repfringes(xpantalla,Itotal),names='new')
    figwidg3.observe(repzoom(xpantalla,Itotal),names='new')
    Interfwidg.observe(updateInterf(interfranja),names='new')
    return

def updateInterf(interfranja):
    Interfwidg.value=round(interfranja*1e3,2)
    return
    

def repsetup(x0):
    fig,ax = plt.subplots(1,1,figsize=(7,5))
    ax.plot(0,0,'o',lw=2)
    ax.set_xlim(-0.1,D+0.1)
    ax.set_ylim(-yrepres*1.5,yrepres*1.5)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (mm)")
    ax.set_title('Esquema del montaje experimental')
    ax.plot(np.linspace(-1,D,50),np.zeros(50),'k')
    ax.vlines(x0,-y0,y0,'r',lw=2)
    ax.vlines(D,-y0*3,y0*3,lw=4)
    ax.plot(np.linspace(x0,x0+.01,3),(-y0/.01)*np.linspace(x0,x0+.01,3) + y0*(1+x0/.01),'r',lw=2)
    ax.plot(np.linspace(x0,x0+.01,3),(y0/.01)*np.linspace(x0,x0+.01,3) - y0*(1+x0/.01),'r',lw=2)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    clear_output()
    figwidg.value ="""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf.getvalue()).decode('ascii'))
    clear_output()
    plt.close(fig)
    return

def repfringes(x,Itotal):
    fig2,ax2 = plt.subplots(1,1,figsize=(3,5))
    ax2.set_ylabel("y (mm)")
    ax2.set_xlim(0,x.max()*1e3)
    ax2.set_ylim(-yrepres,yrepres)
    ax2.set_title('Pantalla (mm)')
    ax2.pcolormesh(x*1e3,x*1e3,Itotal.T,cmap = 'gray',vmin=0,vmax=4)
    buf2 = io.BytesIO()
    plt.savefig(buf2, format='png')
    buf2.seek(0)
    clear_output()
    figwidg2.value ="""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf2.getvalue()).decode('ascii'))
    clear_output()
    plt.close(fig2)
    return

def repzoom(x,Itotal):
    fig3,ax3 = plt.subplots(1,1,figsize=(3,5))
    ax3.set_ylabel("y (mm)")
    ax3.set_xlim(0,x.max()*1e3)
    ax3.set_ylim(-2,2)
    ax3.set_title('Zoom (4 mm)')
    ax3.pcolormesh(x*1e3,x*1e3,Itotal.T,cmap = 'gray',vmin=0,vmax=4)
    buf3 = io.BytesIO()
    plt.savefig(buf3, format='png')
    buf3.seek(0)
    clear_output()
    figwidg3.value ="""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf3.getvalue()).decode('ascii'))
    clear_output()
    plt.close(fig3)
    return


Positionwidg = widgets.FloatSlider(value=0.3,min=0.08,max=0.35,step=0.02,description='Fuente-Biprisma (m)',orientation='horizontal')
changepos = widgets.interactive(changeBiprism,x0=Positionwidg)
resultswidg = widgets.HBox([figbox,Interfwidg])
display(changepos,resultswidg)