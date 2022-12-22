#!/usr/bin/env python
# coding: utf-8

# # Franjas de igual espesor
# 
# <center>
# <img src="thinfilmsoap.gif" height=300px style="max-width:60%">
# </center>

#   Hasta ahora hemos visto la interferencia entre las ondas reflejadas o transmitidas en una lámina planoparalela, es decir, una lámina cuyas caras son paralelas y por tanto tiene un espesor o grosor fijo $h$. Si $n$ es el índice de refracción de la lámina y $\theta_t$ el ángulo transmitido o refractado en la primera cara, el desfase debido a la diferencia de camino entre ambas ondas (desfase geometrico $\delta_G$) es, 
# 
# $$\delta_G = \frac{2\pi}{\lambda} 2 h n \cos(\theta_t)$$
# 
# Si la lámina no tiene ambas caras paralelas y su grosor varia localmente, entonces puede ocurrir que diferentes rayos se solapen en algún punto cercano a la superficie (punto P en la figura). Para tratar este problema, consideraremos que ambas caras no se alejan mucho de ser paralelas entre si. En ese caso, podemos considerar el desfase geométrico entre las ondas que interfieren como, 
# 
# $$\delta_G = \frac{2\pi}{\lambda} 2 h n \overline{\cos(\theta_t)}$$
# 
# 
# <center>
#     
# ![imagenFizeau](imagenfizeau3.png)
# 
# </center>
# donde ahora $\overline{\cos(\theta_t)}$ es un promedio de esos valores de $\theta_t$ para los rayos que llegan al punto P. Normalmente se observa en ángulos cercanos a cero, es decir, normal a la superficie y por tanto $\overline{\cos(\theta_t)} \sim 1$, entonces, 
# 
# $$\delta_G = \frac{2\pi}{\lambda} 2 h n$$
# 
# es decir, el desfase irá cambiando a medida que cambia el espesor de la lámina, e irán apareciendo los máximos y mínimos de luz. Es por eso que a este tipo de franjas se les denomina **franjas de igual espesor** (o *franjas de Fizeau*). Este tipo de franjas podemos verlas fácilmente en la superficie de las pompas de jabón. 
# 
# Hay que notar que, si el tipo de interferencia (constructiva o destructiva) y por tanto que aparezcan máximos o mínimos depende del grosor de la lámina en ese punto, el diagrama interferencial se convierte en este caso en un mapa de alturas o curvas de nivel, que nos indican cómo varía la altura de la lámina espacialmente. Es decir, donde se mantenga el espesor de la lámina el resultado de la interferencia será el mismo.
# 
# Nosotros vamos a centrarnos en dos casos: Una cuña y una superficie curva en contacto con otra plana (Anillos de Newton).
# 
# 

# ## Interferencias en una cuña

# Una cuña es la lámina comprendida entre dos superficies planas que forman un ángulo $\alpha$ entre si. Consideraremos que este ángulo es muy pequeño, por lo que podremos seguir utilizando la siguiente expresión para el desfase geométrico entre las ondas que se reflejan en ambas caras de la lámina:
# 
# $$\delta_G = \frac{2 \pi}{\lambda} 2 h n$$
# 
# donde el espesor $h$ varía a lo largo de la cuña y $n$ es su índice de refracción.
# Para calcular el desfase total tenemos que considerar el desfase debido a las reflexiones de las ondas. Este desfase hay que analizarlo en cada caso particular. En lo que resta de este documento vamos a considerar dos posibles casos de cuñas, y en ambos tendremos que añadir un desfase adicional de $\pi$ rad ($\delta_R = \pi$ rad) debido a la reflexiones.
# 
# Estos casos que vamos a considerar son los siguientes:
# 
# 1. Cuña formada por dos bloques de vidrio que forman un cierto ángulo $\alpha$. Se trata de la capa de aire que queda encerrada entre ambos vidrios. En este caso, las ondas que interfieren, en reflexión, son las reflejadas en la segunda cara del bloque superior de vidrio, y en la primera cara del bloque inferior de vidrio.
# 
# <center>
# 
# ![figura](wedgeglassblocks2.png)
# 
# </center>
# 
# 2. Cuña formada por un material dieléctrico de índice de refracción $n$ rodeada de aire.
# 
# En el caso de una lámina en forma de cuña, el espesor de la lámina $h$ aumenta de forma lineal con la distancia al vértice $x$, es decir,
# 
# $$h = x \tan(\alpha) \simeq x \alpha$$
# 
# 
# ### Máximos y mínimos de interferencia.
# 
# En ambos casos planteados, el desfase total entre las ondas que participan en la interferencia es, 
# 
# $$\delta_{tot} = \delta_G + \delta_R = \frac{2 \pi}{\lambda} 2 h n + \pi$$
# 
# Los maximos y minimos de interferencia se obtendrán cuando:
# 
# * Máximos: $\delta_{tot} = 2 m \pi$ rad
# 
# * Mínimos: $\delta_{tot} = (2 m + 1) \pi$ rad.
# 
# Centrándonos en los mínimos de luz, podemos buscar los grosores de la lámina que nos dan mínimos de interferencia:
# 
# <div class="alert alert-block alert-success">
# 
# $$\frac{2 \pi}{\lambda} 2 h_{min} n + \pi = (2 m +1) \pi \Rightarrow h_{min} = \frac{m \lambda}{ 2 n}$$
# 
# </div>
# 
# Estas alturas se pueden pasar a distancias desde el vértice, teniendo en cuenta la relación entre $x$ y $h$ expresada anteriormente, 
# 
# <div class="alert alert-block alert-success">
# 
# $$h_{min} = \frac{m \lambda}{ 2 n} \Rightarrow x_{min} = \frac{m \lambda}{2 n \tan(\alpha)} \sim  x_{min} = \frac{m \lambda}{2 n \alpha} $$
# 
# </div>
# 
# De la expresión anterior vemos que el diagrama interferencial se compone de máximos y mínimos equiespaciados, de modo que, mirando a la cuña desde arriba, veríamos unas franjas de interferencia, donde en el vértice ($x=0$ y $h = 0$) tendremos un mínimo de interferencia, y la distancia entre mínimos (o máximos), que denominamos *Interfranja* es, 
# 
# <div class="alert alert-block alert-info">
# 
# $$Int = \frac{\lambda}{2 n \tan(\alpha)} \sim  \frac{\lambda}{2 n \alpha} $$
# 
# </div>
# 
# Hay que hacer nota en que $n$ es el índice de la cuña. En el caso de estar formada por dos bloques de vidrio, la cuña estaría formada por aire, por lo que en ese caso $n = 1$
# 

# ----
# La siguiente celda de código genera una figura interactiva donde se puede ver el efecto en el diagrama interferencial de cambiar, tanto el índice de la lámina, como el ángulo $\alpha$ de la cuña. 
# 
# Como sugerencia, 
# 
# * Cambiar el valor de $n$ y $\alpha$ para ver como cambia la interfranja.
# 
# * Aparece un mínimo de luz en el vértice de la cuña. ¿Depende del valor de $\alpha$ o del valor de $n$?
# 
# * Aparte de modificar los valores de $n$ y $\alpha$ en la siguiente celda, demostrar, a partir de la condición de mínimo para el desfase total, que la diferencia de camino en **los minimos** de interferencias es igual a $m\lambda$ (a diferencia de lo que ocurría en el Experimento de Young, donde este valor de la diferencia de camino ocurría en los máximos de interferencia. Este cambio ocurre por la presencia del desfase de $\pi$ adicional debido a las reflexiones).

# In[1]:


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
    fig = plt.figure(figsize=(16,7))
    fig.tight_layout()
    x = np.linspace(0,D,400)
    y = np.linspace(0,D/2,20)
    X,Y = np.meshgrid(x,y)
    h = X*np.tan(alpha)
    deltag = 4*np.pi*n*h/Lambda
    deltatot = deltag + np.pi
    Itot = I1 + I2 + 2*np.sqrt(I1*I2)*np.cos(deltatot)
    plt.subplot(2,2,2)
    plt.pcolormesh(X,Y,Itot,cmap='gray',shading='auto')
    plt.title('Patrón de franjas',fontsize=16)
    plt.axis('off')
    plt.subplot(2,2,1)
    plt.hlines(0, 0, D,linewidth=2)
    plt.vlines(D,0,D*np.tan(alpha),linewidth=2,color='black')
    x = np.linspace(0,D,150)
    plt.plot(x,x*np.tan(alpha),color = 'black',linewidth=2)
    plt.title('Cuña',fontsize=16)
    plt.ylim(-1.5e-5,1e-5)
    plt.xlim(0,D)
    plt.annotate(r'$\alpha$',(D/3,0.000001),fontsize=18)
    plt.axis('off')
    plt.subplot(2,2,4)
    npointsinter = 14
    Int = Lambda/(2*n*alpha)
    N = int((D/Int)*npointsinter)
    x = np.linspace(0,D,N)
    h = x*np.tan(alpha)
    deltag = 4*np.pi*n*h/Lambda
    deltatot = deltag + np.pi
    Itotx = I1 + I2 + 2*np.sqrt(I1*I2)*np.cos(deltatot)
    plt.plot(x,Itotx,color = 'gray',linewidth=2)
    plt.text(D/3,-0.1,"Interfranja ="+ str(np.round(Int*1000,4))+' mm',fontsize=14)
    plt.title('Perfil de irradiancia',fontsize=16)
    plt.ylim(-0.2,0.2)
    plt.xlim(0,D)
    plt.axis('off')
    plt.show()
                     
                     
    
interactive_plot = widgets.interactive(fun, n=(1.05, 2.0),  alpha=(5e-4, 5e-3, 5e-4))
interactive_plot.children[1].readout_format='.4f'
output = interactive_plot.children[-1]
output.layout.height = '400px'

display(interactive_plot)   


# ### Efecto de una longitud de coherencia $l_c$ finita (fuente cuasimonocromática)
# 
# 
# Si la radiación que ilumina la cuña no es monocromática, y por tanto, posee una cierta anchura espectral $\Delta \lambda$, se define una longitud de coherencia 
# 
# 
# $$l_c = \frac{\lambda_0^2}{\Delta \lambda}$$
# 
# Esta longitud de coherencia fija una posición o distancia $x$ a partir de la cual no tendríamos interferencia y no veríamos máximos ni mínimos. En el caso de la cuña, la diferencia de camino en un punto cualquiera de la cuña es,
# 
# $$\Delta = 2 n h \simeq 2 n x \alpha$$
# 
# Por tanto, vemos que a medida que nos alejamos del vértice (aumentamos $x$) también aumenta $h$ y a su vez, aumenta la diferencia de camino óptico $\Delta$. Llegará un punto en el que $\Delta$ será igual al valor de la longitud de coherencia $l_c$ y entonces, a partir de ese punto, no veremos interferencias, y la irradiancia total reflejada será $I_{tot} = I_1 + I_2$.
# 
# El punto que separa la zona de interferencias de la zona en la que no se ven dichas interferencias cumple que, 
# 
# $$ \Delta = l_c  \Rightarrow  2 n x \alpha = l_c $$
# 
# $$ x \sim \frac{l_c}{2 n \alpha}$$.
# 
# 
# -----
# 
# Si se ejecuta la siguiente celda de código aparecerá una simulación para visualizar el efecto de aumentar la anchura espectral, o cambiar el valor de la longitud de onda central de iluminación cuando la radiación que incide en la cuña no es monocromática.
# 
# * ¿Comprueba qué parámetros cambian la interfranja y/o la extensión del diagrama interferencial?
# 
# * Con el valor de $lc$, ¿podrías calcular el valor de la altura correspondiente al borde donde acaba la zona de interferencia?

# In[2]:



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
    plt.text(D*1.05,D/2*1.05,'lc = '+str(np.round(lc*1e9,2))+' nm',fontsize=15)
    plt.axis('off')
    plt.show()
                     

    
interactive_plot2 = widgets.interactive(fun, Deltalambda=(20,100,2),Lambda=(400,600,20),  alpha=(5e-4, 5e-3, 5e-4))
interactive_plot2.children[2].readout_format='.4f'
output = interactive_plot2.children[-1]
output.layout.height = '600px'

display(interactive_plot2)   


# ## Vídeo lección virtual
# El siguiente vídeo muestra una explicación del tema de interferencias en láminas delgadas de espesor variable con forma de cuña
# 
# <video src="../_static/videos/LibroVirtual_LaminaEspesorVariable_cuña.mp4"></video>
