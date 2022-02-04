#!/usr/bin/env python
# coding: utf-8

# # Diseño y caracterización de un tratamiento antirreflejante para una lente oftálmica

# ## Tarea 1. Lente oftálmica. Caracterización de las pérdidas por reflexión

# Primero vamos a elegir una lente oftálmica de alto índice. Realizar una búsqueda en internet e incluir los datos de la lente seleccionada y la dirección de la página web  (*modificar este texto*): 
# 
# * material o nombre 
# 
# * índice de refracción $n_L$= 
# 
# * dirección de la página web, (por ejemplo http://www.ucm.es) 
# 
# Vamos a caracterizar las pérdidas por reflexión de la lente. Calculamos la reflectancia en tanto por ciento en la primera cara de la lente (interfase aire-lente) empleando el coeficiente de reflexión en incidencia normal *escribir aquí el valor modificando este texto*
# 
# * R = %

# ##  Tarea 2. Diseño del tratamiento antirreflejante. Espesor de la monocapa. 

# Vamos a diseñar un tratamiento antirreflejante para la lente de alto índice. Para ello empleamos una capa de fluoruro de magnesio (MgF$_2$) cuyo índice de refracción en el rango del visible se puede aproximar a $n_c$=1.38. Este material presenta un índice de refracción sensiblemente inferior a los típicos de las lentes donde se deposita. 
# 
# Para elegir el tamaño adecuado de la monocapa antirreflejante vamos a considerar incidencia normal ($\theta_i$=0) y tenemos que decidir para que longitud de onda optimizamos el tratamiento. Para elegir esta longitud de onda ejecutar la celda de código que aparece debajo. Esta operación se realizará una única vez, es decir, no habrá que ejecutarla nunca más.

# In[1]:


# NO TOCAR. SOLO EJECUTAR (SOLO UNA VEZ)
####################################################################################
get_ipython().run_line_magic('pylab', 'inline')
lambda0 = int(np.random.rand()*150 +475)
print "Longitud de onda para la que optimizamos el tratamiento = ",lambda0, " nm"


# 
# Escribir aquí el valor de la longitud de onda seleccionada (que aparece arriba) 
# 
# * longitud de onda $\lambda_0$=   nm 
# 
# Calculamos el espesor más pequeño de la monocapa *escribir aquí su valor numérico modificando este texto*
# 
# * espesor1 =   nm
# 

# ## Tarea 3. Caracterización del tratamiento antirreflejante en incidencia normal 

# Vamos a caracterizar la reflectancia de la lente de alto índice con el tratamiento antirreflejante en función de la longitud de onda en el rango del visible. Consideramos el caso de incidencia normal y el espesor calculado en la Tarea 2 (estas son las condiciones que se han empleado en el diseño del tratamiento).  
# 
# En la siguiente celda aparece el código de programación que calcula y pinta dicha reflectancia (en tanto por ciento).
# El texto que aparece después del símbolo # son comentarios.

# In[ ]:


# MODIFICAR LOS DOS PARAMETROS. LUEGO EJECUTAR
########################################################

nL = 1.85 # Incluir el índice de la lente de alto índice

espesor1 = 99.5 # Incluir el valor del espesor de la capa (en nm)

# DESDE AQUÍ NO TOCAR 
##############################################################################################################################

get_ipython().run_line_magic('pylab', 'inline')
nc = 1.38 # Índice de la monocapa (MgF2)
longitud_de_onda = linspace(400,750,100) # Crea los valores de las longitudes de onda en el visible (en nm)

# Coeficientes de reflexion y transmision
rA = (1-nc)/(1+nc)  # Coeficiente de reflexión aire --> monocapa
tA = 2*1/(1+nc)     # Coeficiente de transmisión aire --> monocapa
rB = (nc-nL)/(nc+nL) # Coeficiente de reflexión monocapa --> lente
tC = 2*nc/(nc+1)     # Coeficiente de transmissión monocapa --> aire

# Desfase y Reflectancia para el espesor mínimo
desfase1 = (2*pi/longitud_de_onda)*2*nc*espesor1 + 0*pi # desfase geométrico + desfase debido a las reflexiones
Reflectancia_tratamiento1 = 100*( rA**2 + (tA*rB*tC)**2 + 2*sqrt( (rA**2)*(tA*rB*tC)**2 )*cos(desfase1) ) # Reflectancia (%) 

# Dibujamos la reflectancia en función de la longitud de onda
fig,ax = plt.subplots()
plot(longitud_de_onda,Reflectancia_tratamiento1,lw=2) # Pintamos la reflectancia
xlabel('$\lambda$ (nm)',fontsize=16)
ylabel('Reflectancia (%)',fontsize=16) # Escribimos los nombres de los ejes;


# A la vista de la gráfica comentar *(modificando el texto de este apartado)* los siguientes puntos:
# 
# * valor mínimo de la reflectancia y la longitud de onda en la que ocurre. ¿Tiene algo que ver esta longitud de onda con la seleccionada en la Tarea 2, es decir  con $\lambda_0$?, explicar la relación.
# 
# 
# * valor máximo de la reflectancia y la longitud de onda en la que ocurre. 
# 
# A continuación prestamos atención a los valores de la reflectancia a lo largo de todo el visible, es decir, a toda la curva. Comparando dichos valores con el valor de la reflectancia de la lente calculada en la Tarea 1: 
# 
# * comentar razonadamente si el tratamiento antirreflejantes es eficaz.

# ## Tarea 4. Caracterización del tratamiento antirreflejante con el ángulo de incidencia 

# Vamos a estudiar como se comporta nuestro tratamiento cuando consideramos ángulos de incidencia distintos de cero. Para ello calculamos la reflectancia de la lente con el tratamiento para un ángulo de incidencia $\theta_i$. Usando este ángulo, el código que aparece en la siguiente celda calcula los ángulos incidentes y transmitidos en la distintas interfases y calcula la reflectancia del sistema para las dos componentes de polarización. Al considerar luz despolarizada la reflectancia será el promedio de las dos. En la gráfica se muestra la reflectancia para el ángulo de incidencia seleccionado junto con el caso de incidencia normal. 
# 
# **Antes de ejecutar la siguiente celda, habremos tenido que ejecutar durante esta sesión de trabajo (al menos una vez) la celda de código correspondiente a la Tarea 3 (correspondiente a incidencia normal y espesor mínimo de la monocapa)**. 

# In[ ]:


# MODIFICAR EL PARAMETRO. LUEGO EJECUTAR
#######################################################################################################

angulo_incidente = 30 # Incluir el ángulo de incidencia (en grados) a la interfase aire-monocapa 

# DESDE AQUÍ NO TOCAR. 
##############################################################################################################################


angulo_incidente = angulo_incidente*pi/180 # Pasamos el ángulo a radianes
angulo_transmitido_1 = arcsin(sin(angulo_incidente)/nc) # El ángulo transmitido en la interfase aire-monocapa (en radianes) 
angulo_incidente_2 = angulo_transmitido_1 # El ángulo incidente a la interfase monocapa-lente o a la interfase monocapa-aire 
                                          # es igual al ángulo transmitido en la interfase aire-monocapa (en radianes)
angulo_transmitido_2 = arcsin(nc*sin(angulo_incidente_2)/nL) # El ángulo transmitido en la interfase monocapa-lente (en radianes)

# Coeficientes de reflexion y transmision de las dos componentes de polarización
rAs = (1*cos(angulo_incidente)-nc*cos(angulo_transmitido_1))/(1*cos(angulo_incidente)+nc*cos(angulo_transmitido_1)) # reflexión aire --> monocapa
tAs = 2*1*cos(angulo_incidente)/(1*cos(angulo_incidente)+nc*cos(angulo_transmitido_1))  # transmisión aire --> monocapa
rBs = (nc*cos(angulo_incidente_2)-nL*cos(angulo_transmitido_2))/(nc*cos(angulo_incidente_2)+nL*cos(angulo_transmitido_2))  # reflexión monocapa --> lente
tCs = 2*nc*cos(angulo_incidente_2)/(nc*cos(angulo_incidente_2)+1*cos(angulo_incidente)) # transmissión monocapa --> aire

rAp = (nc*cos(angulo_incidente)-1*cos(angulo_transmitido_1))/(nc*cos(angulo_incidente)+1*cos(angulo_transmitido_1)) # reflexión aire --> monocapa
tAp = 2*1*cos(angulo_incidente)/(nc*cos(angulo_incidente)+1*cos(angulo_transmitido_1))  # transmisión aire --> monocapa
rBp = (nL*cos(angulo_incidente_2)-nc*cos(angulo_transmitido_2))/(nL*cos(angulo_incidente_2)+nc*cos(angulo_transmitido_2))  # reflexión monocapa --> lente
tCp = 2*nc*cos(angulo_incidente_2)/(1*cos(angulo_incidente_2)+nc*cos(angulo_incidente)) # transmissión monocapa --> aire

# Desfase y Reflectancia
desfase1_angulo = (2*pi/longitud_de_onda)*2*nc*espesor1*cos(angulo_transmitido_1)+0*pi # desfase geométrico + desfase debido a las reflexiones 
Reflectancia_tratamiento1_s = 100*( rAs**2 + (tAs*rBs*tCs)**2 + 2*sqrt((rAs**2)*(tAs*rBs*tCs)**2)*cos(desfase1_angulo) ) # componente s (%) 
Reflectancia_tratamiento1_p = 100*( rAp**2 + (tAp*rBp*tCp)**2 + 2*sqrt((rAp**2)*(tAp*rBp*tCp)**2)*cos(desfase1_angulo) ) # componente p (%) 
Reflectancia_tratamiento1_angulo=(Reflectancia_tratamiento1_s+Reflectancia_tratamiento1_p)/2

# Dibujamos la reflectancia en función de la longitud de onda
plot(longitud_de_onda,Reflectancia_tratamiento1,longitud_de_onda,Reflectancia_tratamiento1_angulo,lw=2) # Pintamos la reflectancia
xlabel('$\lambda$ (nm)',fontsize=16);ylabel('Reflectancia (%)',fontsize=16) # Escribimos los nombres de los ejes
legend(('incidencia normal','variando el angulo')) # Escribimos la leyenda;


# A la vista de la gráfica comentar *(modificando el texto de este apartado)* los siguientes puntos:
# 
# * Para un ángulo de 30 grados dar el valor de la reflectancia en $\lambda_0$. Para dicho ángulo de incidencia ¿cuál es el valor mínimo de la reflectancia y la longitud de onda a la que ocurre?
# 
# *  Al aumentar el ángulo de incidencia describir hacia donde se desplaza el valor de la longitud de onda que presenta el mínimo valor de la reflectancia.
# 
# * Determinar a partir de qué ángulo de incidencia la reflectancia en alguna zona del visible alcanza valores próximos a la reflectancia de la lente calculada en la Tarea 1.

# ## Tarea 5. Caracterización del tratamiento antirreflejante con el espesor de la monocapa 

# Hasta ahora hemos caracterizado el tratamiento para el espesor más pequeño posible de la monocapa. A continuación vamos a caracterizar el tratamiento para otros posibles espesores de la monocapa. Consideramos las mismas condiciones que empleamos para optimizar el tratamiento, es decir, incidencia normal y la longitud de onda $\lambda_0$.

# Escribir aquí los dos siguientes espesores de la monocapa *escribir aquí su valor numérico modificando este texto*
# 
# * espesor2 =  nm
# 
# * espesor3 =  nm

# Finalmente vamos a estudiar como se comporta nuestro tratamiento con los dos espesores calculados. También se muestra en la misma gráfica la reflectancia correspondiente al espesor mínimo. 
# 
# Antes de ejecutar la siguiente celda, habremos tenido que ejecutar durante esta sesión de trabajo (al menos una vez) la celda de código correspondientes a la Tarea 3. 

# In[ ]:


from numpy import *
from matplotlib.pyplot import *
# MODIFICAR LOS DOS PARAMETROS. LUEGO EJECUTAR
########################################################

espesor2 =   # Incluir el valor del segundo espesor más pequeño de la monocapa (en nm)

espesor3 =   # Incluir el valor del tercer espesor más pequeño de la monocapa (en nm)

# DESDE AQUÍ NO TOCAR. 
##############################################################################################################################

# Desfase y Reflectancia para el espesor mínimo
desfase1 = (2*pi/longitud_de_onda)*2*nc*espesor1 + 0*pi # desfase geométrico + desfase debido a las reflexiones
Reflectancia_tratamiento1 = 100*( rA**2 + (tA*rB*tC)**2 + 2*sqrt( (rA**2)*(tA*rB*tC)**2 )*cos(desfase1) ) # Reflectancia (%) 

# Desfase y Reflectancia para el segundo espesor mínimo
desfase2 = (2*pi/longitud_de_onda)*2*nc*espesor2 + 0*pi # desfase geométrico + desfase debido a las reflexiones
Reflectancia_tratamiento2 = 100*( rA**2 + (tA*rB*tC)**2 + 2*sqrt( (rA**2)*(tA*rB*tC)**2 )*cos(desfase2) ) # Reflectancia (%) 

# Desfase y Reflectancia para el segundo espesor mínimo
desfase3 = (2*pi/longitud_de_onda)*2*nc*espesor3 + 0*pi # desfase geométrico + desfase debido a las reflexiones
Reflectancia_tratamiento3 = 100*( rA**2 + (tA*rB*tC)**2 + 2*sqrt( (rA**2)*(tA*rB*tC)**2 )*cos(desfase3) ) # Reflectancia (%) 

# Dibujamos la reflectancia en función de la longitud de onda
plot(longitud_de_onda,Reflectancia_tratamiento1,longitud_de_onda,Reflectancia_tratamiento2,longitud_de_onda,Reflectancia_tratamiento3,lw=2) # Pintamos la reflectancia
xlabel('$\lambda$ (nm)',fontsize=16);ylabel('Reflectancia (%)',fontsize=16) # Escribimos los nombres de los ejes ç
legend(('espesor1','espesor2','espesor3'),loc = 'upper right', bbox_to_anchor = (0.5, 0.5)) # Escribimos la leyenda;


# A la vista de la gráfica comentar *(modificando el texto de este apartado)* los siguientes puntos:
# 
# * ¿cúal es el valor mínimo de la reflectancia para los tres espesores y la longitud de onda en la que ocurren?. ¿Por qué el mínimo ocurre en la misma longitud de onda?
# 
# * valor máximo de la reflectancia para los tres espesores y la longitud de onda en la que ocurren. 
# 
# * Comparando las tres curvas con el valor de la reflectancia de la lente calculada en la Tarea 1, comentar razonadamente para que espesores el tratamiento antirreflejante es eficaz.

# In[ ]:




