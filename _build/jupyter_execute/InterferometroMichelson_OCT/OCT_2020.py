#!/usr/bin/env python
# coding: utf-8

# # Tomografía de coherencia óptica. Puntos básicos.

# *La tomografía de coherencia óptica (TCO) es una técnica de imagen tomográfica óptica, no invasiva e interferométrica, que ofrece una penetración de milímetros (aproximadamente 2-3 mm en el tejido o material de que se trate) con resolución axial y lateral de escala micrométrica. La técnica fue demostrada por primera vez en 1991 con una resolución axial de ~30µm. En 2001 la TCO alcanzó una resolución submicrométrica debido a la introducción de fuentes de luz de banda amplia (fuentes que emiten longitudes de onda sobre un rango de ~100 nm). Ahora la TCO es una técnica de imagen ampliamente aceptada, especialmente en oftalmología, otras aplicaciones biomédicas, y la conservación de obras de arte.*
# 
# Esta es la definición que [aparece en la Wikipedia](https://es.wikipedia.org/wiki/Tomograf%C3%ADa_de_coherencia_%C3%B3ptica), pero ¿en qué consiste?. ¿Y en qué se relaciona con lo estudiado durante el curso hasta ahora?

# ### Interferencia de baja coherencia

# Cuando hemos estudiado la interferencia entre dos haces, hemos hecho hincapié en que para que poder visualizarla la diferencia de camino $\Delta$ entre los dos haces que interfieren, ha de ser menor que la longitud de coherencia $l_c$ de la radiación. En caso contrario, el desfase relativo entre las dos ondas varía aleatoriamente y el promedio temporal en el tiempo de observación es nulo. Hasta ahora hemos visto una longitud de coherencia pequeña como un factor limitante en experimentos de interferometría. Sin embargo, puede ser un elemento que podemos utilizar para alcanzar una gran resolución en nuestras medidas.
# 
# Antes de ver la interferencia de baja coherencia primeramente hay que recordar la relación entre la longitud de coherencia y la anchura espectral de la fuente. Pulsos de luz muy anchos espectralmente poseen una longitud de coherencia pequeña, mientras que el caso límite de radiación monocromática tendría una longitud de coherencia infinita. En particular, la relación entre ambas magnitudes es la siguiente:
# 
# $$ l_c = \frac{\lambda^2 }{\Delta \lambda}$$
# 
# Se observa así que cuando hablamos de interferencia con radiación de baja coherencia, hablamos igualmente de interferencia con fuentes de espectro ancho, como pueden ser diodos superluminiscentes o pulsos láser de fs.
# 
# 
# En la interferometría de baja coherencia, efectivamente la luz utilizada posee una longitud de coherencia pequeña, del orden de micras o incluso menor. Esto tiene como consecuencia que si construimos un interferómetro utilizando esta radiación, la diferencia de camino entre los haces que interfieren ha de ser como máximo de ese orden para observar dicha interferencia. O dicho de otro modo, cuando obtenemos interferencia sabemos que la diferencia de camino entre los dos haces es del orden de micras o menor. Por tanto, podemos utilizar este método para medir de forma muy precisa distancias.
# 
# 
# Además, utilizando radiación en la región del infrarrojo ($\sim 800$ nm) la longitud de penetración en los medios biológicos es del orden de mm. En concreto, en el caso del ojo se consigue penetrar hasta la retina ya que esta radiación no es absorbida por el agua presente en la córnea y en los humores acuoso y vítreo.

# ### ¿En qué consiste?

# El principio y montaje para la tomografía de coherencia óptica se puede observar en la siguiente figura (el texto se encuentra en francés, pero creo que se entiende bien)

# In[1]:


from IPython.display import Image
Image("Principe_OCT.png")


# Como se observa en la figura, la radiación con una longitud de coherencia baja (ancho espectro) ilumina un interferómetro de Michelson, en donde en uno de sus brazos colocamos la muestra (o el ojo) y en el otro un espejo móvil. Las diferencias de camino entre el haz reflejado en el espejo y cada uno de los haces reflejados en las superficies de la muestra serán:
# 
# $$\Delta_1 = 2 z -  2 H$$
# 
# $$\Delta_2 = 2 z -  2 (H+ n L_1)$$
# 
# $$\Delta_3 = 2 z -  2 (H + n L_2)$$
# 
# donde se ha supuesto que $z$ es la distancia entre el espejo móvil y el divisor de haz, $H$ la distancia entre la primera superficie de la muestra y el divisor, $n$ el índice de refracción dentro de la muestra, y $L_{1,2}$ las distancias de las superficies maś alejadas de la muestra con respecto a la primera.
# 
# El movimiento de este espejo permitirá igualar los caminos ópticos de los haces reflejados en el espejo móvil y en cada una de las superficies de las que consta la muestra. La irradiancia medida por el detector en función del desplazamiento del espejo se puede apreciar en la figura superior derecha. Se puede observar que aparecen, en el ejemplo mostrado, 3 zonas de interferencia, con máximos y mínimos, correspondientes a cada una de las 3 superficies de las que consta la muestra. La altura de cada zona depende de la reflectancia de esa superficie mientras que la anchura es proporcional a la longitud de coherencia de la fuente.
# 
# Si pensamos en que movemos el espejo desde una zona cercana al divisor de haz del interferómetro, veríamos primero que al mover el espejo la irradiancia se mantiene constante. Esto es debido a que el camino óptico recorrido por el haz reflejado en el espejo es muy diferente a los caminos ópticos de los haces reflejados por cualquiera de las 3 superficies de la muestra, y por tanto no vemos interferencia ($I_{total} = I_1 + I_2$). 
# 
# Al seguir moviendo el espejo, llegará un punto en el que la diferencia de camino entre el haz reflejado en el espejo y el haz reflejado por la primera superficie de la muestra sea menor que $l_c$. Entonces veremos interferencia y la irradiancia detectada oscilará entre unos valores máximos y mínimos a medida que movemos el espejo. 
# 
# Si continuamos moviendo el espejo alejándonos del divisor de haz, nos saldremos de la zona en la que la diferencia de camino entre el haz reflejado en el espejo y el haz reflejado por la primera superficie de la muestra es menor que $l_c$, volviendo a una irradiancia constante. Un posterior movimiento del espejo provocará que se cumpla esta condición (diferencia de camino menor que $l_c$) pero entre el haz reflejado por el espejo y el reflejado por la segunda superficie. Entonces veremos la segunda zona de interferencia en la señal captada por el detector. Lo mismo ocurrirá con la tercera superficie.
# 
# 
# Segun el esquema que hemos visto por cada superficie en uno de los brazos del interferometro, tendremos una zona de interferencia con maximos y minimos registrada por el detector. **La extension de esta zona de interferencias sera igual al doble de la longitud de coherencia**. Si esta longitud de coherencia tiene un valor muy bajo (el laser de Ti:Al2O3 tiene una longitud de coherencia del orden de 2 $\mu$m.) esta zona sera muy estrecha.
# 
# 

# ----
# 
# Veamos un ejemplo numérico en donde definimos dos trenes de pulsos con una diferencia de camino que depende de su posición

# ### Figura para visualizar la interferencia en OCT

# El siguiente codigo muestra 3 figuras que nos permiten ver la inteferencia registrada por un detector en un montaje de OCT, colocando una lamina (2 superficies) en uno de los brazos del interferometro. 
# 
# 
# 
# Las 3 figuras muestran los siguientes aspectos de la interferencia:
# 
# 1. La figura de la izquierda permite ver el solapamiento temporal entre el pulso reflejado en el espejo de referencia movil (azul) con los dos haces reflejados en ambas caras de la lamina (en rojo), cuando movemos el espejo desplazando el valor de $z$. Cada valor de $z$ es un punto en las figuras central y lateral derecha. Cuando se solapan temporalmente los pulsos que llegan al detector, tenemos interferencia. Cuando no, la irradiancia es simplemente la suma de las 3 irradiancias de los pulsos que viajan por el interferometro (pulso reflejado por espejo movil, pulso reflejado por la primera cara de la lamina, y pulso reflejado por la segunda cara de la lamina).
# 
# 2. La figura central muestra lo que obtendriamos si desplazamos el espejo movil distintas distancias $z$, y registramos la irradiancia captada por el detector en cada punto. Se observan dos zonas de interferencia cuando la posicion del espejo movil provoca que la diferencia de camino entre los pulsos sea menor que la longitud de coherencia.
# 
# 3. La figura lateral derecha muestra una ampliacion de la primera zona de interferencia. Se puede estimar la anchura total de esta zona (relacionada con la longitud de coherencia del pulso) y la interfranja (relacionada con la longitud de onda de la radiacion).

# In[2]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')

get_ipython().run_line_magic('matplotlib', 'inline')
from scipy.interpolate import interp1d
import ipywidgets as widg

num_pulsos = 2
c0 = 3e8
twidth = 2e-14
t = np.linspace(0,twidth*25,15000)
t01 = np.linspace(2,5,num_pulsos)*4*twidth
A01 = np.linspace(10,4,num_pulsos)
t02 = [8*twidth]
Lambda = 9.5e-7
wpulse = 2*np.pi*c0/Lambda
k = 2.0*np.pi/Lambda

z = 3.2*Lambda #lo que se mueve un espejo. Luego, en tren2, vendrá multiplicado por 2
tren1 = np.sum(np.asarray([A01[i]*np.exp(-((t-t01[i])/twidth)**2)*np.exp(1.0j*(-wpulse*t)) 
                           for i in range(len(t01))]),axis=0)
zshow = np.linspace(0,c0*twidth*10,900)

int_array = np.zeros(np.shape(zshow))
dt = t[1]-t[0]
t_int = t[-1]
#i1 =  0.5*(np.sum(np.real(tren1)**2)*dt/t_int + np.sum(np.real(tren2)**2)*dt/t_int)
#print(i1*2) # i1 + i2
for i,zz in enumerate(zshow):
    tren2 = np.sum(np.asarray([np.exp(-((t-(t00 + 2*zz/c0 - twidth*4.5))/twidth)**2)*np.exp(1.0j*(k*2*zz-wpulse*t))
                               for t00 in t02]),axis=0)
    #Interferencia
    etotal = tren1+tren2
    int_array[i] = np.sum(np.real(etotal)**2)*dt/t_int
fun_int = interp1d(zshow,int_array)

def oct(z,zshow,int_array,tren1,fun_int):
    z=z*1e-6
    tren2 = np.sum(np.asarray([A01[0]*np.exp(-((t-(t00 + 2*z/c0 - twidth*4.5))/twidth)**2)*np.exp(1.0j*(k*2*z-wpulse*t))
                           for t00 in t02]),axis=0)
    fig, ax = plt.subplots(1,3,figsize=(23,6))
    ax[0].plot(t*1e15,np.real(tren1),t*1e15,np.real(tren2))
    ax[0].set_title('Solapamiento temporal pulsos')
    ax[0].set_xlabel('t (fs)')
    ax[0].set_ylabel('E (u.a)')
    ax[1].plot(zshow*1e6,int_array)
    ax[1].set_title('Irradiancia en funcion de la posicion del espejo')
    ax[1].set_xlabel(r'z ($\mu$m)')
    ax[1].set_ylabel('I (u.a)')
    ax[2].plot(z*1e6,fun_int(z),'go',alpha=0.5)
    ax[2].plot(zshow*1e6,int_array)
    ax[2].set_xlim(5,23)
    ax[2].set_title('Zoom Primera Zona de interferencia')
    ax[2].set_xlabel(r'z ($\mu$m)')
    ax[2].set_ylabel('I (u.a)')
               

widg.interact(oct,z=(0,60,1),zshow=widg.fixed(zshow),int_array=widg.fixed(int_array),tren1=widg.fixed(tren1),fun_int=widg.fixed(fun_int))


# **De la figura**
# 
# * Relacionar la interfranja con la longitud de onda: Recordar que en el interferometro de Michelson lo que tenemos que desplazar un espejo $\Delta z$ para pasar de un maximo al siguiente es $\lambda/2$. Esta sera la interfranja que aparece en las figuras central y lateral derecha. Estimar la longitud de onda de la radiacion que ilumina el interferometro y comprobar que es igual a 950 nm (realizar esta estimacion de forma aproximada).
# 
# * Relacionar anchura de la zona de interferencia con l$_c$. Estimar por tanto la longitud de coherencia de la radiacion anterior y comprobar que es del orden de 6 $\mu$m.
# 
# * Relacionar valor cte con I1 + I2
# 
# * ¿Por qué la segunda zona tiene un valor menor? 

# ### Podemos utilizar este montaje para medir espesores pequegnos
# 
# 
# Segun hemos visto, cada cara de una lamina nos da una zona de interferencia distinta. Podemos medir por tanto el espesor de la lamina, midiendo cuanto hemos tenido que desplazar el espejo movil de un centro de la primera zona de interferencia al centro de la segunda zona de interferencia.
# 
# Efectivamente, tengamos una lamina de espesor $L$ e indice de refraccion $n$ en uno de los brazos del interferometro, mientras que en el otro brazo disponemos de un espejo movil, cuya distancia al divisor del haz llamamos $z$. Ademas, llamamos $H$ a la distancia entre el divisor de haz y la primera cara de la lamina. 
# 
# 
# <center>
# <img src=michelsonfiguretikzOCT.jpg width=600px></img>
# </center>
# 
# En el centro de la primera zona de interferencia se cumple que $\Delta_{12} = 0$, donde llamamos $\Delta_{12}$ a la diferencia de camino entre el haz que se refleja en el espejo movil (haz $1$), y el haz reflejado en la primera cara de la lamina (haz $2$). En ese punto, estos haces se solapan por completo, y ademas, tenemos un maximo de interferencia. Por otro lado, en el centro de la segunda zona de interferencia, $\Delta_{13} = 0$, donde $\Delta_{13}$ es ahora la diferencia de camino entre el haz que se refleja en el espejo movil (haz $1$) y el que se refleja en la segunda cara de la lamina (haz $3$).
# 
# Por tanto, en el centro de la primera zona de interferencia se cumple que, 
# 
# $$\Delta_{12} = 0 \Rightarrow 2 (z_1 - H) = 0 \Rightarrow z_1 = H$$
# 
# $$\Delta_{13} = 0 \Rightarrow 2 (z_2 - (H + n L)) = 0 \Rightarrow z_2 = H + n L$$
# 
# De este modo, $z_2 -z_1 =  n L$. Sabiendo el indice de refraccion del material que forma la lamina, y la distancia entre los centros de las zonas de interferencia $z_2 - z_1$, podemos despejar $L$.

# In[ ]:




