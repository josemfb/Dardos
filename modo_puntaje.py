import dartsgui2 as gui


def run(lista):
    turnos = ["Ptje."]
    j = gui.Juego(lista, turnos)

    # TODO: implementar gráficamente
    print("Ingrese hasta que puntaje quiere jugar")
    print("Normalmente es 301 o 501 puntos")
    max = int(input())
    for i in range(1, len(lista)+1):
        j.actualizar_puntajes(i, 1, max)

    alguien_gano = False

    while True:
        for i in range(1, len(lista)+1):
            mensaje = "Ingrese el primer dardo de " + lista[i - 1]
            tirada = gui.dardo(j.puntajes, mensaje)
            j.restar_puntajes(i, 1, gui.calcula_puntos(tirada[0], tirada[1]))
            if j.entrega_puntos(i, 1) <= 0:
                alguien_gano = True
                break
            mensaje = "Ingrese el segundo dardo de " + lista[i - 1]
            tirada = gui.dardo(j.puntajes, mensaje)
            j.restar_puntajes(i, 1, gui.calcula_puntos(tirada[0], tirada[1]))
            if j.entrega_puntos(i, 1) <= 0:
                alguien_gano = True
                break
            mensaje = "Ingrese el tercer dardo de " + lista[i - 1]
            tirada = gui.dardo(j.puntajes, mensaje)
            j.restar_puntajes(i, 1, gui.calcula_puntos(tirada[0], tirada[1]))
            if j.entrega_puntos(i, 1) <= 0:
                alguien_gano = True
                break
        if alguien_gano:
            break

    ganadores = j.entrega_menor(len(turnos))
    msj = "El ganador es\n" + ganadores[0]
    gui.dardo(j.puntajes, msj)
