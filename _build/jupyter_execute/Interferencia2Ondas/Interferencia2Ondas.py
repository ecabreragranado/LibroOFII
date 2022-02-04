#!/usr/bin/env python
# coding: utf-8

# # Interferencia entre 2 ondas electromagnéticas

# ### Repaso de lo estudiado en cursos anteriores

# En cursos anteriores se ha tratado de responder a la pregunta: ¿Qué perturbación encontramos en un punto P si llegan a él dos ondas diferentes?
# 
# En particular, se ha estudiado el caso en el que las dos ondas son armónicas, del tipo:
# 
# $$y_1(x_1,t) = A \cos(k x_1 - \omega t + \phi_1) $$
# $$y_2(x_2,t) = A \cos(k x_2 - \omega t + \phi_2) $$
# 
# Donde se considera que las dos ondas poseen la misma amplitud para simplificar el resultado. 
# 
# El *principio de superposición* nos dice que la perturbación total es la suma de las perturbaciones
# provocadas por cada una de las ondas. Este principio es equivalente a decir que la ecuación de ondas
# es una ecuación lineal.
# 
# Así pues, si llamamos $y_t(x_p,t)$ a la perturbación total:
# 
# $$y_t(x,t) = A \cos(k x_1 - \omega t + \phi_1) + A \cos(k x_2 - \omega t + \phi_2)$$
# 
# Teniendo en cuenta que $\cos A + \cos B = 2 \cos(\frac{A+B}{2})\cos(\frac{A-B}{2})$, 
# 
# $$y_t(x_p,t) = 2 A \cos(k \frac{x_1 - x_2}{2} + \frac{\phi_1 - \phi_2}{2}) \cos(k \frac{x_1 + x_2}{2} - \omega t+ \frac{\phi_1 + \phi_2}{2})$$
# 
# Si definimos $\delta = k (x_1 - x_2) + \phi_1 - \phi_2$, el valor de esta variable determina la amplitud de
# la perturbación en el punto P. Este valor depende de la diferencia de caminos entre las dos ondas y del desfase inicial. Si
# $\delta = 2 m \pi$, con $m = 0, \pm 1, \pm 2...$ la amplitud total tomará el valor máximo $2 A$, mientras que si $\delta = 2(m+1) \pi$
# la amplitud será nula. 
# 
# Vemos que **la interferencia da lugar a una redistribución espacial de la energía**.

# ### Interferencia entre dos ondas electromagnéticas

# La interferencia anteriormente explicada es, por supuesto, válida para las ondas electromagnéticas. Sin embargo, en este caso hay que considerar algunas características particulares de este tipo de ondas que añaden nuevos efectos, 
# 
# * Las ondas electromagnéticas poseen **polarización**, es decir, tenemos que sumar vectores.
# 
# * Lo que medimos no es la amplitud de la onda sino la irradiancia. Esta magnitud, aparte de ser proporcional al cuadrado de la 
# amplitud, representa un promedio en un tiempo mucho mayor que el periodo de oscilación de los campos ($\sim$ 1-10 fs).
# 
# $$ I \propto < \vec{E}^2>_{\tau} = \frac{1}{\tau} \int_t^{t + \tau} \vec{E(t')}^2 dt' $$
# 
# $$ I = \epsilon_0 c n < \vec{E}^2>_{\tau} $$
# 
# * Debido a que lo que vemos es este promedio, la fase entre los campos que interfieren no puede variar en el tiempo si queremos ver
# la interferencia. Esta característica se denomina *coherencia* y la veremos desarrollada más adelante en el curso.
# 
# Vamos a describir a continuación la **interferencia de dos ondas electromagnéticas planas, polarizadas linealmente y monocromáticas**
# 
# Los campos eléctricos asociados a cada onda serán:
# 
# $$E_1(\vec{r},t) = \vec{E_{01}} cos(\vec{k_1} \vec{r} - \omega t + \phi_1) $$
# $$E_2(\vec{r},t) = \vec{E_{02}} cos(\vec{k_2}\vec{r} - \omega t + \phi_2) $$
# 
# El campo total será $\vec{E_t} = \vec{E_1} + \vec{E_2}$ , y la irradiancia total $I_t = \epsilon_0 c n <\vec{E_T}^2>$.
# 
# $$I_t = \epsilon_0 c n <(\vec{E_1} + \vec{E_2})^2> =  \epsilon_0 c n <\vec{E_1}^2> +  \epsilon_0 c n <\vec{E_1}^2> +  2 \epsilon_0 c n <\vec{E_1} \cdot \vec{E_2}>$$
# 
# En los anteriores términos, podemos reconocer,
# 
# $$I_1 = \epsilon_0 c n <\vec{E_1}^2>$$
# $$I_2 = \epsilon_0 c n <\vec{E_2}^2>$$
# 
# mientras que el último término se conoce como término de interferencia. Si multiplicamos escalarmente ambos campos y realizamos
# la integral que nos da el promedio en el tiempo, considerando que $<sen^2(\omega t)> = <cos^2(\omega t)> =  1/2$ y además que
# $<sen(\omega t)cos(\omega t)> =  0$, podemos llegar al siguiente resultado:
# 
# $$<\vec{E_1} \cdot \vec{E_2}> = \frac{1}{2}\vec{E_{01}} \cdot \vec{E_{02}} cos[(\vec{k_1} - \vec{k_2})\cdot \vec{r} + (\phi_1 - \phi2)] $$
# 
# En esta expresión se ha asumido además que las fases iniciales $\phi_{12}$ no dependen del tiempo.
# 
# De la anterior expresión podemos extraer varias características:
# 
# + El término de interferencia depende del *producto escalar* $\vec{E_{01}} \cdot \vec{E_{02}}$.
# Es decir, **si las dos ondas se encuentran polarizadas perpendicularmente no interfieren**. Este producto
# escalar puede escribirse también con los vectores unitarios en las direcciones de $\vec{E_{01}}$ y $\vec{E_{02}}$, 
# $\vec{E_{01}} \cdot \vec{E_{02}} = E_{01}E_{02}(\vec{e_{1}} \cdot \vec{e_{2}})$
# 
# + Depende del desfase relativo entre las dos ondas $\delta = (\vec{k_1} - \vec{k_2})\cdot \vec{r} + (\phi_1 - \phi2)$.
# 
# 
# Así pues, podemos concluir que,
# 
# $$I_t = I_1 + I_2 + 2 \sqrt{I_1 I_2}(\vec{e_{1}} \cdot \vec{e_{2}})cos(\delta)$$
# 
# En el caso en que $I_1 = I_2 = I_0$, $I_t = 2 I_0 ( 1 + cos(\delta)) = 4 I_0 cos^2(\frac{\delta}{2})$
# 
# Si definimos el contraste como, 
# 
# $$C = \frac{I_{max} - I_{min}}{I_{max} + I_{min}}$$
# 
# podemos reescribir la irradiancia total como, 
# 
# $$I_t = (I_1 + I_2)(1 + C cos(\delta))$$
# 
# Vamos a ver un ejemplo de la variación de la irradiancia total con el desfase entre las dos ondas.

# In[1]:


from numpy import *
from matplotlib.pyplot import *
style.use('fivethirtyeight')
delta = arange(0,6*pi,0.1)
## Cambia estos parametros
I_1 = 1
I_2 =  0.2
############
I_t = I_1 + I_2 + 2*sqrt(I_1*I_2)*cos(delta)
fig = plt.figure(figsize=(10,6))
plot(delta,I_t)
ylim(0,4)
xlabel(r'$\delta$')
ylabel(r'I$_t$');


# En el anterior código, 
# 
# * Cálcula el contraste de la interferencia.
# * Cambia los valores de $I_1$ y de $I_2$ y ejecuta la celda. ¿En qué cambia la figura?. ¿Cambia el contraste?
# * ¿Qué valores de $\delta$ observas que dan máxima $I_t$ y cuáles mínima?
# 

# Vemos que el desfase $\delta$ es el que determina el valor de la irradiancia total. Hay que tener presente que viene definido, para el caso que estamos estudiando, por la expresión,
# 
# $$ \delta = (\vec{k_1} - \vec{k_2})\cdot \vec{r} + (\phi_1 - \phi_2) $$
# 
# Vemos pues que, fijado el desfase inicial entre las dos ondas $\phi_1 - \phi_2$, $\delta$ depende únicamente del punto en donde estemos midiendo $I_t$ y de la diferencia entre los
# vectores de onda asociados a cada una de las dos ondas que interfieren.

# ### Otros recursos
# 
# Los siguientes videos de Kahn Academy explican de una manera sencilla la interferencia de 

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('https://youtu.be/H02ZBgrzkNU')


# In[3]:


from IPython.display import YouTubeVideo
YouTubeVideo('https://youtu.be/F5uuAQprw84')
YouTubeVideo('https://youtu.be/Y7peakctWdc')


# In[5]:


from IPython.display import HTML
HTML('<div style="position: relative; width: 300px; height: 232px;"><a href="http://phet.colorado.edu/sims/wave-interference/wave-interference_en.jnlp" style="text-decoration: none;"><img src="http://phet.colorado.edu/sims/wave-interference/wave-interference-screenshot.png" alt="Wave Interference" style="border: none;" width="300" height="232"/><div style="position: absolute; width: 200px; height: 80px; left: 50px; top: 76px; background-color: #FFF; opacity: 0.6; filter: alpha(opacity = 60);"></div><table style="position: absolute; width: 200px; height: 80px; left: 50px; top: 76px;"><tr><td style="text-align: center; color: #000; font-size: 24px; font-family: Arial,sans-serif;">Click to Run</td></tr></table></a></div>')


# In[ ]:




