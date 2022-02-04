#!/usr/bin/env python
# coding: utf-8

# # Interferencia de dos ondas de luz

# ## Teoría
# 
# Cuando a una misma región del espacio llegan dos ondas de luz (ondas electromagnéticas) la onda resultante será la superposición (suma) de ambas. Antes de empezar recordamos algunas características particulares de este tipo de ondas.
# 
# * Las ondas electromagnéticas poseen **polarización**, es decir, la vibración ocurre en una dirección.
# 
# * Lo que se mide es la irradiancia de la onda. Esta magnitud es proporcional al cuadrado de la amplitud, y al variar periódicamente en el tiempo de forma muy rápida ($\sim$ 1-10 fs), lo que nosotros (nuestro ojo) o cualquier otro detector ve es un promedio temporal de dicha magnitud. Teniendo en cuenta que el promedio temporal del coseno al cuadrado es un medio: $< \sin^2(\omega t)> = <\cos^2(\omega t)> =  1/2$ tendremos
# 
# 
# $$ I = \epsilon_0 c n < \vec{E}^2>_{tiempo} =  \epsilon_0 c n E_0^2 < \cos^2(\vec{k} \vec{r} - \omega t + \phi) >  = \frac{1}{2} \epsilon_0 c n E_0^2   $$
# 
# 
# Vamos a describir a continuación la **interferencia de dos ondas electromagnéticas planas, polarizadas linealmente y monocromáticas**
# 
# Los campos eléctricos asociados a cada onda serán:
# 
# $$\vec{E_1}(\vec{r},t) = E_{01} \vec{e_{1}} \cos(\vec{k_1} \vec{r} - \omega t + \phi_1) $$
# $$\vec{E_2}(\vec{r},t) = E_{02} \vec{e_{2}} \cos(\vec{k_2}\vec{r} - \omega t + \phi_2) $$
# 
# donde $\vec{e_{j}}$ es un vector unitario indicando la dirección de vibración del campo y $\phi_j$ es un fase inicial del campo.
# 
# 
# El campo total será $\vec{E_T} = \vec{E_1} + \vec{E_2}$ , y por tanto la irradiancia total $I_T = \epsilon_0 c n <\vec{E_T}^2>$.
# 
# $$I_T = \epsilon_0 c n <(\vec{E_1} + \vec{E_2})^2> =  \epsilon_0 c n <\vec{E_1}^2> +  \epsilon_0 c n <\vec{E_2}^2> +  2 \epsilon_0 c n <\vec{E_1} \cdot \vec{E_2}>$$
# 
# En los anteriores términos, podemos reconocer las irradiancias de las dos ondas,
# 
# $$I_1 = \epsilon_0 c n <\vec{E_1}^2> = \frac{1}{2} \epsilon_0 c n E_{01}^2 $$
# $$I_2 = \epsilon_0 c n <\vec{E_2}^2> = \frac{1}{2} \epsilon_0 c n E_{02}^2 $$
# 
# mientras que el último término se conoce como **término de interferencia** y será el responsable de los nuevos fenómenos.
# 
# $$  2 \epsilon_0 c n <\vec{E_1} \cdot \vec{E_2}> =  2 \epsilon_0 c n  E_{01}E_{02} (\vec{e_{1}}\cdot\vec{e_{2}})  < \cos(\vec{k_1} \vec{r} - \omega t + \phi_1) \cos(\vec{k_2}\vec{r} - \omega t + \phi_2) >  $$
# 
# Como no sabemos calcular el promedio temporal del producto de dos cosenos usamos la siguiente relación trigonométrica $2\cos(A)\cos(B)=\cos(A+B)+\cos(A-B)$.
# 
# $$ 2 \epsilon_0 c n <\vec{E_1} \cdot \vec{E_2}> =  2 \epsilon_0 c n  E_{01}E_{02} (\vec{e_{1}}\cdot\vec{e_{2}}) \frac{1}{2}  < \cos(\vec{k_1} \vec{r} + \vec{k_2}\vec{r} - 2 \omega t + \phi_1 + \phi_2)  + \cos(\vec{k_1} \vec{r} - \vec{k_2}\vec{r}   + \phi_1 - \phi_2) > $$
# 
# El primer término del promedio temporal oscila rápidamente (a la frecuencia 2$\omega$) entre -1 y 1 y por tanto su promedio será nulo. El segundo término, que es el coseno de la resta de las fases de las dos ondas, no varía en el tiempo y por tanto su promedio temporal será él mismo. Hemos asumido que las fases iniciales de  los campos que interfieren no  varian en el tiempo, ya que esto impediría ver las interferencias. Esta característica se denomina *coherencia* y la veremos desarrollada más adelante en el curso. Por tanto, el término de interferencia queda de la siguiente forma:
# 
# 
# $$ 2 \epsilon_0 c n <\vec{E_1} \cdot \vec{E_2}> =  2 \epsilon_0 c n E_{01}E_{02} (\vec{e_{1}}\cdot\vec{e_{2}}) \frac{1}{2}  \cos[ (\vec{k_1} -  \vec{k_2}) \vec{r}   + \phi_1 - \phi_2]  $$
# 
# Por último podemos escribir el término de interferencia en función de las irradiancias de las ondas:
# 
# $$ 2 \epsilon_0 c n <\vec{E_1} \cdot \vec{E_2}> =  2 \sqrt{\frac{1}{2} \epsilon_0 c n E_{01}^2} \sqrt{\frac{1}{2} \epsilon_0 c n E_{02}^2} (\vec{e_{1}}\cdot\vec{e_{2}})  \cos[ (\vec{k_1} -  \vec{k_2}) \vec{r}   + \phi_1 - \phi_2]  =  2 \sqrt{I_1 I_2} (\vec{e_{1}}\cdot\vec{e_{2}})  \cos[ (\vec{k_1} -  \vec{k_2}) \vec{r}   + \phi_1 - \phi_2] $$
# 
# Así llegamos a la siguiente expresión general de la irradiancia total:
# 
# <div class="alert alert-success">
# $$I_T = I_1 + I_2 + 2 \sqrt{I_1 I_2} (\vec{e_{1}}\cdot\vec{e_{2}})  \cos(\delta)$$
# </div>
# 
# donde $\delta$ es la **diferencia de fase o desfase** (resta) entre las dos ondas que interfieren.
# 
# 
# 
# 
# De la anterior expresión podemos extraer varias conclusiones:
# 
# * El término de interferencia depende de las polarizaciones de las dos ondas a través del *producto escalar* $\vec{e_{1}}\cdot\vec{e_{2}}$. Es decir, **si las dos ondas se encuentran polarizadas perpendicularmente no interfieren**.
# 
# * El término de interferencia será positivo cuando el coseno sea positivo y por tanto la irradiancia total será mayor que las suma de las dos irradiancias. También podrá ser negativo cuando el coseno sea negativo y la irradiancia total será menor que la suma de las dos irradiancias. Por ello diremos que la interferencia puede ser **constructiva o destructiva**.
# 
# * El parámetro clave en el término de interferencia es el **desfase entre las ondas** $\delta$, que incorpora todos los desfases que hayan sufrido las ondas (por reflexión, etc) y sobre todo por haber recorrido distinto camino óptico. Es decir, para llegar a una región del espacio cada una de las dos ondas recorrerá un camino óptico diferente lo cuál provocará una diferencia de fase. Lo interesante es que esta **diferencia de camino óptico** cambiará al fijarnos en otro punto del espacio. Y al variar el defase cambiará el valor del término de interferencia y  por tanto el de la irradiancia total. Esto significa que espacialmente veremos una variación de la irradiancia provocada por la interferencia. En unas zonas del espacio veremos más irradiancia a cambio de tener menos en otras, siendo este el resultado fundamental de las interferencias, **la redistribución espacial de la energía**.

# ## Preguntas y cuestiones
# 
# Vamos a ver un ejemplo de la variación de la irradiancia total con el desfase entre las dos ondas. Para ello hay que ejecutar la siguiente celda de código. Pinchar sobre la celda de código y luego ejecutar con el botón Run del menú superior. En la parte superior de la celda se encuentran los parámetros que podéis cambiar, son las irradiancias de las dos ondas y el producto escalar de los vectores de polarización.

# In[1]:


#####################################################
# PUEDES CAMBIAR LOS VALORES DE LAS DOS IRRADIANCIAS
###################################################
I_1 = 1
I_2 = 1
e1e2 = 1
#################################
# NO TOCAR LO SIGUIENTE
###############################
from numpy import *
from matplotlib.pyplot import *
style.use('fivethirtyeight')
delta = arange(0,8*pi,0.1)
I_T = I_1 + I_2 + 2*e1e2*sqrt(I_1*I_2)*cos(delta)
#fig = plt.figure(figsize=(10,6))
plot(delta,I_T)
ylim(-0.1,4.1)
xlabel('$\delta$ (rad.)')
ylabel('I$_T$');


# Primero consideramos las dos irradiancias iguales a 1. Observando el resultado de la gráfica contestar a las siguientes cuestiones.
# 
# * Viendo la forma descrita por la irradiancia total decir qué valores del desfase provocan máxima irradiancia.
# 
# * Lo mismo que el caso anterior pero para la irradiancia mínima.
# 
# Ahora modificamos en el código el valor de la irradiancia de una de las dos ondas. Por ejemplo cambiar $I_1=0.1$. Observar el resultado y contestar. 
# 
# * ¿Cambian las posiciones en las que aparecen los máximos y los mínimos?
# 
# * ¿En qué cambia la figura?.
# 
# 
# Por último probamos a cambiar el ángulo formado por los vectores de polarización de las dos ondas, es decir e1e2. Las dos irradiancias las ponemos iguales a 1.
# 
# * ¿Cómo cambia la figura si las polarizaciones forman 60 grados, es decir e1e2=0.5?
# 
# * ¿Qué sucede si las polarizaciones son perpendiculares, es decir e1e2=0?.

# ## Otros recursos
# 
# El siguiente video de Kahn Academy explica de una manera sencilla la interferencia de dos ondas. Puedes ver el video dentro de la celda o pinchar en YouTube para abrir otra ventana del navegador.

# In[2]:


from IPython.display import HTML
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/H02ZBgrzkNU?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>')

