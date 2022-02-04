#!/usr/bin/env python
# coding: utf-8

# # Interferometro de Michelson

# ### De que se compone?
# 
# 
# El esquema de un interferómetro de Michelson se ha dibujado a continuación.
# 
# <center>
# <img src=michelsonfiguretikz.jpg width=400px></img>
# </center>
# 
# Una fuente que puede ser extensa ilumina un divisor de haz, que puede ser una lamina plano-paralela de un material dieléctrico, aunque normalmente se aplica un tratamiento a una de las caras para aumentar la reflectividad de dicha cara e igualar las irradiancias de los dos haces que separa y que van a interferir. Tanto el haz reflejado como el transmitido por el divisor se reflejan en sendos espejos $M_1$ y $M_2$, volviendo de nuevo al divisor. Parte de estos haces se reflejan de nuevo, yendo a un detector o al plano focal de una lente convergente, donde se observa la interferencia.
# 
# En esta descripción falta aun el papel que juega la lamina compensadora $LC$. La presencia de esta lamina facilita la observación de interferencias con luz no monocromática ya que permite compensar la diferencia de camino que introduce el divisor de haz. Para entender el por que de su presencia, nos hemos de fijar en el camino total que realizan los rayos dentro de la lamina que sirve como divisor de haz. En nuestro caso, el haz marcado en azul recorre 3 veces el grosor de la lamina antes de llegar al detector, mientras que el haz marcado en rojo, lo recorrería 1 vez sin la presencia de la lamina compensadora. El doble paso por esta permite igualar los caminos ópticos de ambos haces cuando la distancia de los espejos al divisor del haz son iguales.
# 
# Generalmente uno de los espejos es movil, lo que permite cambiar una de estas distancias, variando la diferencia de camino entre los haces que llegan al detector y por tanto, el carácter de la interferencia.
# 
# ### Importancia histórica
# 
# El interferómetro de Michelson es conocido por ser un elemento crucial en el desarrollo de la Teoría de la Relatividad Especial de Einstein. En el siglo XIX se consideraba que la luz no se podía propagar por el vacío, sino que, al igual que una onda en una cuerda o el sonido, necesita un medio por el que propagarse. A este medio, que debía ofrecer muy poca resistencia al movimiento (pues los planteas se mueven a través suyo) pero a la vez debía ser muy rígido (porque la luz se propaga a muy alta velocidad). A este medio se le llamaba *éter*. [El experimento de Michelson-Morley](https://en.wikipedia.org/wiki/Michelson%E2%80%93Morley_experiment) permitió establecer que el éter no existía y ser uno de los primeros resultados experimentales que llevaron finalmente a la Teoría de la Relatividad Especial.
# 
# ### Relación con franjas de igual espesor y franjas de igual inclinación. Patrones que se observan
# 
# Como se ha comentado anteriormente, la diferencia de camino $\Delta$ entre los haces depende de las posiciones de los espejos con respecto al divisor de haz $DH$. Mas concretamente, y como se observa en la siguiente figura, si llamamos $d$ a la diferencia de distancias entre los espejos y el divisor de haz ($\overline{DHM_1} - \overline{DHM_2}$), entonces, la diferencia de camino para los rayos dibujados es $\Delta = 2 d$, ya que debemos considerar tanto la ida como la vuelta desde los espejos $M_1$ y $M_2$.
# 
# <center>
# <img src=michelsonfiguretikz2.jpg width=400px></img>
# </center>
# 
# 
# Sin embargo, este valor de la diferencia de camino es valido únicamente para ese punto en el que se sitúa el detector, que se correspondería con el punto central del perfil transversal de los haces que interfieren. Para ver que patrón de interferencias tenemos cuando miramos otros rayos que no se propagan por el eje del sistema, podemos añadir una lente convergente y observar dicho patrón en su plano focal. En este caso, podemos hallar el patrón de interferencias si nos damos cuenta de que, desde este punto en el que observamos, nuestro sistema es equivalente a dos superficies planas con una distancia entre ellas y que reflejan los haces que van a interferir. Esta equivalencia la vemos si proyectamos el espejo $M_2$ sobre el camino que lleva a $M_1$, lo cual seria observar la imagen $M'_2$ de $M_2$ dada por el divisor de haz y la lamina compensadora, como aparece en la figura anterior. Al hacerlo, vemos que las franjas que observemos en el plano focal de la lente convergente pueden ser de dos tipos:
# 
# <center>
# <img src=michelsonfiguretikzlineal.jpg width=400px></img>
# </center>
# 
# 1. En el caso en el que las superficies de $M_1$ y $M'_2$ sean paralelas entre si el sistema es equivalente a una lamina planoparalela, observando anillos brillantes y oscuros, al igual que nos ocurría cuando estudiamos ese caso. A este tipo de franjas las denominamos *franjas de igual inclinación*.
# 
# 2. En el caso en el que las superficies de $M_1$ y $M'_2$ **no** sean paralelas entre si el sistema es equivalente a una cuña, observando franjas rectas equiespaciadas brillantes y oscuras. A este tipo de franjas las denominamos *franjas de igual espesor*.
# 
# <center>
# <img src = franjasmichelson.png width=300></img>
# </center>

# ## Aplicaciones

# ### Medida de la longitud de onda

# In[1]:


from IPython.display import HTML
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/j-u3IEgcTiQ?start=33" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


# Como se ha indicado anteriormente, la diferencia de camino en el punto central del patron de interferencias es $\Delta = 2 d$. Eso implica que el desfase entre los haces es $\delta = k \Delta = \frac{4 \pi}{\lambda} d$. Si observamos las distancias $d$ de uno de los espejos al divisor de haz que nos dan maximos y minimos, tendremos, 
# 
# * Maximos: $\delta = 2 m \pi$ rad $\Rightarrow d = m \lambda /2$ 
# 
# * Minimos $\delta = (2 m +1) \pi$ rad $\Rightarrow d = (2 m +1) \lambda /4$
# 
# En ambos casos, lo que debemos desplazar el espejo para pasar de un maximo/minimo al siguiente es $\Delta d = \lambda/2$. Por ello, una forma de medir la longitud de onda de la radiacion consiste en observar por cuantos minimos/maximos pasamos en el centro del patron de interferencias al desplazar un espejo una cierta cantidad $L$. Si llamamos a este numero de maximos/minimos $N$, de las relaciones anteriores se obtiene que, 
# 
# $$L = N \frac{\lambda}{2} \Rightarrow \lambda = \frac{2 L}{N}$$
# 
# como aparece en el video anterior.

# ## Medida de la longitud de coherencia de la radiacion

# Quizas la aplicacion mas importante (dentro de la carrera de Optica y Optometria) del interferometro de Michelson es la OCT (Tomografia de Coherencia Optica), la cual se basa en el funcionamiento de un interferometro de Michelson bajo iluminacion por una fuente de muy baja longitud de coherencia (y por tanto, con una gran anchura espectral). Antes de ver la OCT, vamos a analizar lo que ocurre cuando iluminamos este interferometro con radiacion no monocromatica, y si podemos utilizarlo para medir, tanto la longitud de coherencia de la radiacion como la anchura espectral.
# 
# En todo este apartado la presencia de la lamina compensadora resulta crucial, pues sin ella, la diferencia de camino entre los haces que van a los dos espejos seria desde el principio demasiado grande para observar interferencias (mayor que la longitud de coherencia de la radiacion). 
# 
# <center>
# <img src=michelsonfiguretikzlc.jpg width=400px></img>
# </center>
# 
# En cualquier caso, si la longitud de coherencia es finita, habra una distancia del espejo movil que provocara que $\Delta = 2 d > l_c$ a partir de la cual no veremos interferencia. Por tanto, anotando la distancia $D_{max}$ al divisor del haz del espejo movil a partir de la cual ya no se observan interferencias, y sabiendo la distancia $D_0$ del espejo fijo, tendremos que,
# 
# 
# $$d_{max} = D_{max} - D_0$$
# 
# $$l_c = d_{max}/2$$
# 
# y sabiendo $l_c$, sabemos la anchura espectral $\Delta \lambda = \frac{\lambda_0^2}{l_c}$.

# In[ ]:




