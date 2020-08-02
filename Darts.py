import os
import modo_checklist
import modo_doubledown
import modo_practica
import modo_puntaje


# TODO: implementar graficamente y no por consola
def juego():
    print("Bienvenido")
    print("Que desea jugar?")
    print("1. Modo chupar poto")
    print("2. Modo Focker")
    print("3. Practica")
    print("4. Puntaje")
    print("5. Salir")
    game = int(input())
    if game == 1:
        modo_doubledown.run(solicita_jugadores())
    elif game == 2:
        # TODO: implementar
        modo_checklist.run(solicita_jugadores())
    elif game == 3:
        # TODO: implementar
        modo_practica.run(solicita_jugadores())
    elif game == 4:
        # TODO: implementar
        modo_puntaje.run(solicita_jugadores())
    elif game == 5:
        # TODO: implementar
        os._exit(0)
    else:
        print("Tonto")
        juego()


# TODO: implementar graficamente y no por consola
def solicita_jugadores():
    print("Ingrese el numero de jugadores")
    jugador = int(input())
    lista = [""]
    for i in range(jugador):
        print("Ingrese el nombre del Jugador", str(i + 1))
        aux = input()
        lista.append(aux)
    lista.pop(0)
    return lista


juego()
