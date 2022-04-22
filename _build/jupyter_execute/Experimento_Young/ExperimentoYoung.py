#!/usr/bin/env python
# coding: utf-8

# # Experimento de Young

# In[1]:


from IPython.display import Image
Image(filename="YoungTwoSlitExperiment.JPG")


#     ''The experiments I am about to relate ... may be repeated with great ease, 
#     whenever the sun shines, and without any other apparatus than is at hand to everyone [1]''
#     
# Así comenzó Thomas Young su famoso experimento el 24 de noviembre de 1803 en la Real Sociedad de Londres. Ante una audencia mayoritariamente defensora de la teoría corpuscular de la luz (apoyada por Isaac Newton), Thomas Young llevó a cabo el primer experimento de interferencias de luz, demostrando la naturaleza ondulatoria de la luz. Dejó pasar un rayo de sol por un pequeño orificio de la ventana de la habitación e hizo incidir el haz de luz sobre el canto de una tarjeta diviendo el haz en dos. Estos dos haces al solaparse en una pantalla generaban unas franjas oscuras y brillantes de luz.
# 
# [1] Thomas Young, "Experimental Demonstration of the General Law of the Interference of Light", Philosophical Transactions of the Royal Society of London vol. 94 (1804). 

# ## Teoría
# 
# Normalmente el experimento de Young se representa con una doble rendija, tal y como aparece en la figura anterior. Una onda esférica (o bien una onda plana, el tratamiento es equivalente), incide en una pantalla sobre la cual se han realizado dos aperturas $S_1$ y $S_2$ muy próximas entre sí (llamaremos a la distancia entre ellas $a$). Estas aperturas actúan como dos fuentes secundarias de radiación, generando a su vez dos ondas esféricas que se superponen en el espacio que hay detrás de ellas. Si observamos la distribución de irradiancia en una pantalla situada a una cierta distancia $D$, ¿qué nos encontraremos?.
# 
# Las dos ondas que se generan en $S_1$ y $S_2$ pueden escribirse como:
# 
# $$\vec{E_1} = \vec{e_1} \; E_{01} \;  \; \cos\left( k r_1 - \omega t + \phi_1\right)$$
# $$\vec{E_2} = \vec{e_2} \; E_{02} \;  \; \cos\left( k r_2 - \omega t + \phi_2\right)$$
# 
# $E_{0j}$  es la amplitud de la onda, $\vec{e_j}$  es la dirección de vibración y $\phi_j$ es la fase inicial.  $r_1$ ($r_2$) es el camino que recorre la onda desde $S_1$ ($S_2$) hasta el punto de observación P. Ambas ondas tienen la misma longitud de onda.
# 
# La superposición de estas dos ondas, nos dará la expresión de la irradiancia ya conocida, 
# 
# $$I_T = I_1 + I_2 + 2 \sqrt{I_1 I_2} \; (\vec{e_ 1}\cdot\vec{e_ 2}) \; cos(\delta)$$
# 
# donde $\delta = k (r_2 - r_1) + \phi_2 - \phi_1$ es el desfase (o la diferencia de fase) entre las dos ondas.
# 
# En esta expresión podemos hacer alguna que otra simplificación, 
# 
# * $\vec{e_ 1} \cdot \vec{e_ 2}=1$ porque las ondas las consideramos polarizadas linealmente en la misma dirección.
# * $I_1 = I_2$ en caso de que no haya ningún filtro en $S_1$ ó $S_2$, las dos ondas tienen la misma amplitud.
# * $\phi_2 - \phi_1 = 0$ ya que el frente de ondas llega simultáneamente a $S_1$ y $S_2$. Nótese que si colocásemos por ejemplo una pieza de un material transparente antes de una de las dos aperturas, tendríamos un desfase adicional en una de las dos ondas y esta diferencia ya no sería nula. Esto ocurriría porque una de las ondas viajaría a través del material mientras la otra onda lo haría en aire. 
# 
# Así la irradiancia total queda
# 
# $$I_T = 2 I_1 \left( 1 + cos(\delta) \; \right)$$
# 
# con $\delta = k (r_2 - r_1)$
# 
# Como vemos, **es la diferencia de caminos $\Delta = r_2 - r_1$ la que determina el valor de la irradiancia final en el punto P**. Vamos a calcularla.

# In[2]:


from IPython.display import Image
Image(filename="ExperimentoYoung.jpg")


# Según la figura, $\Delta = r_2 - r_1$ lo podemos escribir como $\Delta = a sen(\theta)$, siendo $a$ la separación entre las rendijas. Si éste ángulo es pequeño (lo que significa que la distancia entre las fuentes y la pantalla de observación sea grande comparada con la separación entre las fuentes, $D \gg a$), esta expresión la podemos simplificar, 
# 
# $$ \Delta = a \; sen(\theta) \simeq a \; tan(\theta) = a \frac{x}{D}$$.
# 
# Y por tanto, 
# 
# $$\delta = k \frac{a x }{D} = \frac{2 \pi a x}{\lambda D}$$
# 
# En estas expresiones, $x$ es la distancia del punto P de observación al eje mientras que $D$ es la distancia entre el plano
# que contiene a las fuentes y la pantalla de observación, donde se encuentra P. Podemos reescribir la irradiancia total en la pantalla empleando la expresión calculada del desfase 
# 
# <div class="alert alert-success">
# $$I_T = 2 I_1 \left( 1 + cos\left( \frac{2 \pi a x}{\lambda D} \right) \; \right)$$
# </div>

# ## Distribución de luz. Patrón de interferencias
# 
# Ahora estamos en disposición de contestar a la pregunta que nos planteábamos antes, ¿cómo es la distribución de irradiancia en la pantalla de observación?. Vemos que el desfase depende de la altura en la pantalla $x$, por tanto al movernos en esa dirección el valor de la irradiancia cambiará. En particular el término que provoca esa variación es del tipo cosenoidal $cos( \frac{2 \pi a x}{\lambda D})$ por lo que veremos en la pantalla una distribución cosenoidal, con máximos de irradiancia cuando $\delta = 2 m \pi$, con $m = 0, \pm 1, \pm 2 ...$ y mínimos de irradiancia cuando $\delta = (2 m + 1) \pi$, con $m = 0, \pm 1, \pm 2 ...$. Las posiciones $x$ a las que corresponden estas condiciones serán, 
# 
# Máximos de irradiancia.  $\delta = 2 m \pi rad \implies \Delta = m \lambda \implies$
# $$x^{max}_m = \frac{m \lambda D}{a}$$
# 
# Mínimos de irradiancia.  $\delta = (2 m + 1)\pi \implies \Delta = \frac{(2m +1) \lambda}{2} \implies$
# $$x^{min}_m = \frac{(2m + 1) \lambda D}{2a}$$
# 
# Vamos a dibujar la distribución de irradiancia en la pantalla y un corte a lo largo del eje X (ejecutar la siguiente celda de código).

# In[3]:


###################################################################################
# PARÁMETROS. SE PUEDEN MODIFICAR SUS VALORES
###################################################################################
Lambda = 700e-9 # en metros, longitud de onda de la radiación
D = 14.5  # en metros, distancia entre el plano que contiene las fuentes y la pantalla de observación
a = 0.01 # en metros, separación entre fuentes de Young
I1 = 0.1 # Consideramos irradiancias normalizadas a un cierto valor.
I2 = 1
###################################################################################

from matplotlib.pyplot import *
from numpy import *
get_ipython().run_line_magic('matplotlib', 'inline')
style.use('fivethirtyeight')

interfranja=Lambda*D/a # cálculo de la interfranja
k = 2.0*pi/Lambda
x = linspace(-5*interfranja,5*interfranja,500)
X,Y = meshgrid(x,x)
delta = k*a*X/D
Itotal = I1 + I2 + 2.0*sqrt(I1*I2)*cos(delta)
figure(figsize=(14,5))
subplot(121)
pcolormesh(x*1e3,x*1e3,Itotal,cmap = 'gray',vmin=0,vmax=4)
xlabel("x (mm)"); ylabel("y (mm)")
subplot(122)
plot(x*1e3,Itotal[int(x.shape[0]/2),:])
xlabel("x (mm)"); ylabel("Irradiancia total normalizada")


# Como podemos ver, los máximos están equiespaciados (lo mismo sucede con los míminos), siendo la distancia entre dos máximos consecutivos
# $$ \text{Interfranja} = \frac{\lambda D}{a} $$
# Dicha magnitud se conoce con el nombre de interfranja y nos da información sobre el tamaño característico del patrón de franjas. 
# Además del tamaño, para poder observar con claridad las franjas es necesario que estén bien contrastadas. Para ello se define el contraste o visibilidad de las franjas
# $$ C = \frac{I_T^{max}-I_T^{min}}{I_T^{max}+I_T^{min}}$$
# que nos dice cuanto están separados los máximos de luz respecto de los mínimos. 
# 
# El valor de estas dos magnitudes para el caso representado en la figura anterior se muestra en la siguiente celda (ejecutar dicha celda después de haber ejecutado la anterior celda de código)

# In[4]:


interfranja=Lambda*D/a # cálculo de la interfranja
C = (Itotal.max() - Itotal.min())/(Itotal.max() + Itotal.min()) # cálculo del contraste
print ("a=",a*1e3,"mm   ","D=",D,"m   ","Longitud de onda=",Lambda*1e9,"nm") # valores de los parámetros
print ("Interfranja=",interfranja*1e3,"mm") # muestra el valor de la interfranja en mm
print ('Contraste=',C) # muestra el valor del contraste


# ## Preguntas y Cuestiones
# 
# Emplear las dos celdas de código anteriores para analizar las siguientes cuestiones. 
# 
# * Prueba a cambiar el valor de los parámetros $\lambda$, $D$ y $a$ (de uno en uno) y observa cómo cambia la distribución de luz. Observa como se modifica el valor de la interfranja y del contraste.
# 
# * Disminuye el valor de $I_1$ o $I_2$ y observa cómo cambia el patrón de interferencias. ¿Cómo cambia el valor de la interfranja y del contraste?

# ### ¿Qué diferencia habría si en vez de iluminar con luz monocromática iluminamos con luz blanca?
# 
# Podemos verlo en la siguiente imagen

# In[5]:


from IPython.display import Image
Image(filename="FranjasYoungWhiteLight.jpg")


# Como se puede observar, en el caso de luz blanca, cada una de las longitudes de onda que la componen forma un sistema de franjas con los máximos situados en posiciones distintas y con una interfranja diferente. Esto dificulta enormemente la visualización de la interferencia y nos llevará a definir el concepto de luz coherente e incoherente.

# ## Otros recursos
# 
# Los siguientes videos de Kahn Academy explican de una manera sencilla la interfere
# ncia de las ondas en el experimento de Young. Puedes ver el video dentro de la celda o pinchar en YouTube para abrir otra ventana del navegador

# In[6]:


from IPython.display import HTML
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/F5uuAQprw84?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>')


# In[7]:


from IPython.display import HTML
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/Y7peakctWdc?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>')


# In[ ]:




