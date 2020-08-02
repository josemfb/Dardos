import dartsgui2 as gui


def run(lista):
    turnos = ["15", "16", "D", "17", "18", "T", "19", "20", "B"]
    j = gui.Juego(lista, turnos)

    for t in range(len(turnos)):
        for i in range(len(lista)):
            mensaje = "OBJETIVO: " + turnos[t] + "\n---\nIngrese el primer dardo de " + lista[i]
            tirada1 = gui.dardo(j.puntajes, mensaje)
            mensaje = "OBJETIVO: " + turnos[t] + "\n---\nIngrese el segundo dardo de " + lista[i]
            tirada2 = gui.dardo(j.puntajes, mensaje)
            mensaje = "OBJETIVO: " + turnos[t] + "\n---\nIngrese el tercer dardo de " + lista[i]
            tirada3 = gui.dardo(j.puntajes, mensaje)

            # Si es la primera tirada, 40 puntos, si no, lo que se tenia de antes
            if t == 0:
                puntos = 40
            else:
                puntos = j.entrega_puntos(i+1, t)
            j.sumar_puntajes(i + 1, t + 1, puntos)

            # Si le achuntó con algun dardo, da el puntaje
            fallo_todo = True
            if tirada1[0] == turnos[t] or tirada1[1] == turnos[t]:
                fallo_todo = False
                j.sumar_puntajes(i+1, t+1, gui.calcula_puntos(tirada1[0], tirada1[1]))
            if tirada2[0] == turnos[t] or tirada2[1] == turnos[t]:
                fallo_todo = False
                j.sumar_puntajes(i+1, t+1, gui.calcula_puntos(tirada2[0], tirada2[1]))
            if tirada3[0] == turnos[t] or tirada3[1] == turnos[t]:
                fallo_todo = False
                j.sumar_puntajes(i+1, t+1, gui.calcula_puntos(tirada3[0], tirada3[1]))

            # Si fallo todos baja el puntaje a la mitad
            if fallo_todo:
                mitad = puntos // 2
                j.restar_puntajes(i + 1, t + 1, mitad)

    ganadores = j.entrega_mayor(len(turnos))
    j.imprime_consola()
    print(ganadores)
    if len(ganadores) == 1:
        msj = "El ganador es\n" + ganadores[0]
    else:
        msj = "Empate entre\n" + ganadores[0]
        for i in range(1, len(ganadores)-1):
            msj += ", " + ganadores[i]
        msj += " y " + ganadores[len(ganadores)-1]
    gui.dardo(j.puntajes, msj)
