from matplotlib.patches import Circle


def parte2(dist,alpha,D,n,yrepres,y0):
    import numpy as np
    import warnings
    warnings.filterwarnings('ignore')
    import matplotlib.pyplot as plt
    plt.style.use('bmh')
    import ipywidgets as widgets
    from IPython.display import display
    import io
    import base64
    from IPython.display import clear_output
    #Focal de la lente
    fp = 0.2 # 20 cm
    # Separacion entre fuentes virtuales
    x0 = dist
    a = 2*x0*np.tan((n-1)*alpha) #separacion entre fuentes virtuales
    xlimit = (D-x0)*np.tan((n-1)*alpha) # distancia desde el eje que ocupa el patron de interferencias

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
    figbwidg = widgets.HTML("""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf.getvalue()).decode('ascii')))
    plt.close(fig)

    fig2,ax2 = plt.subplots(1,1)
    ax2.set_xlabel("x (mm)")
    ax2.set_ylabel("y (mm)")
    #ax2.set_xlim(0,x.max()*1e3)
    #ax2.set_ylim(-yrepres,yrepres)
    ax2.set_title('Pantalla')
    ax2.pcolormesh(np.zeros((500,500)))
    buf2 = io.BytesIO()
    plt.savefig(buf2, format='png')
    buf2.seek(0)
    figbwidg2 = widgets.HTML("""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf2.getvalue()).decode('ascii')))
    figboxlens = widgets.HBox([figbwidg,figbwidg2])
    plt.close(fig2)
    clear_output()

    #########
    aprimawidg = widgets.FloatText(0,description='a\'. (mm)',color='#C13535')

    def changelens(xlens=D-0.1):
        s = -xlens
        sp = D - xlens
        beta = sp/s
        aprima = beta*a
        figbwidg.observe(repsetuplens(xlens),names='new')
        spref = (D + np.sqrt(D**2 - 4*fp*D))/2 #Posicion correcta
        sref = spref-D
        figbwidg2.observe(repimage(xlens,sref,aprima),names='new')
        aprimawidg.observe(updateaprima(aprima),names='new')
        return

    def updateaprima(aprima):
        aprimawidg.value=round(-aprima*1e3,2) # en mm
        return


    def repsetuplens(xlens):
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
        ax.annotate("", xy=(np.abs(xlens), y0*1.5), xytext=(np.abs(xlens),-y0*1.5),
                    arrowprops=dict(arrowstyle="<->",color='k')) # representacion lente
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        clear_output()
        figbwidg.value ="""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf.getvalue()).decode('ascii'))
        clear_output()
        plt.close(fig)
        return

    def repimage(xlens,sref,ap):
        fig2,ax2 = plt.subplots(1,1,figsize=(4,4))
        rad = 6*np.abs((xlens+ sref)/sref) + 0.25 # Nota: sref < 0
        circle1 = Circle((0,-ap*1e3/2), radius=rad, color='r',alpha = 1 - 1.7*np.abs((xlens+sref)/sref))
        circle2 = Circle((0,ap*1e3/2), radius=rad, color='r',alpha = 1- 1.7*np.abs((xlens+sref)/sref))
        ax2.add_artist(circle1)
        ax2.add_artist(circle2)
        ax2.set_ylabel("y (mm)")
        ax2.set_xlim(-yrepres,yrepres)
        ax2.set_ylim(-yrepres,yrepres)
        ax2.set_title('Pantalla')
        buf2 = io.BytesIO()
        plt.savefig(buf2, format='png')
        buf2.seek(0)
        clear_output()
        figbwidg2.value ="""<img src='data:image/png;base64,{}'/>""".format(base64.b64encode(buf2.getvalue()).decode('ascii'))
        clear_output()
        plt.close(fig2)
        return


    PosLenswidg = widgets.FloatSlider(value=0.4,min=x0+0.02,max=0.42,step=0.01,description='Dist Fuente-Lente',orientation='horizontal')
    changeposlens = widgets.interactive(changelens,xlens=PosLenswidg)
    finalwidg = widgets.HBox([figboxlens,aprimawidg])
    display(changeposlens,finalwidg)
    return