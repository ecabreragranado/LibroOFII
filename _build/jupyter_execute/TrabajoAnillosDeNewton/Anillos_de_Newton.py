#!/usr/bin/env python
# coding: utf-8

# # Caracterización de una lente oftálmica mediante la técnica de los Anillos de Newton

# ####  Consultar el manual de uso de los cuadernos interactivos (notebooks) que se encuentra disponible en  el Campus Virtual

# ### Grupo de trabajo

# En esta celda los integrantes del grupo: *modificar el texto*
# 
# * Juan Antonio Fernández 
# * Alberto Pérez
# * Juan 
# 
# Incluir la dirección de correo electrónico del responsable del grupo

# ## Tarea 1. Figura con el patrón de interferencias (Anillo de Newton)

# Estudiaremos como se determina el radio de curvatura de un lente plano-convexa empleando la técnica interferométrica conocida como Anillos de Newton. Para ello vamos a simular nuestra lente plano-convexa empleando el sistema de dos superficies proporcionado por el profesor. 
# 
# Vamos a mostrar la imagen con el patrón de interferencias medido. Para ello es necesario subir a vuestra cuenta de SageMath la imagen que habéis tomado. Si pincháis en "New" (en la parte superior izquierda de la página), podeís arrastrar directamente vuestra imagen al "Drop Files". 
# 
# En la siguiente celda de código escribir el nombre de la imagen para que se pueda mostrar. El texto que aparece después del símbolo # son comentarios. Una vez ejecutada vuestra imagen debe aparecer a continuación. Si no es así, por favor contactad con el profesor.

# In[1]:


# MODIFICAR EL NOMBRE DEL FICHERO IMAGEN. LUEGO EJECUTAR
########################################################

nombre_fichero_imagen="prueba.jpg"  # Incluir el nombre completo con extensión del fichero imagen dentro de las comillas                

# DESDE AQUÍ NO TOCAR 
##############################################################################################################################
get_ipython().run_line_magic('pylab', 'inline')
from IPython.core.display import Image,display
Image(filename=nombre_fichero_imagen,width=600)


# ## Tarea 2. Determinar el radio de los anillos oscuros

# Empleando la imagen anterior vamos a medir el diámetro de los anillos oscuros. Se pueden medir directamente en la pantalla del ordenador o imprimiendo la figura en una hoja de papel. Escribir en la siguiente tabla el diámetro de los anillos oscuros en las unidades indicadas (**añadir tantas filas como sean necesarias manteniendo el formato**) y explicar como se han medido (pantalla del ordenador, papel).
# 
#  Número del anillo | Diámetro del anillo (mm)
# -------| ------
#  1      |   3.6
#  2      |   --
#  3      |   --
#  4      |   --
# 
#  
# * Explicación del proceso
# 
# (Escribir aquí la explicación del proceso)
# 
# ---
# 
# Estos diámetros tienen el aumento $\beta$ correspondiente al sistema óptico de medida y al tamaño de la figura en la pantalla del ordenador o en la hoja de papel. Teniendo en cuenta la escala de referencia que aparece en la figura calcular el aumento $\beta$ de los diámetros medidos (*escribir el valor*). Esta medida debe realizarse en las mismas condiciones que las de los diámetros.
# 
# * $\beta$ =
# 
# Usando dicho aumento podemos obtener el radio real de los anillos oscuros.
# 
# Radio = (Diámetro / 2) / $\beta$     
# 
# Escribir otra tabla con los valores finales de los radios de los anillos oscuros en las unidades indicadas (como en la tabla anterior, añadir tantas filas como sean necesarias mantiendo el formato).
# 
# Número | Radio real (mm)
# ---| ---
#  1      |   --     
#  2      |   --      
#  3      |   --

# ## Tarea 3. Análisis de los datos. Ajuste lineal de los radios de los anillos oscuros

# Empleando los radios de los anillos oscuros vamos a representar gráficamente el radio al cuadrado en función del número del anillo oscuro. Dicha representación debería darnos una dependencia lineal cuya pendiente es el radio de curvatura multiplicado por la longitud de onda de la luz empleada en el experimento, es decir, 
# 
# $$\text{pendiente} =  \lambda  \text{R }$$
# 
# Como hemos empleando luz blanca para realizar el experimento vamos a emplear una longitud de onda central del visible: $\lambda$=550 nm.
# 
# En la siguiente celda de código se introducen los radios de los anillos oscuros obtenidos en el apartado anterior (en milímetros). Introducir los valores separados por comas. El código permite representar los datos y realizar un ajuste lineal para obtener el valor de la pendiente (aparece escrito en la figura). Dicho valor tendrá las unidades de los radios al cuadrado, es decir, mm$^2$.

# In[2]:


# MODIFICAR LOS RADIOS DE LOS ANILLOS OSCUROS. LUEGO EJECUTAR
########################################################

radio=array([2.5, 6, 9])  # separar los valores con comas (usar el punto como símbolo decimal)

# DESDE AQUÍ NO TOCAR
##############################################################################################################################
get_ipython().run_line_magic('pylab', 'inline')
m=linspace(1,size(radio),size(radio)) # Vector con los números de los anillos
radio2=radio*radio # Vector con los radios de los anillos al cuadrado
a,b = polyfit(m,radio2,1) # Ajuste de los datos a una recta donde a es la pendiente y b la ordenada en el origen

plot(m,radio2,'o',m,a*m+b,'-',lw=2) 
xlabel('Numero del anillo')
ylabel('Radio$^2$ (mm$^2$)') # Escribimos los nombres de los ejes
te = "pendiente = %f mm$^2$" % a;title(te); # Se muestra el valor de la pendiente;


# Empleando el valor de la pendiente y la longitud de onda calcular el radio de curvatura de la lente 
# 
# * $R$=  (*incluir las unidades*)
