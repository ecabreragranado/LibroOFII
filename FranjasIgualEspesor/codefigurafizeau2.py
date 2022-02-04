import numpy as np
import ipywidgets as widgets
import matplotlib.pyplot as plt



n = 1.45
alpha = 2*np.pi/180
D = 0.1e-2
r = (n-1)/(1+n)
t = 2/(1+n)
tp = 2*n/(1+n)
I0 = 1
I1 = I0*r**2
I2 = I0*(t*r*tp)**2


def fun(Deltalambda,Lambda,alpha):
    fig = plt.figure(figsize=(10,4))
    x = np.linspace(0,D,500)
    y = np.linspace(0,D/2,20)
    X,Y = np.meshgrid(x,y)
    h = X*np.tan(alpha)
    Lambda = Lambda*1e-9
    Deltalambda = Deltalambda*1e-9
    lc = Lambda**2/Deltalambda
    deltag = 4*np.pi*n*h/Lambda
    deltatot = deltag + np.pi
    Difcamino = 2*n*h
    Itot = I1 + I2 + (2*np.sqrt(I1*I2)*np.cos(deltatot))*(Difcamino<lc)
    Itot=Itot
    plt.pcolormesh(X,Y,Itot,cmap='gray',shading='auto')
    plt.axis('off')
    plt.show()
                     


    
interactive_plot = widgets.interactive(fun, Deltalambda=(20,100,2),Lambda=(400,600,20),  alpha=(5e-4, 5e-3, 5e-4))
interactive_plot.children[2].readout_format='.4f'
output = interactive_plot.children[-1]
output.layout.height = '600px'





texto = widgets.Text(value = str(np.round(interactive_plot.children[1].value**2/interactive_plot.children[0].value,2))+' nm',description='lc')
caja1 = widgets.HBox([interactive_plot,texto])
display(caja1)   