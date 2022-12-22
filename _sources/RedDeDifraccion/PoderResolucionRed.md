---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Poder de Resolucion de la Red de difraccion

+++

En el anterior documento hemos visto cómo una red de difracción es capaz de separar espacialmente el espectro que compone la radiación que incide sobre ella. Efectivamente, la ecuación de la red,

$$ d(\sin(\theta) - \sin(\varepsilon)) = m \lambda$$

nos dice que, dentro de un mismo orden de difracción (mismo valor de $m$), cada longitud de onda nos va a dar un máximo localizado en distintos ángulos. Por otro lado, también hemos visto que estos máximos tienen una cierta anchura, menor cuanto mayor sea el número de rendijas iluminadas de la red. Esta anchura, en radianes, vimos que era igual a,

$$\Delta \theta \simeq   \frac{2 \lambda}{ N d}$$

donde $N$ es el número de rendijas iluminadas y $d$ el paso de la red.

Esta capacidad de separar las distintas longitudes de onda permite utilizar la red de difracción como un instrumento de medida del espectro desconocido de distintas fuentes. Pero una vez nos planteamos utilizar la red de difracción para este fin, surge inevitablemente la pregunta sobre cuál es su capacidad para separar dos longitudes de onda muy próximas. Aunque maás adelante daremos una expresión para poder cuantificarlo, es útil definir, aunque sea de forma poco precisa, a esta capacidad de distinguir dos longitudes de onda próximas como _poder de resolución_ de la red. En cierto sentido es similar al _poder de resolución_ que utilizamos para hablar de la capacidad de un sistema óptico para distinguir las imágenes de dos objetos muy próximos, pero hay que señalar que en este caso, no hay formación de imagen de ningún objeto ni nada por el estilo. En este contexto, nos referimos a la posibilidad de medir dos longitudes de onda distintas utilizando la red de difracción.

- De qué depende que podamos distinguir dos máximos correspondientes a dos longitudes de onda muy próximas?. De modo cualitativo, podemos pensar que distinguiremos dos máximos si están _suficientemente_ separados como para identificarlos como distintos. Es decir, que no se confundan entre sí.

- Cómo podemos establecer un criterio para establecer que dos máximos se encuentran _suficientemente_ separados?. En este caso, no hace falta recurrir a un nuevo criterio. Ya disponíamos de uno, el criterio de Rayleigh, que podemos utilizar aquí estableciendo que _dos máximos correspondientes a dos longitudes de onda se encontrarán resueltos cuando la separación entre los máximos sea mayor que la semianchura de uno de ellos_. Es decir, igual que lo utilizábamos para establecer si dos manchas de Airy se encontraban resueltas, lo podemos utilizar aquí (en aquella ocasión, la semianchura del máximo era el radio de la mancha de Airy).

Ahora, para poder establecer herramientas cuantitativas y poder, por ejemplo, elegir entre dos redes de difracción para realizar una medida de un espectro, tenemos que dar, por un lado, una expresión para la separación entre los máximos correspondientes a dos longitudes de onda (que asumiremos que son próximas), y por otro, comparar lo que obtengamos con la semianchura de un máximo. Veamos el primer punto:

Supongamos que tenemos dos longitudes de onda $\lambda$ y $\lambda + \Delta \lambda$. Cada una de ellas dará un máximo en el orden $m$, cuyas posiciones vendrán dadas por la ecuación de la red para cada una,

$$ d(\sin(\theta) - \sin(\varepsilon)) = m \lambda$$
$$ d(\sin(\theta + \delta \theta) - \sin(\varepsilon)) = m (\lambda + \Delta \lambda)$$

La segunda ecuación nos indica que el ángulo que define la posición del máximo para la segunda longitud de onda será ligeramente diferente al de la primera longitud de onda. Esta segunda ecuación podemos desarrollarla sabiendo la relación trigonométrica,

$$\sin(\theta + \delta \theta) = \sin(\theta)\cos(\delta \theta) + \sin(\delta \theta) \cos(\theta)$$

Antes de introducir este desarrollo en la segunda ecuación de la red, vamos a simplificar la anterior expresión un poco. Como sabemos que $\Delta \theta$ es pequeño, podemos realizar las aproximaciones $\sin(\delta \theta) \simeq \delta \theta$ y $\cos(\delta \theta) \simeq 1$. De este modo, el desarrollo del seno de la suma de ángulos nos quedaría,

$$\sin(\theta + \Delta \theta) \simeq \sin(\theta) + (\Delta \theta) \cos(\theta)$$

Ahora sí, la introducimos en la segunda ecuación de la red, quedando,

$$ d\left(\sin(\theta) + (\delta \theta)\cos(\theta) - \sin(\varepsilon)\right) = m \lambda + m \Delta \lambda)$$

o reordenando los términos,

$$ d\left(\sin(\theta) - \sin(\varepsilon)\right)+ d(\delta \theta)\cos(\theta)  = m \lambda + m \Delta \lambda)$$

Ahora si nos fijamos en la primera de las ecuaciones de la red, para la longitud de onda $\lambda$, vemos que $ d(\sin(\theta) - \sin(\varepsilon)) = m \lambda$ por lo que la ecuación nos queda,

$$d(\delta \theta)\cos(\theta)  = m \Delta \lambda) \Rightarrow \delta \theta = \frac{m \Delta \lambda}{d \cos(\theta)}$$

Por último, realizamos la aproximación $\cos(\theta) \sim 1$ al igual que hacíamos en el desarrollo del cálculo de la anchura de un máximo. Esta aproximación es un poco más restrictiva que las anteriores pero en todo caso el posible error cometido es pequeño. Finalmente, llegamos a la expresión para la separación angular de los máximos $\delta \theta$,

$$\delta \theta \simeq \frac{m \Delta \lambda}{d}$$

Si observamos la anterior ecuación, podemos llegar a dos conclusiones,

- La separación entre máximos es mayor si se observa en un orden de difracción mayor

- Cuanto menor sea el paso de red $d$ , mayor es también esa separación

---

La anterior expresión nos da la separación angular entre los máximos, mientras que al principio del documento recordamos el valor de la anchura de un máximo. Tenemos pues los dos ingredientes para poder aplicar el criterio de Rayleigh: para que dos longitudes de onda se consideren resueltas por la red de difracción, sus máximos deben estar separados, al menos, la semianchura de uno de ellos, o dicho de otro modo,

$$\delta \theta \ge \Delta \theta /2 \Rightarrow \frac{m \Delta \lambda}{d} \ge \frac{\lambda}{ N d}$$

Operando, llegamos a la expresión final que vamos a utilizar,

<div class=alert-info>

$$ \frac{\lambda}{\Delta \lambda} \le N m$$

</div>

+++

## Poder de resolución y separación mínima.

Qué nos dice la anterior ecuación?. Por un lado, $\Delta \lambda$ es la separación entre las longitudes de onda que queremos resolver. Si las llamamos $\lambda_1$ y $\lambda_2$, $\Delta \lambda = \lambda_2 - \lambda_1$. Por otro lado, $\lambda$ normalmente se considera como la longitud de onda media de ese intervalo. En este ejemplo sería $\bar{\lambda} = (\lambda_1 + \lambda_2)/2$. Por último $m$ es el orden de difracción en el que estamos observando los máximos y $N$ es el número de rendijas **iluminadas** de la red.

Lo que nos dice la anterior ecuación es que el cociente $\frac{\lambda}{\Delta \lambda}$ ha de ser menor que una cierta cantidad, igual al producto del orden de difracción y el número de rendijas iluminadas. A este producto se le denomina **Poder de resolución de la red**, $P_r$, 

$$P_r = N m$$

Veamos algunas consecuencias de la anterior condición que hemos obtenido, 

1. A mayor diferencia de longitudes de onda ($\lambda_1$ y $\lambda_2$), el cociente $\frac{\lambda}{\Delta \lambda}$ será menor, favoreciendo que se cumpla la condición establecida por el criterio de Rayleigh. Lo cual es lógico, cuanto más diferentes sean las longitudes de onda que queremos resolver, más fácil será porque los máximos estarán más separados.

2. Una vez fijada la red de difracción y el número de rendijas iluminadas, la separación mínima entre longitudes de onda que esta red es capaz de distinguir vendrá dada por la igualdad en la ecuación que hemos obtenido. Es decir, esta separación mínima $\Delta \lambda_{min}$$ será igual a, 

<div class=alert-info>

$$\Delta \lambda_{min} = \frac{\bar{\lambda}}{N m}$$

</div>

3. A mayor número de rendijas iluminadas ($N$ mayor), el poder de resolución de la red aumenta, y la separación mínima $\Delta \lambda_{min}$ disminuye (la red es capaz de distinguir longitudes de onda más próximas) y el poder de resolución de la red aumenta.

4. Si observamos en un orden de difracción más alto, esta separación mínima también disminuye y el poder de resolución de la red también aumenta.

+++

El siguiente programa permite ver cómo se separan los máximos de irradiancia para dos longitudes de onda separadas por lo que en el programa se denomina `DeltaLambda`. Se puede observar cómo cambiando el número de rendijas iluminadas los máximos se hacen más estrechos, permitiendo distinguir espacialmente las dos longitudes de onda.

Cambiar la separación entre longitudes de onda y el número de rendijas para observar cuándo se cumple el Criterio de Rayleigh para resolver dos longitudes de onda.

```{code-cell} ipython3
from numpy import *
import numpy as np
from matplotlib.pyplot import *
style.use('ggplot')
%matplotlib inline

# Parametros
#########
a = 0.0005 # anchura de cada rendija en mm
d = 1.0/600 # paso de la red
E0 = 100.0 # Amplitud del campo normalizada a 1
N = 80 # Numero de rendijas iluminadas

Lambda1 = 555e-6 # longitud de onda 1 en mm
DeltaLambda = 3e-6 # separacion entre las dos longitudes de onda.
################
##################

Lambda2 = Lambda1 + DeltaLambda # longitud de onda 2 en mm
k1 = 2.0*pi/Lambda1
k2 = 2.0*pi/Lambda2

theta = linspace(0.01,50,6000)*pi/180
Delta = d*sin(theta)
beta1 = pi*a*sin(theta)/Lambda1
beta2 = pi*a*sin(theta)/Lambda2
E1 = (E0/N)*(sin(beta1)/beta1)
E2 = (E0/N)*(sin(beta2)/beta2)

fases1 = zeros(((N-1),len(theta)),dtype=complex)
fases2 = zeros(((N-1),len(theta)),dtype=complex)
for i in range(len(fases1)):
    fases1[i,:] = 1j*k1*i*Delta
    fases2[i,:] = 1j*k2*i*Delta
Etotal1 = sum(exp(fases1),axis=0)*E1
Etotal2 = sum(exp(fases2),axis=0)*E2
Itotal1 = abs(Etotal1)**2
Itotal2 = abs(Etotal2)**2
fig = figure(figsize=(18,8))
subplot(121)
plot(theta*180/pi,Itotal1,theta*180/pi,Itotal2)
xlabel('Angulo (grados)')
ylabel('Irradiancia');
subplot(122)
title('orden 2')
plot(theta*180/pi,Itotal1,theta*180/pi,Itotal2)
xlabel('Angulo (grados)')
ylabel('Irradiancia')
xlim([40,44])
ylim([0,2500])

del(fases1)
del(fases2)
#del(theta)
del(Delta)
```

## Poder de resolución de un monocromador

+++

<center>

<img src=./monocromador4.jpg width=500px></img>

</center>


Como hemos visto, las características de la red de difracción imponen un límite en su capacidad para resolver dos longitudes de onda cercanas. Sin embargo, este no es el único límite que tenemos que considerar si hablamos de la capacidad de un *dispositivo* para resolver dos longitudes de onda cercanas. 

La clave, es qué compone un *dispositivo* de medida de espectros. Por supuesto uno de los componentes será la red de difracción como elemento que separa espacialmente el espectro de la radiación (podría ser un prisma con una alta dispersión, pero en este tema nos centramos en las propiedades de la red de difracción). Pero a su vez, necesitamos *preparar* la luz que incide en la red para que entre un haz colimado a un cierto ángulo $\varepsilon$ con respecto a la normal a la red. Para ello normalmente se utiliza una lente convergente antes de la red y colocamos la fuente en el foco objeto de dicha lente. Por otro lado, necesitamos otra lente convergente detrás de la red para observar el espectro en su plano focal imagen. De este modo, ya tenemos casi nuestro espectrómetro o monocromador. 

Sin embargo, nos falta un elemento para poder medir el espectro en el plano focal imagen. Necesitamos seleccionar los máximos para realizar la medida. Esta selección se puede realizar por una rendija y a continuación un detector, o bien, si sustituimos nuestra pantalla en el plano focal imagen por el sensor de una cámara CCD, la selección la realizan los píxeles del sensor, que tienen un cierto tamaño. En cualquier caso, hay un elemento en ese plano focal imagen, que tiene una cierta anchura $L$ que selecciona una pequeña parte del espectro. 

Esta anchura $L$, al ser finita, hace que entre en el detector (o sea recogido por el píxel del sensor de una cámara), no una única longitud de onda, sino un cierto rango $\Delta \lambda_{rendija} = \lambda_{sup} - \lambda_{inf}$, donde $\lambda_{sup,inf}$ denotan las longitudes de onda cuyos máximos se encuentran en el borde superior o inferior de la rendija y que podemos calcular utilizando la ecuación de la red. Esta diferencia podrá ser mayor o menor que la $\Delta \lambda_{min}$ capaz de resolver la red de difracción por sus propias limitaciones (orden de difracción $m$ en el que se observa y número de rendijas iluminadas $N$). En cualquier caso, hay siempre que considerar que el tamaño de esta rendija puede reducir el poder de resolución del dispositivo. Para estimarlo, lo podemos definir de forma análoga al poder de resolución de la red, 

$$P_{r,dispositivo} = \frac{\bar{\lambda}}{\Delta \lambda_{min,dispositivo}}$$

donde $\Delta \lambda_{min,dispositivo}$ se refiere a la separación mínima entre dos longitudes de onda que puede distinguir el dispositivo, y que vendrá determinada por la red de difracción o por la rendija de observación en función de cuál de ellas es mayor (siempre habrá que escoger en este caso la mayor de las dos, pues será la que limite más el poder de resolución).

-----

El siguiente código muestra en la figura de la izquierda de nuevo el orden 2 que se dibuja en la figura del apartado anterior, pero esta vez añadiendo mediante una sombra en verde el tamaño de un rendija con la que mediríamos el espectro mediante un detector situado detrás suya, el cual registraría la irradiancia total que pasa a través de la rendija. Se puede variar el tamaño de la rendija y observar cómo una rendija mayor va a dar lugar a una pérdida de detalle en la irradiancia registrada, no pudiendo de ese modo distinguir ambos máximos.

```{code-cell} ipython3
from numpy import *
import numpy as np
from matplotlib.pyplot import *
style.use('ggplot')
%matplotlib inline

# Parametros de la red
#########
a = 0.0005 # anchura de cada rendija en mm
d = 1.0/600 # paso de la red
N = 30 # Numero de rendijas iluminadas

Lambda1 = 555e-6 # longitud de onda 1 en mm
DeltaLambda = 10e-6 # separacion entre las dos longitudes de onda.
################

# Anchura del detector

AnchuraDetector = 100 # numero de puntos que componen la rendija. Cambiar entre 2 y 500 para incrementar su tamaño
##################

Lambda2 = Lambda1 + DeltaLambda # longitud de onda 2 en mm
k1 = 2.0*pi/Lambda1
k2 = 2.0*pi/Lambda2
E0 = 100.0 # Amplitud del campo
theta = linspace(0.01,50,10000)*pi/180
Delta = d*sin(theta)
beta1 = pi*a*sin(theta)/Lambda1
beta2 = pi*a*sin(theta)/Lambda2
E1 = (E0/N)*(sin(beta1)/beta1)
E2 = (E0/N)*(sin(beta2)/beta2)

fases1 = zeros(((N-1),len(theta)),dtype=complex)
fases2 = zeros(((N-1),len(theta)),dtype=complex)
for i in range(len(fases1)):
    fases1[i,:] = 1j*k1*i*Delta
    fases2[i,:] = 1j*k2*i*Delta
Etotal1 = sum(exp(fases1),axis=0)*E1
Etotal2 = sum(exp(fases2),axis=0)*E2
Itotal1 = abs(Etotal1)**2
Itotal2 = abs(Etotal2)**2
fig = figure(figsize=(18,8))
subplot(121)
title('orden 2')
plot(theta*180/pi,Itotal1,theta*180/pi,Itotal2)

xlabel('Angulo (grados)')
ylabel('Irradiancia')
xlim([38,46])
ylim([0,2500])

del(fases1)
del(fases2)
#del(theta)
del(Delta)
##################
AngulosDetector = AnchuraDetector*(theta[1]-theta[0])*180/np.pi
fill_betweenx(Itotal1,42-AngulosDetector,42+AngulosDetector,color='green',alpha=0.3)
legend((r'$\lambda_1$',r'$\lambda_2$','Rendija'))
nn = np.size(theta)//AnchuraDetector
n = np.size(theta)
Idet = np.zeros(n)
thetadet = np.zeros(n)
h = -1
Itotdet = Itotal1+Itotal2
ind0 = 7600 # coincide con 38 grados para theta con 10000 puntos
ind1 = 9200 # coincide con 46 grados para theta con 10000 pts
for i in np.arange(ind0,ind1,1):
    h = h+1
    Idet[h] = np.sum((Itotdet)[i-AnchuraDetector//2:i+AnchuraDetector//2])
    thetadet[h]=theta[i]*180/pi

Idet = Idet
subplot(122)
title('orden 2 tras rendija')
plot(thetadet,Idet)
xlabel('Angulo (grados)')
ylabel('Irradiancia')
xlim([38,46])
ylim([0,Idet.max()*1.3]);
```

```{code-cell} ipython3

```
