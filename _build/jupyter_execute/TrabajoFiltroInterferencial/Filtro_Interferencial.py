#!/usr/bin/env python
# coding: utf-8

# # Filtro interferencial para evitar el daño ocular causado por un puntero láser

# ## Introducción

# Desgraciadamente es fácil encontrar noticas sobre daño ocular causado por punteros láser. Vemos varias noticas en periódicos nacionales:
# 
# https://sevilla.abc.es/andalucia/cordoba/sevi-puntero-laser-causa-danos-irreparables-ojos-menor-12-anos-cordoba-202002011319_video.html
# 
# https://www.lavanguardia.com/vida/20131113/54394039426/alerta-lesiones-retina-punteros-laser.html
# 
# https://www.elperiodico.com/es/sociedad/20161105/alertan-del-uso-de-los-punteros-laser-porque-ya-ha-provocado-cegueras-5610137
# 
# Aquí vemos varios trabajos sobre el tema en revistas de investigación:
# 
# https://www.nature.com/articles/s41433-018-0276-z
# 
# https://link.springer.com/article/10.1007/s10792-012-9555-z
# 
# ----------
# 
# 
# El trabajo consiste en encontrar un filtro interferencial comercial que sirva para 
# proteger el ojo de la radiación visible de un puntero láser de alta potencia. El trabajo
# se divide en las siguientes tareas:

# ## Tarea 1. Exposición máxima permisible (MPE)

# La exposicióm máxima permisible (MPE *maximum permissible exposure*) es la máxima densidad de potencia 
# o de energía (W/cm$^2$ o J/cm$^2$) de un haz de luz que puede alcanzar el ojo humano sin producir daño. 
# La MPE se mide en la córnea, y depende de la longitud de onda de la radiación y del tiempo de exposición. 
# En la siguiente figura se muestra la MPE en la córnea (en unidades de irradiancia (W/cm$^2$)) en función 
# del tiempo de exposición para distintos rangos del espectro electromagnético.
# Figura de http://en.wikipedia.org/wiki/Laser_safety 

# In[1]:


from IPython.display import Image, display
Image(url="http://upload.wikimedia.org/wikipedia/commons/thumb/2/28/IEC60825_MPE_W_s.png/640px-IEC60825_MPE_W_s.png")


# ### Tarea 1 (a). Irradiancia máxima

# Como estamos considerando el haz láser de un puntero que emite en el visible, nos fijaremos en la curva corresponsidente al rango visible. El tiempo de exposición será el tiempo que tardemos en cerrar el ojo al ser iluminado. Así con este tiempo de exposición obtener de la gráfica la irradiancia máxima que puede alcanzar el ojo.
# 
# Escribir el tiempo de exposición empleado y el correspondiente valor de la irradiancia.
# 
# 
# * Tiempo de exposición =  s
# 
# * Irradiancia máxima permisible =   W/cm$^2$

# ### Tarea 1 (b). Potencia máxima

# Empleando el valor de la irradiancia anterior, y considerando que el haz que alcanza nuestro ojo está colimado
# con un tamaño equivalente al de nuestra pupila, calcular la potencia máxima que puede alcanzar nuestro ojo
# sin provocar daño (relacionar potencia e irradiancia).
# 
# Escribir el tamaño de la pupila, las operaciones y el resultado final de la potencia (en mW)
# 
# * Diámetro de la pupila  = mm
# 
# * Cálculos intermedios
# 
# * Potencia máxima permisible = mW

# ##  Tarea 2. Elección del puntero láser

# Buscar en internet información sobre un
# puntero láser visible que sea de alta potencia.
# Verificar que dicho puntero láser puede provocar daño ocular (teniendo en cuenta el resultado de la **Tarea 1 (b)**)
# 
# Escribir aquí las características técnicas de dicho láser 
# 
# * potencia
# * longitud de onda 
# * precio
# * otras características
# * página web http://www.ucm.es
# 

# ##  Tarea 3. Elección del filtro interferencial

# Vamos a buscar en internet un filtro interferencial
# comercial que permita evitar el riesgo de daño ocular para el
# puntero láser seleccionado y que a su vez nos permita seguir viendo lo mejor posible.
# Se tratará de un filtro que bloquee
# la longitud de onda del puntero láser.

# ### Tarea 3 (a). Busqueda e información del filtro interferencial

# Vamos a emplear la información accesible en la casa **Semrock** ( https://www.semrock.com/filters.aspx )
# 
# Seleccionar en esta página web un filtro adecuado. En el menú de la izquierda se puede seleccionar el tipo de filtro: pasa banda (bandpass), pasa alta y pasa baja (long-pass and short-pass), filtro suprime banda (notch). Pinchar sobre cada filtro (sobre la curva de transmitancia, sobre el *Part Number*, o sobre *Show Product Detail*) para obtener más información. Escribir aquí las características más relevantes del filtro seleccionado: 
# 
# * Nombre del filtro (*Part Number*)
# * transmitancia T o densidad óptica OD 
# * rango de longitudes de onda
# * precio
# * página web del filtro seleccionado (cambiar la siguiente dirección) https://www.semrock.com/FilterDetails.aspx?id=LP02-224R-25
# 
# https://www.semrock.com/FilterDetails.aspx?id=LP02-244RS-25
# 
# 
# 

# ### Tarea 3 (b). Verificación del filtro

# Empleando el dato de la transmitancia (T) a la longitud de onda del
# puntero láser comprobar que dicho filtro evitará el riesgo de
# lesión.
# 
# Para ello vamos a consultar los datos de la transmitancia del filtro seleccionado que aparecen en la página web de Semrock. Seguimos los siguientes pasos:
# 
# 1. Pinchar con el ratón en la página web del filtro seleccionado sobre **ASCII Data**, que se encuentra en la leyenda de la figura (derecha).
# 
# 2. Aparecerán los valores experimentales de la transmitancia. La columna de la izquierda es la longitud de onda en nm y la columna de la derecha es la transmitancia de 0 a 1. 
# 
# 3. Desplazarse hasta encontrar el valor de la transmitancia a la longitud de onda del puntero láser.

# In[2]:


from IPython.display import Image
Image(filename="ejemplofiltro.png")


# Apunta el valor de la transmitancia a la longitud de onda seleccionada
# 
# *  $\lambda$  = 
# 
# * **T** = 
# 
# Empleando el valor de la transmitancia del filtro a la longitud de onda del puntero láser verificar 
# que el filtro evitará el riesgo de daño ocular. Escribir a continuación la estimación realizada.
# 
# * Estimación de la potencia que alcanzará el ojo con el filtro:
# 
# 
# 

# In[ ]:




