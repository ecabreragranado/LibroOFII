#!/usr/bin/env python
# coding: utf-8

# # Franjas de igual espesor
# 
# <center>
# <img src="thinfilmsoap.gif" height=300px style="max-width:60%">
# </center>

# Hasta ahora hemos visto la interferencia entre las ondas reflejadas o transmitidas en una lamina planoparalela. En ella, llamando $h$ a su grosor, $n'$ a su indice de refraccion y $\theta'$ al angulo de refraccion en la primera cara, obtenemos que el desfase debido a la diferencia de camino entre ambas ondas (desfase geometrico $\delta_G$) es, 
# 
# $$\delta_G = \frac{4\pi}{\lambda} h n' \cos(\theta')$$
# 
# Si la lamina no tiene ambas caras paralelas y su grosor varia localmente, entonces puede ocurrir que diferentes rayos se solapen en algun punto cercano a la superficie (punto P en la figura). Para tratar este problema, consideraremos que ambas caras no se alejan mucho de ser paralelas entre si. En ese caso, el desfase geometrico entre las ondas que interfieren, podemos considerarlo efectivamente como, 
# 
# $$\delta_G = \frac{4\pi}{\lambda} h n' \overline{\cos(\theta')}$$
# 
# 
# <center>
#     
# ![imagenFizeau](imagenfizeau.png)
# 
# </center>
# donde ahora, $\bar{\cos(\theta')}$ es un promedio de esos valores de $\theta'$ para los rayos que llegan al punto P. Si este valor es constante (normalmente se observa en angulos cercanos a cero, es decir, normal a la superficie y por tanto $\bar{\cos(\theta')} \sim 1$) entonces, 
# 
# $$\delta_G = \frac{4\pi}{\lambda} h n'$$
# 
# es decir, el desfase, y por tanto si obtenemos maximo o minimo de interferencia, depende del espesor de la lamina. Es por eso que a este tipo de franjas se les denomina **franjas de igual espesor** (o *franjas de Fizeau*). Este tipo de franjas podemos verlas facilmente en la superfice de las pompas de jabon. 
# 
# Hay que notar que, si el tipo de interferencia (constructiva o destructiva) y por tanto que aparezcan maximos o minimos depende del grosor de la lámina en ese punto, el diagrama interferencial se convierte en este caso en un mapa de alturas o curvas de nivel, que nos indican cómo varía la altura de la lámina espacialmente.
# 
# 
# Nosotros vamos a centrarnos en dos casos de estudio: Una cu$\text{\~n}$a y una superficie curva en contacto con otra plana (Anillos de Newton)
# 
# 

# ## Interferencias en una cuña

# Una cuña esta constituida por dos superficies planas que forman un angulo $\alpha$ entre si. Consideraremos que este angulo es pequeño, por lo que podremos seguir utilizando, para el desfase geometrico entre las ondas que se reflejan en ambas caras de la lamina, la expresion:
# 
# $$\delta_G = \frac{4 \pi}{\lambda} h n$$
# 
# Para calcular el desfase total, tenemos que considerar, adicionalmente, el desfase debido a las reflexiones, que tenemos que analizar caso a caso. En lo que resta de este documento, consideraremos dos posibles casos, en los cuales, en ambos, tendremos que añadir un desfase adicional de $\pi$ rad ($\delta_R = \pi$ rad.)
# 
# Estos casos que vamos a considerar son los siguientes:
# 
# 
# 1. Cuña formada por dos bloques de vidrio que forman un cierto angulo $\alpha$. En este caso, las ondas que interfieren, en reflexion, son las reflejadas en la segunda cara del bloque superior de vidrio, y en la primera cara del bloque inferior de vidrio.
# 
# <center>
# 
# ![figura](wedgeglassblocks.png)
# 
# </center>
# 
# 2. Cuña formada por un material dielectrico de indice de refraccion $n'$ rodeada de aire.
# 
# 
# 
# Por ultimo, a la hora de encontrar las posiciones de los maximos y minimos tendremos que tener en cuenta la relacion entre la altura o grosor $h$ en un punto de la cuña, y su distancia al vertice $x$. Al ser simplemente una relacion lineal, tenemos que, 
# 
# $$h = x \tan(\alpha)$$
# 
# 
# ### Maximos y minimos de interferencia.
# 
# En ambos casos planteados, el desfase total entre las ondas que participan en la interferencia es, 
# 
# $$\delta_{tot} = \delta_G + \delta_R = \frac{4 \pi}{\lambda} h n' + \pi$$
# 
# Los maximos y minimos de interferencia se obtendran cuando:
# 
# * Maximos: $\delta_{tot} = 2 m \pi$ rad
# 
# * Minimos: $\delta_{tot} = (2 m + 1) \pi$ rad.
# 
# Centrandonos en los minimos, podemos buscar, en primer lugar, que grosores de la lamina nos dan minimos de interferencia:
# 
# <div class="alert alert-block alert-success">
# 
# $$\frac{4 \pi}{\lambda} h_{min} n + \pi = (2 m +1) \pi \Rightarrow h_{min} = \frac{m \lambda}{ 2 n}$$
# 
# </div>
# 
# Estas alturas se pueden pasar a distancias desde el vertice, teniendo en cuenta la relacion entre $x$ y $h$ expresada anteriormente, 
# 
# <div class="alert alert-block alert-success">
# 
# $$h_{min} = \frac{m \lambda}{ 2 n} \Rightarrow x_{min} = \frac{m \lambda}{2 n \tan(\alpha)} \sim  x_{min} = \frac{m \lambda}{2 n \alpha} $$
# 
# </div>
# 
# De la expresion anterior vemos que el diagrama interferencial se compone de maximos y minimos equiespaciados, de modo que, mirando a la cuña desde arriba, veriamos unas franjas de interferencia, donde en el vertice ($x=0$ y $h = 0$) tendremos un minimo de interferencia, y la distancia entre minimos(o maximos), que denominamos $Interfranja$ es, 
# 
# <div class="alert alert-block alert-info">
# 
# $$Int = \frac{\lambda}{2 n \tan(\alpha)} \sim  \frac{\lambda}{2 n \alpha} $$
# 
# </div>
# 
# Hay que hacer nota en que $n$ es el indice de la cuña. En el caso de estar formada por dos bloques de vidrio, la cuña en si estaria formada por aire, por lo que en ese caso $n = 1$
# 

# ----
# La siguiente celda genera una figura interactiva donde se puede ver el efecto en el diagrama interferencial de cambiar, tanto el indice de la lamina, como el angulo $\alpha$ de la cuña. 
# 
# Como sugerencia, 
# 
# * Cambiar el valor de $n$ y $\alpha$ para ver como cambia la interfranja.
# 
# * Aparece un minimo en el vertice de la cugna?. Depende del valor de $\alpha$ o del valor de $n$?
# 
# * Aparte de modificar los valores de $n$ y $\alpha$ en la siguiente celda, demostrar, a partir de la condicion de minimo para el desfase total, que la diferencia de camino en **los minimos** de interferencias es igual a $m\lambda$ (a diferencia de lo que ocurria en el Experimento de Young, donde este valor de la diferencia de camino ocurria en los maximos de interferencia. Este cambio ocurre por la presencia del desfase de $\pi$ adicional debido a las reflexiones).

# In[1]:


get_ipython().run_line_magic('run', 'codefigurafizeau.py')


# ### Efecto de una longitud de coherencia $l_c$ finita (fuente cuasimonocromatica)
# 
# 
# Si la radiacion que ilumina la cuña no es monocromatica, y por tanto, posee una cierta anchura espectral $\Delta \lambda$, se define una longitud de coherencia 
# 
# 
# $$l_c = \frac{\lambda_0^2}{\Delta \lambda}$$
# 
# Esta longitud de coherencia fija una diferencia de camino optico $\Delta_{max} = l_c$ a partir de la cual no tendriamos interferencia y no veriamos maximos y minimos. En el caso de la cuña, la diferencia de camino en un punto cualquiera de la cuña es, 
# 
# $$\Delta = 2 n h = 2 n x \tan(\alpha)$$
# 
# 
# Por tanto, vemos que a medida que nos alejamos del vertice (aumentamos $x$) tambien aumenta $h$ y a su vez, aumenta $\Delta$. Llegara un punto en el que $\Delta$ sea igual al valor que tenga $l_c$ y entonces, a partir de ese punto, no veremos interferencias, y la irradiancia total reflejada sera $I_{tot} = I_1 + I_2$.
# 
# El punto que separa la zona de interferencias de la zona en la que no se ven dichas interferencias cumple que, 
# 
# $$\Delta_{lim} = 2 h_{lim} n = 2 n x_{lim} \tan(\alpha) = l_c$$
# 
# $$ x_{lim} \sim \frac{l_c}{2 n \alpha}$$.
# 
# 
# 
# -----
# 
# Si se ejecuta la siguiente celda, aparecera una simulacion para visualizar el efecto de aumentar la anchura espectral, o cambiar el valor de la longitud de onda central de iluminacion cuando la radiacion que incide en la cugna no es monocromatica.
# 
# * Por que al cambiar algunos parametros cambia el valor de la interfranja y otros no?
# 
# * Por que al cambiar el valor de $\alpha$ cambia la extension del patron de interferencia?
# 
# * Con el valor de $lc$, podrias calcular el valor de la altura correspondiente al borde de la zona de interferencia?

# In[2]:


get_ipython().run_line_magic('run', 'codefigurafizeau2.py')


# In[ ]:




