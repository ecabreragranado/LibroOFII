import numpy as np
import ipywidgets as widgets
import matplotlib.pyplot as plt


Lambda = 4.1e-7
n = 1.45
alpha = 2*np.pi/180
D = 0.1e-2
r = (n-1)/(1+n)
t = 2/(1+n)
tp = 2*n/(1+n)
I0 = 1
I1 = I0*r**2
I2 = I0*(t*r*tp)**2


def fun(n,alpha):
    fig, (ax1,ax2) = plt.subplots(2)
    x = np.linspace(0,D,500)
    y = np.linspace(0,D/2,20)
    X,Y = np.meshgrid(x,y)
    h = X*np.tan(alpha)
    deltag = 4*np.pi*n*h/Lambda
    deltatot = deltag + np.pi
    Itot = I1 + I2 + 2*np.sqrt(I1*I2)*np.cos(deltatot)
    ax1.plt.pcolormesh(X,Y,Itot,cmap='gray',shading='auto')
    ax1.plt.axis('off')
    ax1.plt.show()
                     
def fun2(n,alpha):
    fig2 = plt.figure(figsize=(10,4))
    plt.hlines(0, 0, D,linewidth=2)
    plt.vlines(D,0,D*np.tan(alpha),linewidth=2,color='black')
    x = np.linspace(0,D,150)
    plt.plot(x,x*np.tan(alpha),color = 'black',linewidth=2)
    plt.ylim(-1.5e-5,1e-5)
    plt.xlim(0,D)
    plt.annotate(r'$\alpha$',(D/3,0.000001),fontsize=18)
    plt.axis('off')
    
def fun3(n,alpha):
    fig3 = plt.figure(figsize=(10,4))
    npointsinter = 20
    Int = Lambda/(2*n*alpha)
    N = int((D/Int)*npointsinter)
    x = np.linspace(0,D,N)
    h = x*np.tan(alpha)
    deltag = 4*np.pi*n*h/Lambda
    deltatot = deltag + np.pi
    Itotx = I1 + I2 + 2*np.sqrt(I1*I2)*np.cos(deltatot)
    plt.plot(x,Itotx,color = 'red',linewidth=2)
    plt.ylim(0,0.3)
    plt.xlim(0,D)
    plt.axis('off')
                     
    
interactive_plot = widgets.interactive(fun, n=(1.05, 2.0),  alpha=(5e-4, 5e-3, 5e-4))
interactive_plot.children[1].readout_format='.4f'
output = interactive_plot.children[-1]
output.layout.height = '600px'

interactive_plot2 = widgets.interactive(fun2, n=(1.05, 2.0), alpha=(5e-4, 5e-3, 5e-4))
interactive_plot2.children[1].readout_format='.4f'
output2 = interactive_plot2.children[-1]
output2.layout.height = '600px'

interactive_plot3 = widgets.interactive(fun3, n=(1.05, 2.0),  alpha=(5e-4, 5e-3, 5e-4))
interactive_plot3.children[1].readout_format='.4f'

output = interactive_plot.children[-1]
output.layout.height = '600px'


l1 = widgets.link((interactive_plot2.children[0], 'value'), (interactive_plot.children[0], 'value'))
l2 = widgets.link((interactive_plot2.children[1], 'value'), (interactive_plot.children[1], 'value'))
l3 = widgets.link((interactive_plot2.children[0], 'value'), (interactive_plot3.children[0], 'value'))
l4 = widgets.link((interactive_plot2.children[1], 'value'), (interactive_plot3.children[1], 'value'))



texto = widgets.Text(value = str(np.round(Lambda*1000/(2*interactive_plot2.children[0].value*interactive_plot2.children[1].value),4))+' mm',description='Interfranja')
caja1 = widgets.HBox([interactive_plot2,interactive_plot])
caja2 = widgets.HBox([texto,interactive_plot3])
cajatot = widgets.VBox([caja1,caja2])
display(cajatot)   