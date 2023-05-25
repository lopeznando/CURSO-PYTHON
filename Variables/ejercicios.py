##Convenciones al nombrar elementos
#A la hora de escribir código, todo tiene nombres: variables, clases, funciones, paquetes, módulos, etc. 
#Es por lo tanto muy importante seguir unas directrices determinadas para que nuestro código 
#sea lo más legible posible. No se nombra igual a una clase que a una función, y tampoco suele ser 
#recomendable usar nombres como a o x ya que aporta poca información. A continuación lo vemos en detalle.

#Eligiendo Nombres
#Antes de nada debemos debemos pensar el nombre que le vamos dar a nuestra variable clase o función. 
# Es importante tener en cuenta lo siguiente:

#Evitar usar palabras reservadas. Si es necesario usar una palabra reservada como class,
#  usar class_ como alternativa.
#Evitar usar l O y I, ya que pueden ser confundidas.
#Usar _variable para especificar uso interno. 
# Por ejemplo from m import * no importaría lo que empieza con _.
#Se puede usar __variable para invocar el name mangling y hacer privadas determinadas variables o métodos.
#Para métodos mágicos usar siempre __init__, pero no son nombres que debemos crear sino reutilizar 
# los que Python nos ofrece.
#Estilos: Camel Case y snake_case
#Supongamos que ya sabemos como vamos a nombrar a nuestra clase, función o variable. 
# Pongamos que queremos llamar a nuestra función “mi función de prueba”. 
# Dado que no podemos utilizar espacios para nombrar variables, hay diferentes alternativas:

#mi_funcion_de_prueba
#MiFuncionDePrueba
#MIFUNCIONDEPRUEBA
#MI_FUNCION_DE_PRUEBA
#mifunciondeprueba
#Algunas de estas alternativas son conocidas como Camel Case o snake_case en el mundo de la programación.
#  Pues bien, Python define cómo nombrar a cada tipo de la siguiente manera:

#Funciones: Letras en minúscula separadas por barra baja: funcion, mi_funcion_de_prueba.
#Variables: Al igual que las funciones: variable, mi_variable.
#Clases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba.
#Métodos: Al igual que las funciones, usar snake case: metodo, mi_metodo.
#Constantes: Nombrarlas usando mayúsculas y separadas por barra bajas: UNA_CONSTANTE, OTRA_CONSTANTE.
#Módulos: Igual que las funciones: modulo.py, mi_modulo.py.
#Paquetes: En minúsculas pero sin separar por barra bajas: packete, mipaquete
#En el siguiente fragmento podemos ver su uso.

# mi_script.py
#CONSTANTE_GLOBAL = 10

#class MiClase():
 #   def mi_primer_metodo(self, variable_a, variable_b):
  #      return (variable_a + variable_b) / CONSTANTE_GLOBAL


#mi_objeto = MiClase()
#print(mi_objeto.mi_primer_metodo(5, 5)).
# COMO DECLARAR CONSTANTES EN PYTHON
#En Python las constantes no existen. Para guardar un valor constante se utiliza una variable pero por
#convencion se utiliza las letras mayusculas para darle nombre a dicha variable. 
#3sí, si al programar nos encontramos con un identificador en mayúsculas sabremos que no debe ser alterado.
