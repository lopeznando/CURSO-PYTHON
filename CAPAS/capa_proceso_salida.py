import capa_entrada
while True:
    
    capa_entrada.jugador1
    capa_entrada.jugador2

    if capa_entrada.jugador1 == capa_entrada.jugador2:
            print("Empate!")
    elif capa_entrada.jugador1 == "piedra":
        if capa_entrada.jugador2 == "papel":
                print("¡Jugador 2 gana! Papel envuelve piedra.")
        else:
                print("¡Jugador 1 gana! Piedra rompe tijera.")
    elif capa_entrada.jugador1 == "papel":
            if capa_entrada.jugador2 == "tijera":
                print("¡Jugador 2 gana! Tijera corta papel.")
            else:
                print("¡Jugador 1 gana! Papel envuelve piedra.")
    elif capa_entrada.jugador1 == "tijera":
            if capa_entrada.jugador2 == "piedra":
                print("¡Jugador 2 gana! Piedra rompe tijera.")
            else:
                print("¡Jugador 1 gana! Tijera corta papel.")
    else:
            print("Opción no válida. Por favor, elige piedra, papel o tijera.")

    continuar = input("¿Quieren jugar otra vez? (si/no): ")
    if continuar.lower() != "s":
        break