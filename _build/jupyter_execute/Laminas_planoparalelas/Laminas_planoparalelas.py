#!/usr/bin/env python
# coding: utf-8

# # Interferencia en láminas planoparalelas. Franjas de igual inclinación
# 
# Una de las formas habituales de obtener interferencias es mediante la división del frente de ondas de un haz procedente de una fuente para posteriormente recombinar ambas partes. A este tipo de interferómetros se les conoce como **interferómetros por división del frente de ondas** y ejemplos de ellos pueden ser el interferómetro de la doble rendija o el biprisma de Fresnel. Otra estrategia para disponer de dos ondas que guarden una relación de fase constante en el tiempo entre ellas y por tanto den lugar a interferencia, es utilizar la reflexión y transmisión parcial en una superficie o espejo para producir estas dos ondas. A este tipo de interferómetros se les denomina **interferómetros por división de amplitud**. El ejemplo quizás más sencillo lo podemos encontrar en una lamina planoparalela (lámina con caras paralelas y por tanto espesor fijo).
# 
# Efectivamente, si iluminamos una lámina planoparalela, de índice de refracción *n* y grosor *h*, con un haz que proceda de una fuente puntual, parte de este haz se reflejará en la primera cara y parte se transmitirá al interior de la lámina. Vamos a fijarnos en una parte del haz que se propague en una determinada dirección (un rayo incidente que incide sobre la lámina con un ángulo $\theta_i$). El haz transmitido, al llegar a la segunda cara, sufrirá a su vez una reflexión interna, transmitiéndose parcialmente al siguiente medio. Si nos ocupamos ahora mismo del haz que se refleja internamente en la segunda cara, este haz llegará a continuación de nuevo a la primera cara, sufriendo otra reflexión interna y transmitiéndose a su vez parcialmente al medio exterior. Este proceso de reflexiones internas se repetirá, bien hasta que el haz salga de la lámina, o bien hasta que se quede sin energía.
# 
# Tenemos por tanto una situación en la que la reflexión y la transmisión global de la lámina es un conjunto de ondas producidas por las continuas reflexiones internas. Además, observando la figura podemos apreciar que estas ondas se propagarán en la misma dirección (los rayos de salida son paralelos). Si hacemos coincidir estos haces, por ejemplo utilizando una lente convergente, en su plano focal imagen observaremos la interferencia de todas estas ondas.
# 
# <center>
# <img src="laminaRefleTransmi.png" height=200px style="max-width:60%">
# </center>
# 
# Por supuesto, las reflexiones y transmisiones producidas en cada paso, llevan consigo que el haz que se propaga por el interior de la lámina sea cada vez mas débil, por lo que los haces reflejados internamente más de una vez contribuirán cada vez menos a la irradiancia total. Este hecho nos permite, como primera aproximación al problema, considerar únicamente la interferencia de las dos primeras ondas reflejadas/transmitidas en la lámina. De este modo podremos aplicar la expresión de la irradiancia total vista anteriormente para el caso de dos ondas, es decir,
# 
# $$I_t = I_1 + I_2 + 2\sqrt{I_1 I_2} \cos(\delta)$$
# 
# en donde en la expresión anterior, $I_1$ ahora será la irradiancia de la primera onda reflejada/transmitida (según estemos considerando la interferencia en reflexión o transmisión), $I_2$ será la irradiancia de la segunda onda reflejada/transmitida, $\delta$ es el desfase total entre estas ondas, que debemos calcular. Por último, hay que apuntar que en la ecuación anterior se ha supuesto que los haces que interfieren se propagan con igual polarización.
# 
# A continuación vamos a analizar la interferencia que se produce en reflexión. Para ello, primero tenemos que obtener la irradiancia de cada onda que participa en la interferencia, así como el desfase entre ellas.
# 
# 

# ## Irradiancia de las ondas que interfieren en reflexión
# 
# Para calcular la irradiancia de las dos primeras ondas reflejadas por la lámina tenemos que observar que procesos de reflexión y transmisión sufren dichas ondas hasta que convergen en el plano de observación.
# 
# <center>
# <img src="laminaRefleInten.png" height=200px style="max-width:60%">
# </center>
# 
# La primera onda reflejada (cuya irradiancia hemos denominado $I_1$), sufre únicamente una reflexión en la primera cara de la lámina. Tendremos por lo tanto que,
# 
# $$I_1 = R_1 I_0$$
# 
# siendo $R_1$ la reflectancia en esa primera cara e $I_0$ la irradiancia del haz incidente en la lámina. Por otro lado, la reflectancia la podemos escribir en función del coeficiente de reflexión $r_1$ como $R_1 = | r_1|^2$ donde la expresión del coeficiente de reflexión depende tanto de la polarización del haz incidente (paralela al plano de incidencia o perpendicular al mismo), así como del ángulo de incidencia y de los índices de refracción de la lámina y del medio exterior. Por ejemplo, para el caso en el que la polarización del haz incidente sea perpendicular al plano de incidencia, y el medio desde el que incide la onda sea aire, el coeficiente de reflexión $r_1$ toma la siguiente expresión:
# 
# 
# $$
# r_1 = \frac{\cos(\theta_i) - n \cos(\theta_t)}{\cos(\theta_i) + n \cos(\theta_t)}
# $$
# 
# Por otro lado, la segunda onda reflejada (cuya irradiancia hemos denominado $I_2$) sufre una transmisión en la primera cara de la lámina, una reflexión en la segunda cara, y finalmente otra transmisión, de nuevo en la primera cara, desde el interior de la lámina hacia el exterior. Por tanto, podemos expresar $I_2$  en función de $I_0$ mediante los coeficientes de transmisión y reflexión del siguiente modo:
# 
# 
# $$
# I_2 = (t_1 r_2 t_1')^2 I_0
# $$
# 
# donde $t_1$ es el coeficiente transmisión de la primera cara cuando la luz incide desde el exterior, $r_2$ el coeficiente de reflexión en la segunda cara y $t_1'$ es el coeficiente de transmisión en la primera cara cuando la luz incide desde el interior de la lámina. Estos coeficientes, al igual que en el caso de $r_1$, dependen de la polarización del haz incidente, del ángulo de incidencia y de los índices de los medios que separan las interfases de la lámina. Para el caso particular en que la polarización del haz sea perpendicular al plano de incidencia y el medio que rodea la lámina sea aire, tenemos que,
# 
# 
# $$
# t_1= \frac{2 \cos(\theta_i)}{\cos(\theta_i) + n \cos(\theta_t)}
# $$
# 
# 
# $$
# r_2= \frac{n \cos(\theta_t) - \cos(\theta_i)}{\cos(\theta_i) + n \cos(\theta_t)}
# $$
# 
# 
# $$
# t_1'= \frac{2 n \cos(\theta_t)}{\cos(\theta_i) + n \cos(\theta_t)}
# $$
# 
# Como vemos, la irradiancia de la onda que se refleja en la segunda cara será, en general, significativamente menor que la irradiancia de la onda reflejada en la primera cara ($I_2 < I_1$). Esa diferencia de irradiancias se traducirá en que el contraste del patrón de interferencias se reducirá y no alcanzará el valor de 1, tomando los mínimos de interferencia valores mayores que 0.
# 
# Irradiancia de las ondas que interfieren en transmision
# 
# Como se aprecia en la gráfica, las ondas que interfieren en transmisión sufren más reflexiones o transmisiones en las caras de la lámina que las que interfieren en reflexión. Esto va a dar lugar a que la irradiancia total sea menor en este caso. Aparte de ello, las irradiancias tampoco serán iguales por lo que el contraste del digrama interferencial también en este caso será menor que 1. Más concretamente, y observando la figura anterior, podemos calcular las irradiancias $I_1$ e $I_2$ de las ondas que interfieren según las siguientes expresiones:
# 
# 
# $$
# I_1 = (t_1 t_2') ^2 I_0
# $$
# 
# 
# $$
# I_2 = (t_1 r_2 r_1 t_2')^2 I_0
# $$
# 
# 

# ## Desfase entre las ondas que interfieren
# 
# <center>
# <img src="laminaplanoparalela2.png" height=200px style="max-width:60%">
# </center>
# 
# El desfase entre las ondas que interfieren **en reflexión**  vendrá dado por dos contribuciones. La primera de ellas es, simplemente, el desfase debido a la diferencia de camino recorrida por cada una de las dos ondas. Efectivamente, si miramos el diagrama anterior, vemos que la segunda onda, al penetrar en la lámina y reflejarse en la segunda cara, recorre más camino óptico que la primera hasta llegar al punto en el que se solapan, que puede ser, como hemos comentado anteriormente, el plano focal de una lente convergente. Esta diferencia de camino la podemos expresar del siguiente modo.
# 
# $$\Delta = n(\overline{AB} + \overline{BC}) - \overline{AD}$$
# 
# donde se ha considerado que el índice del medio exterior es 1. Ahora estos segmentos los queremos escribir en función del grosor de la lámina $h$ o el ángulo de incidencia $\theta_i$, que son parámetros que podemos controlar en un supuesto experimento.  Para ello, y con algo de trigonometría, podemos darnos cuenta de que, 
# 
# $$\overline{AB} = \overline{BC} = \frac{h}{\cos(\theta_t)}$$
# $$\overline{AD} = \overline{AC} \sin(\theta_i) = 2 h \tan(\theta_t) \sin(\theta_i) $$
# 
# Es decir, $\Delta = 2 n h / \cos(\theta_t) + 2 h \tan(\theta_t) \sin(\theta_i)$. Ahora utilizando la ley de Snell, $\sin(\theta_i) = n \sin(\theta_t)$, y las relaciones entre las funciones trigonométricas, podemos transformar esta expresión en,
# 
# $$\Delta = 2 n h \cos(\theta_t)$$.
# 
# Por tanto, el desfase debido a esta diferencia de camino, que llamaremos *desfase geométrico* y denotaremos como $\delta_G$ , será 
# 
# $$\delta_G = k \Delta =  \frac{2 \pi}{\lambda} 2 n h \cos(\theta_t)$$
# 
# Como hemos comentado anteriormente, este no es el único desfase que tenemos que considerar en la expresión de la irradiancia total. El motivo es que los coeficientes de reflexión en la primera y segunda cara, que afectan respectivamente a la onda 1 y a la onda 2, pueden ser de distinto signo. Efectivamente, si consideramos la expresión general del coeficiente de reflexión para, por ejemplo, un haz polarizado linealmente perpendicular al plano de incidencia tenemos, 
# 
# $$r = \frac{n_i \cos(\theta_i) - n_t \cos(\theta_t)}{n_i \cos(\theta_i) + n_t \cos(\theta_t)}$$
# 
# en donde $n_i/n_t$ son los índices de los medios desde el que incide la luz y al que pasa, respectivamente. Y $\theta_i/\theta_t$ son los ángulos de incidencia y transmisión en la interfase respectivamente. Como vemos, en función de los valores de los índices, el signo del coeficiente de reflexión puede ser positivo (si $n_i > n_t$) o negativo (si $n_i < n_t$). Este cambio de signo puede cambiar completamente el carácter de la interferencia, porque si afecta sólo a una de las ondas que interfieren, tendríamos que los campos tenderían a cancelarse en vez de a reforzarse cuando únicamente el desfase geométrico daría lugar a máximos. Es decir, de interferencia constructiva, pasaríamos a interferencia destructiva!.
# 
# Afortunadamente, podemos incluir este cambio de signo de una forma sencilla en nuestro esquema de trabajo si nos damos cuenta de un signo negativo es equivalente a una fase adicional en la onda de $\pi$ rad, ya que $e^{i\pi} = -1$. Por tanto, añadiremos al desfase total que sufren las dos ondas un nuevo desfase que denominaremos *desfase debido a las reflexiones* y denotaremos como $\delta_R$. Este desfase será igual a $\pi$ rad cuando el signo de los dos coeficientes de reflexión no sea el mismo, y 0 rad, cuando sí que lo sea. Es decir, 
# 
# 
# $$ \delta_R = \left\{ 
#   \begin{array}{ c l }
#     \pi \;\; \textrm{rad} & \quad \textrm{si } n_i > n \;\& \;n <n_s \;\; \textrm{ó}\;\;  n_i <n \;\& \; n >n_s\\
#     0  \;\;   \textrm{rad}        & \quad \textrm{en el resto de casos}
#   \end{array}
# \right.$$
# 
# donde $n_i$ es el índice del medio desde el que incide la luz, $n$ es el índice de la lámina y $n_s$ el índice del medio al que se transmite la luz después de la lámina. Podemos ver, por tanto, que en el caso anteriormente considerado de una lámina rodeada de aire, tendríamos que $\delta_R = \pi$ rad. 
# 
# Finalmente, el desfase total de las dos ondas que interfieren en reflexión será $\delta_{tot} = \delta_G + \delta_R$.
# 
# 
# Para el caso de las ondas que interfieren en transmisión, podemos observar que el desfase debido a la diferencia de camino es el mismo que el calculado anteriormente, mientras que el desfase debido a las reflexiones es justo el opuesto que el caso anterior, al tener la segunda onda dos reflexiones internas, una en la segunda cara, y otra en la primera. La consecuencia es que en las condiciones en las que encontremos máximos en reflexión, encontraremos mínimos en la interferencia de las ondas que se transmiten, y al revés. Evidentemente, esto es algo esperable, ya que si la lámina no absorbe nada de energía, si la irradiacia es máxima en reflexión, ha de ser mínima en transmisión ya que la suma de ambas ha de ser igual a la irradiancia del haz incidente.
# 

# ### Patron de franjas observado en el plano focal de una lente convergente
# 
# 
# Anteriormente hemos comentado que las ondas reflejadas en ambas caras salen propagándose en direcciones paralelas pudiendo observar el patrón de interferencias en el plano focal de una lente convergente. ¿Pero cómo es este patrón?. Podemos deducir su forma observando las figuras anteriores y añadiendo una lente que recogería los haces reflejados en la lámina y que proceden, inicialmente, de la fuente S. Si esta fuente no es puntual, a distintos puntos de la superficie llegarán haces procedentes de distintos puntos de la fuente, cada uno de ellos con un ángulo de incidencia distinto, iluminando de este modo toda la superficie de la lámina. En términos de rayos (que nos marcan las direcciones de propagación de los haces), podemos decir que rayos que incidan con el mismo ángulo de incidencia en diferentes puntos darán lugar a dos rayos reflejados que llegarán a la lente subtendiendo el mismo ángulo, lo que finalmente los hará converger a la misma distancia del eje de la lente. Al incidir con el mismo ángulo de incidencia los pares de haces reflejados en cada punto tendrán el mismo desfase, y el carácter de la interferencia (constructiva o destructiva) será el mismo.
# 
# Tenemos por tanto, que los rayos que incidan en diferentes puntos de la superficie de la lámina con un ángulo de incidencia que dé lugar a un máximo de interferencia distribuirán este máximo en una circunferencia con centro el eje de la lente, es decir, el patrón de interferencias consistirá en circunferencias concéntricas de máximos y mínimos. Si observamos una región pequeña de la lámina o si la fuente es muy pequeña, veremos arcos de circunferencia únicamente.
# 
# MEJORAR! FIGURA??
# 

# In[1]:


# MODIFICAR ESTE VALOR PARA VER COMO CAMBIA LA FIGURA
from numpy import *
from matplotlib.pyplot import *
####################
fig = figure(figsize=(16,6))
Lambda =600 #(nm)
n = 1.4 # índice de refracción de la lámina 
e = 20*Lambda/n # escogemos el espesor de la lámina (en nm)
focal =30 # focal de la lente (mm)
x = np.linspace(-30,30,400)
[X,Y] = meshgrid(x,x)
rho =  np.sqrt(X**2 + Y**2) #(mm)
theta_i = arctan2(rho,focal)
theta_t = arcsin((1.0/n)*sin(theta_i))

deltaG = (4.0*pi/Lambda)*n*e*cos(theta_t)
deltaR = pi

r1 = (cos(theta_i) - n*cos(theta_t))/(cos(theta_i)+n*cos(theta_t))
t1 = 2*cos(theta_i)/(cos(theta_i)+n*cos(theta_t))
t1p=2*n*cos(theta_t)/(cos(theta_i)+n*cos(theta_t))
r2 = (n*cos(theta_t) - cos(theta_i))/(cos(theta_i)+n*cos(theta_t))

#i0=1;
i0=1*cos(theta_i)
i1= cos(theta_i)*i0*r1**2
i2 =cos(theta_t)*cos(theta_i)*i0*(r2*t1*t1p)**2

I_t = i1 +i2 + 2*sqrt(i1*i2)*cos(deltaG + deltaR)
subplot(1,2,1)
pcolormesh(X,Y,I_t,cmap=cm.copper,vmin=0,vmax=1);
colorbar()
subplot(1,2,2)
plot(x,I_t[:,I_t.shape[1]//2])
## algo está mal porque en el centro debería ser un mínimo si no me equivoco..


# 
# ### Condición de máximo y mínimo. Franjas de igual inclinación
# 
# La condición para tener máximos de interferencia es, al igual que en otros casos, que el desfase total sea igual  a $2 m \pi$ rad. Dependiendo de la relación entre los índices de la lámina, el medio desde el que incide la luz, y el medio al que se transmite tras la lámina, el desfase debido a las reflexiones tomará el valor 0 ó $\pi$ rad, cambiando por tanto la condición de máximos. Si nos centramos en uno de los dos casos, por ejemplo cuando $\delta_R = \pi$ rad, tendríamos como condición de máximo, 
# 
# $$\delta_G + \delta_R = 2 m \pi \Rightarrow   \frac{4 \pi}{\lambda} n h \cos(\theta_t) +  \pi = 2 m \pi \Rightarrow \frac{n h \cos(\theta_t)}{\lambda} = \frac{(2 m -1)}{4}$$
# 
# Si realizamos una operación similar para el caso de los mínimos de interferencia, tendríamos (también para el caso particular en el que $\delta_R = \pi$ rad), 
# 
# $$\delta_G + \delta_R = (2 m +1)\pi \Rightarrow   \frac{4 \pi}{\lambda} n h \cos(\theta_t) +  \pi = (2 m +1)\pi \Rightarrow \frac{n h \cos(\theta_t)}{\lambda} = \frac{m}{2}$$
# 
# 
# Vemos por tanto que para una determinada longitud de onda y, dada una lámina con un espesor definido, el único parámetro libre que nos queda en las anteriores expresiones, y que por tanto define la posición de los máximos y mínimos en el plano focal de la lente convergente es el ángulo de transmisión en la primera cara $\theta_t$. Este ángulo viene fijado a través de la ley de Snell por el ángulo de incidencia y la relación de los índices de la lámina y del medio desde el que incide la luz. De ahí que a este tipo de franjas observadas gracias a una lámina planoparalela se les denomine **franjas de igual inclinación**.
# 

# ## Vídeo lección virtual
# El siguiente vídeo muestra una explicación sobre las interferencias en láminas de caras planoparalelas y de las franjas de igual inclinación que aparecen como resultado de la interferencias de los haces reflejados en ambas caras de la lámina.

# In[2]:


nombre_archivo_video = "LibroVirtual_LáminaPlanoParalela.mp4"

from IPython.display import Video
Video(nombre_archivo_video)


# In[ ]:




