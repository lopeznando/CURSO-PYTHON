# def miObjeto(**valores):
#     nuevoObjeto={
#         "nombre":valores["a"],
#         "apellido":valores["b"],
#         "edad":"",
#         "sexo":"",
#         "direccion":""
#     }
#     return nuevoObjeto
# print(miObjeto(a="jose",b="alvarez"))

# lista=[2,5,8,4,2]
# def sumaNumeros(arrayNumeros):
#     totalSuma=0
#     for numero in arrayNumeros:
#         totalSuma += numero
# print(sumaNumeros(lista))

# lista=[2,5,0,4,1]
# def sumaNumeros(arrayNumeros):
#     print(sumaNumeros(lista))
#     def numeroMenor(arrayNumeros):
#         menor=arrayNumeros[0]
#         for numero in arrayNumeros:
#             if numero < menor:
#                 menor=numero
#         return menor
#     print(numeroMenor(lista))

# lista=[2,5,0,4,1]
# def sumaNumeros(arrayNumeros):
#  print(sumaNumeros(lista))
# def numeroMenor (arrayNumeros):
#  print(numeroMenor(lista))
# def numeroMayor (arrayNumeros):
#     mayor=arrayNumeros[0]
#     for numero in arrayNumeros:
#         if numero > mayor:
#             mayor=numero
#             return mayor
#         print(numero mayor(lista))

listaNombres=["jory","orlando","yadira"]
edades=[50,15,10]
def objeto(listaNombres,edades):
    lista=[]
    for indice,objet in enumerate(listaNombres):
        lista.append({"nombre": objet,"edad": edades[indice],"completo":f"{objet} {edades[indice]}"})
    return lista

print(objeto(listaNombres,edades))
















