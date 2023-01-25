#!/usr/bin/env python
# coding: utf-8

# # Anillos de Newton

# In[1]:


from IPython.display import Image
Image(filename="ImagAnillosNewton.jpg")


# El patrón de interferencias que aparece al reflejarse la luz entre dos superficies transparentes, una curva y otra plana, es conocido como Anillos de Newton.
# 
# El patrón consiste en un conjunto de anillos centrados en el punto de contacto de las dos superficies. Se trata de **franjas de luz de igual espesor**, es decir, cada anillo representa la región en la cual el espesor que hay entre las dos superficies es el mismo. El espesor de la lámina que queda encerrada entre las dos superficies aumenta más rápidamente al alejarnos del centro (punto de contacto). Por ello los anillos más alejados del centro están más juntos.
# 
# Esta técnica se emplea para evaluar la calidad de superficies ópticas, veáse como ejemplo el siguiente artículo sobre caracterización de lentes oftálmicas.

# In[2]:


from IPython.display import Image
Image(filename="PaperAnillosNewton.JPG")


# ## Teoría

# Para estudiar los anillos de Newton analizamos las ondas reflejadas en la lámina de espesor variable (generalmente de aire) que se forma al depositar una lente plano-convexa sobre una superficie plana, tal y como se muestra en la siguiente figura. El radio de curvatura de la lente es $R$. Según nos alejamos del centro (punto de contacto) el espesor de la capa de aire aumenta. Nos quedamos a una distancia $x$ del centro. A esa distancia el espesor de la capa de aire es $e$. Si iluminamos el sistema desde arriba con una haz colimado de longitud de onda $\lambda$, la onda reflejada en la cara inferior de la lente plano-convexa y la onda reflejada en la cara superior de la superficie plana interfieren. Y lo hacen como si se tratara de una lámina delgada de espesor $e$. Considerando incidencias muy cercanas a la normal, la diferencia de camino entre esas dos ondas será:
# 
# $$ \Delta = 2 e$$
# 
# y por lo tanto el desfase 
# 
# $$ \delta = \frac{2 \pi}{\lambda} 2 e + \pi$$
# 
# donde hemos incluido un desfase de $\pi$ debido a las reflexiones, ya que una onda se refleja en la interfase vidrio-aire y la otra lo contrario (aire-vidrio).
# 
# El desfase entre las dos ondas depende del espesor de la capa de aire. Este espesor va aumentando al alejarnos del centro con lo cual la condición de interferencia irá igualmente variando, pasando por máximos ($\delta=2m\pi$) y mínimos ($\delta=(2m+1)\pi$) de luz. 
# 
# Justo en el centro o punto de contacto el espesor es nulo. Así que el desfase será $\pi$, el correspondiente a las reflexiones, y tendremos que las ondas interfieren destructivamente. Por eso en el punto de contacto se observará un mínimo de luz.

# In[3]:


from IPython.display import Image
Image(filename="esquemaAnillosNewton1.jpg")


# Vamos a calcular a que distancias del centro tenemos mínimos de luz, o lo que es lo mismo las posiciones de los anillos oscuros.
# Para ello vamos a expresar el espesor de la capa de aire $e$ en función de la distancia al centro $x$ y del radio de la lente $R$.
# Nos fijamos en la figura anterior en el triángulo rectángulo marcado con un patrón de rayas diagonales. La relación entre los lados del triángulo es:
# 
# $$ R^2 = x^2 + (R-e)^2 $$
# 
# Estamos considerando que la capa de aire es delgada y por tanto el espesor será mucho menor que el valor del radio de la lente $R$. Así podemos escribir $(R-e)^2 = R^2 + e^2 - 2 e R \simeq R^2 - 2 e R $, es decir, despreciar $e^2$. Por tanto nos queda
# 
# $$ R^2 = x^2 + R^2 - 2 e R $$
# 
# y despejando el espesor de la expresión anterior obtenemos 
# 
# $$ e =  \frac{x^2}{2R} $$
# 
# es decir, el espesor varía de forma parabólica con la distancia al centro. Además la variación del espesor es más apreciable cuando el radio de la lente es más pequeño. Es decir, el radio de la lente va a influir en como varía el espesor de la lámina de aire y por tanto en la distribución de luz resultante. 
# 
# Si empleamos el espesor anterior en el desfase entre las dos ondas obtenemos finalmente 
# 
# $$ \delta = \frac{2 \pi}{\lambda} 2 \frac{x^2}{2R}  + \pi $$

# ## Distribución de los anillos oscuros

# Ahora ya estamos en disposición de calcular las distancias al centro $x$ para obtener mínimos de luz $(\delta=(2m+1)\pi)$
# 
# $$ \frac{2 \pi}{\lambda} \frac{x^2}{R}  + \pi  = 2m\pi + \pi$$
# 
# Despejamos $x$ y obtenemos lo que llamamos los radios de los anillos oscuros
# 
# <div class="alert alert-block alert-success">
# 
# $$ x_m^2 = m \lambda R $$
#     
# </div>
# 
# Vemos que el cuadrado de los radios de los anillos oscuros es proporcional al radio de la lente. La distancia o separación entre anillos oscuros consecutivos no es fija, y por eso no se habla de la interfranja. En particular la distancia entre el anillo de orden $m$ y el $m+1$ es
# 
# $$ x_{m+1} - x_m = \sqrt{\lambda R} \left( \sqrt{m+1} - \sqrt{m} \right)$$
# 
# Con esta expresión podemos comprobar fácilmente que la distancia entre los anillos oscuros cerca del centro 
# $(x_2-x_1 \simeq 0.4 \sqrt{\lambda R} )$  es mayor que la distancia entre anillos oscuros lejos del centro 
# $(x_{12}-x_{11} \simeq 0.15 \sqrt{\lambda R} )$. Es decir, que los anillos se juntan al alejarnos del centro, tal y como ya habíamos explicado al inico de este documento.
# 
# Esta técnica interferométrica permite determinar el radio de curvatura de la lente $R$ midiendo los radios de los anillos oscuros $x_m$. Por ejemplo, con el radio del primer anillo  oscuro: $ R =  x_1^2 / \lambda$. La forma habitual consiste en representar gráficamente el radio al cuadrado de los anillos oscuros en función del orden o número del anillo ($m$). Mediante un ajuste lineal, la pendiente de la recta de ajuste nos permitirá obtener el valor del radio de la lente, $pendiente = \lambda R$. 

# ## Desplazamiento vertical de la lente

# En ocasiones sucede que el centro de la lente plano-convexa no está en contacto con la superficie plana debido a alguna imperfección, como por ejemplo partículas de polvo. Esto hace que la capa de aire encerrada entre las dos superficies sea mayor que en el caso analizado anteriormente. Ahora tendremos que añadir a la capa de aire anterior un espesor adicional que representa la distancia que se ha desplazado la lente de la superficie plana ($h$). La situación se representa en la siguiente figura.

# In[4]:


from IPython.display import Image
Image(filename="esquemaAnillosNewton2.jpg")


# Vemos en la figura que el espesor total de la lámina de aire será el espesor anterior $e=x^2 / (2 R)$ más el desplazamiento vertical $h$. Por lo tanto el desfase entre las dos ondas será: 
# 
# $$ \delta = \frac{2 \pi}{\lambda} 2 \left( \frac{x^2}{2R} + h \right) + \pi $$
# 
# Imponiendo de nuevo la condición de mínimo de luz (interferencias destructiva) $(\delta=(2m+1)\pi)$ y despejando $x$ obtenemos los radios de los anillos oscuros
# 
# $$ x_m^2 = m \lambda R - 2 h R $$
# 
# Fijándonos en una anillo concreto ($m$ fijo) vemos que su radio disminuye respecto de su posición original (cuando $h=0$) ya que el término nuevo que aparece con $h$ resta. Esto quiere decir que los anillos se desplazan desde su posición original (con $h=0$) hacia el centro, lo cual es normal ya que hemos aumentado el espesor total de la capa de aire y para seguir teniendo la misma diferencia de camino (y mismo desfase múltiplo impar de $\pi$) se tienen que mover hacia el interior.
# 
# Ahora si queremos determinar el radio de la lente $R$ tenemos que tener cuidado, no podremos coger el radio de un anillo oscuro ya que normalmente no sabremos cual es el valor del desplazamiento vertical de la lente $h$. Por ello nos vemos obligados a representar gráficamente los radios al cuadrado frente al número del anillo y obtener el radio de la pendiente de la recta de ajuste que sigue siendo igual que antes  $pendiente = \lambda R$.

# Ejecutar la siguiente celda de código para observar la distribución de luz correspodiente a los anillos de Newton

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
plt.style.use('bmh')
import ipywidgets as widgets
from IPython.display import display
plt.style.use('fivethirtyeight')

#Lambda = 5.5e-7;h0 = 0;R = 10.5
n = 1
I1 = 1; I2 = 1
x,y = np.mgrid[-100:100,-100:100]*5e-5
xcut = np.arange(-100*5e-5,100*5e-5,5e-5)
def anillos(h,R,Color):
    fig, ax = plt.subplots(1,2,figsize=(16,8))
    if(Color=='Azul (400nm)'):
        Lambda = 4e-7
        cmapchosen = 'Blues'
    elif(Color=='Verde (550 nm)'):
        Lambda = 5.5e-7
        cmapchosen = 'Greens'
    elif(Color=='Rojo (650 nm)'):
        Lambda = 6.5e-7
        cmapchosen = 'Reds'
   
    espesor = (x**2 + y**2)/(2*R) + h*1e-6
    delta = (2*np.pi/Lambda)*2*n*espesor + np.pi
    Itot = I1 + I2 + 2*np.sqrt(I1*I2)*np.cos(delta)
    #x = np.sqrt(m*Lambda*r - 2*h*r)
    ax[0].imshow(-Itot,cmap=cmapchosen)
    ax[1].plot(xcut*1e3,Itot[:,np.shape(Itot)[1]//2])
    ax[1].set_xlabel('Distancia al centro (mm)')
    ax[1].set_ylabel('Intensidad')
    #display(fig)
    return 

lambdawidgets = widgets.Dropdown(options=['Azul (400nm)','Verde (550 nm)','Rojo (650 nm)'])
lambdawidgets.height = 30
widgets.interact(anillos,h=(0,0.5,0.01),R=(5.0,15.0,0.5),Color=lambdawidgets)#widgets.fixed(5.5e-7))


# ## Cuestiones. Preguntas

# Emplear la celda de código anterior para analizar las siguientes cuestiones.
# 
# Lente en contacto con la superficie plana. Dejamos el parámetro $h$ a cero. Lámina de aire $n=1$.
# 
# * Para una longitud de onda fija (por ejemplo $\lambda$=550e-9 m) cambiamos el radio de la lente $R$ entre 5 y 15 metros y observamos cómo cambia la distribución de luz.
# 
# * Para un radio de curvatura de $R=8$ metros cambiamos la longitud de onda $\lambda$ y observamos cómo cambia la distribución de luz.
# 
# 
# Desplazamiento vertical de la lente. Ahora dejamos fijo $\lambda$=550e-9 m y $R=8$ m.
# 
#  * Cambia la separación entre la lente y la superficie plana a $h=0.2$ micras y observa cómo cambia la distribución de luz con respecto a $h=0$.
# 
# <span style="color:blue">Pregunta Reto.</span>
# Supongamos que el espacio entre las dos superficies se rellena de un líquido (sumergiendo el sistema) cuyo índice de refracción en el rango del visible es aproximadamente $n=1.5$. Deja el resto de parámetros fijos ($\lambda$=550e-9 m, $R=8$ m y $h=0$). Observa cómo cambia el patrón de interferencias al cambiar el índice de refracción.

# In[ ]:




