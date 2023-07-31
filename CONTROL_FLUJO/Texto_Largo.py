frutas=[]
indice=1
while len(frutas)<5:
    nuevaFruta=input('ingresa una fruta: ')
    for fruta in frutas:
       if len(nuevaFruta) == len(fruta):
        print('misma longitud ingresa otro')
    if nuevaFruta in frutas:
        print('esta fruta existe ingresa otro')
    else:
        frutas.append(nuevaFruta)

def textoLargo(array):
    longitudTexto=0
    mostrarFruta=''
    for index in range(0,len(array)):
      if len(array[index]) >longitudTexto:
          longitudTexto=len(array[index])
          mostrarFruta=array[index]
    return mostrarFruta
print(f"""el texto largo se encuentra en el indice, {indice}
y el texto largo es {textoLargo(frutas)}
""")
