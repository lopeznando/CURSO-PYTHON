# lista=['texto',10,False]
# #El objeto trabaja con clave y valor
# objeto={"alumno": "jory","edad:":50,"amigos":["mireya","anthony"]}
# objeto["alumno"]="moises"
# objeto["edad"]=25
# objeto["sexo"]="todos los dias"
# print(objeto)

# objeto={}
# objeto['nombre']=input('ingrese su nombre: ')
# objeto['edad']=int(input('ingrese su edad: '))
# objeto['sexo']=input('ingrese su sexo: ')
# print(objeto)

# lista=[]
# while True:
#  objeto={}
#  objeto['nombre']=input('nombre de la mascota: ')
#  objeto['edad']=int(input('edad de la mascota: '))
#  objeto['comidas']=[]
#  while len(objeto['comidas'])<3:
#    comida=input('ingrese la comida favorita: ')
#    objeto['comidas'].append(comida)
#  lista.append(objeto)
#  condicion=input('si desea salir escriba salir: ')
#  if condicion=='salir':
#    break
# print(lista)

# lista=[]
# empresa={}
# empresa['nombre']=input('ingrese nombre de la empresa: ')
# empresa['RUC']=int(input('ingrese su RUC: '))
# empresa['direccion']=input('ingrese su direccion: ')
# empresa['sucursales']=[]
# while len(empresa['sucursales'])<3:
#   sucursal=input('ingrese el nombre de la sucursal: ')
#   empresa['sucursales'].append(sucursal)
# empresa['horario']={}
# empresa['horario']['dia']=input('ingrese el horario del dia: ')
# empresa['horario']['tarde']=input('ingrese el hoarario de la tarde: ')
# print(empresa)

nombre=input('ingrese nombre de la empresa: ')
RUC=int(input('ingrese su RUC: '))
direccion=input('ingrese su direccion: ')
#EJMPLO CON FOR
sucursales=[]
for indice in range(0,3):
    sucursal=input('ingrese la sucursal')
    sucursales.append(sucursal)
#ELEMPLO POR SEPARACION DE COMAS
    sucursales=input('ingrese las sucursales por comas: ').split(',')
    horario_dia=input('ingrese el hoarario de dia: ')
    horario_tarde=input('ingrese el horario de la tarde: ')
empresa={'nombre':nombre,
        'ruc':RUC,
        'direccion':direccion,
        'sucursales':sucursales,
        'horario':{
             'dia':horario_dia,
             'tarde':horario_tarde
        }}
print(empresa)

empresas=[]
while len(empresas)<3:
  nombre=input('ingrese nombre de la empresa: ')
  RUC=int(input('ingrese su RUC: '))
  direccion=input('ingrese su direccion: ')
  sucursales=input('ingrese las sucursales por comas: ').split(',')
  horario_dia=input('ingrese el hoarario de dia: ')
  horario_tarde=input('ingrese el horario de la tarde: ')
  empresa={'nombre':nombre,
          'ruc':RUC,
          'direccion':direccion,
          'sucursales':sucursales,
          'horario':{
              'dia':horario_dia,
              'tarde':horario_tarde
          }}
  empresas.append(empresa)
print(empresas)





