import entrada_datos
while len (entrada_datos.lista)<5:
    dato=input('ingresa un dato: ')
    entrada_datos.lista.append(dato)
for texto in range(0,len(entrada_datos.lista)):
  if entrada_datos.lista[texto]=='disco':
     palabra=entrada_datos.lista[texto]
     indice=texto
     