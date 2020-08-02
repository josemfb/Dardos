from tkinter import *


def dardo(puntajes_actuales=None, mensaje=None):

    # Se invoca si se hace click
    if puntajes_actuales is None:
        puntajes_actuales = []

    def check_pos(event):
        global valor
        rect = canvas.find_overlapping(event.x, event.y, event.x, event.y)
        valor = canvas.gettags(rect[len(rect) - 1])[0]
        board.destroy()

    # Establece el tamaño de las celdas de la tabla de puntajes
    alto_c = 40
    ancho_c = 75
    margen = (750 - (ancho_c * (len(puntajes_actuales) + 1))) / 2

    # Crea un canvas
    board = Tk()
    board.attributes('-fullscreen', True)
    board.title("Tablero")
    ancho_board = 700
    if puntajes_actuales:
        ancho_board += margen * 2 + ancho_c * len(puntajes_actuales)
    alto_board = 700
    canvas = Canvas(board, width=ancho_board, height=alto_board)
    canvas.pack()

    # Crea los numeros
    posiciones = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14,
                  11, 8, 16, 7, 19, 3, 17, 2, 15, 10]
    k = 0
    saltos = "\n" * 24
    for i in posiciones:
        coord = 350, 350
        canvas.create_text(coord, angle=-90 + (k * 18), text=str(i) + saltos, font=("Sans", 18))
        k += 1

    # Crea el tablero de dardos
    for i in range(20):
        color1 = "green"
        color2 = "white"
        if i % 2 == 1:
            color1 = "red"
            color2 = "black"
        # dobles
        coord = 50, 50, 650, 650
        canvas.create_arc(coord, start=-9+18*i, extent=18, fill=color1, tags=(str(posiciones[i])+"D"))
        # primera zona simple
        coord = 80, 80, 620, 620
        canvas.create_arc(coord, start=-9+18*i, extent=18, fill=color2, tags=(str(posiciones[i])+"S"))
        # triples
        coord = 185, 185, 515, 515
        canvas.create_arc(coord, start=-9+18*i, extent=18, fill=color1, tags=(str(posiciones[i])+"T"))
        # segunda zona simple
        coord = 215, 215, 485, 485
        canvas.create_arc(coord, start=-9+18*i, extent=18, fill=color2, tags=(str(posiciones[i])+"S"))
        # bullseye
        coord = 320, 320, 380, 380
        canvas.create_oval(coord, fill="green", tags="BS")
        coord = 335, 335, 365, 365
        canvas.create_oval(coord, fill="red", tags="BD")

    # Si se entregan puntajes se crea la tabla
    if puntajes_actuales:
        # lineas verticales
        largo_linea = alto_c * (len(puntajes_actuales[0]) + 1)
        for k in range(0, len(puntajes_actuales) + 1):
            grosor = 1
            if k == 0 or k == len(puntajes_actuales):
                grosor = 3
            coord = 700 + margen + ancho_c * k, alto_c, 700 + margen + ancho_c * k, largo_linea
            canvas.create_line(coord, width=grosor)

        # lineas horizontales
        largo_linea = 700 + margen + ancho_c * (len(puntajes_actuales))
        for k in range(0, len(puntajes_actuales[0]) + 2):
            grosor = 1
            if k == 1 or k == len(puntajes_actuales[0]) + 1:
                grosor = 3
            coord = 700 + margen, alto_c * k, largo_linea, alto_c * k
            canvas.create_line(coord, width=grosor)

        # textos
        for i in range(0, len(puntajes_actuales)):
            for j in range(0, len(puntajes_actuales[i])):
                coord_x = 700 + margen + ancho_c * (i + 0.5)
                coord_y = + alto_c * (j + 1.5)
                coord = coord_x, coord_y
                canvas.create_text(coord, text=puntajes_actuales[i][j], font=("Sans", 12))

    # Si se entrega mensaje se presenta
    if mensaje:
        coord_x = 700 + margen + ancho_c * len(puntajes_actuales) / 2
        coord_y = 100 + alto_c * len(puntajes_actuales[0])
        coord = coord_x, coord_y

        mensaje_aux = [mensaje, "", "", ""]

        corte = mensaje.find(" ", 20)
        if mensaje.find("\n") > 0:
            corte = mensaje.find("\n")
        if len(mensaje) > 20 and corte > 0:
            mensaje_aux[1] = mensaje[corte + 1:len(mensaje)]
            mensaje_aux[0] = mensaje[0:corte]
            corte = mensaje_aux[1].find(" ", 20)
            if mensaje_aux[1].find("\n") > 0:
                corte = mensaje_aux[1].find("\n")
            if len(mensaje_aux[1]) > 20 and corte > 0:
                mensaje_aux[2] = mensaje_aux[1][corte + 1:len(mensaje_aux[1])]
                mensaje_aux[1] = mensaje_aux[1][0:corte]
                corte = mensaje_aux[2].find(" ", 20)
                if mensaje_aux[2].find("\n") > 0:
                    corte = mensaje_aux[2].find("\n")
                if len(mensaje_aux[2]) > 20 and corte > 0:
                    mensaje_aux[3] = mensaje_aux[2][corte + 1:len(mensaje_aux[2])]
                    mensaje_aux[2] = mensaje_aux[2][0:corte]

        canvas.create_text(coord, text=mensaje_aux[0], fill="green", font=("Sans", 24))
        coord = coord_x, coord_y + 40
        canvas.create_text(coord, text=mensaje_aux[1], fill="green", font=("Sans", 24))
        coord = coord_x, coord_y + 80
        canvas.create_text(coord, text=mensaje_aux[2], fill="green", font=("Sans", 24))
        coord = coord_x, coord_y + 120
        canvas.create_text(coord, text=mensaje_aux[3], fill="green", font=("Sans", 24))

    # Hace que al hacer click se llame a check_pos
    canvas.bind("<Button-1>", check_pos)

    # Mantiene el tablero abierto
    mainloop()

    # Retorna una tupla (num, mult)
    return valor[0:len(valor)-1], valor[len(valor)-1]


def puntos(puntajes_actuales=None, mensaje=None):
    tirada = dardo(puntajes_actuales, mensaje)
    return calcula_puntos(tirada[0], tirada[1])


def calcula_puntos(num, mult):
    # Calcula el valor del lanzamiento
    resultado_multiplicador = 1
    if num == "B":
        resultado_posicion = 25
    else:
        resultado_posicion = int(num)

    if mult == "S":
        resultado_multiplicador = 1
    elif mult == "D":
        resultado_multiplicador = 2
    elif mult == "T":
        resultado_multiplicador = 3

    return resultado_posicion * resultado_multiplicador


class Juego:

    def __init__(self, lista_jugadores, lista_de_juego):
        self.puntajes = []
        aux = [""] + lista_de_juego
        self.puntajes.append(aux)
        # Añade una fila por jugador, en blanco los puntajes
        for j in lista_jugadores:
            auxiliar = [j]
            for _ in lista_de_juego:
                auxiliar.append("")
            self.puntajes.append(auxiliar)

    def entrega_puntos(self, jug, pos):
        return int(self.puntajes[jug][pos])

    def actualizar_puntajes(self, jug, pos, ptje):
        self.puntajes[jug][pos] = ptje

    def sumar_puntajes(self, jug, pos, ptje):
        if not self.puntajes[jug][pos]:
            self.puntajes[jug][pos] = 0
        self.puntajes[jug][pos] += ptje

    def restar_puntajes(self, jug, pos, ptje):
        if not self.puntajes[jug][pos]:
            self.puntajes[jug][pos] = 0
        self.puntajes[jug][pos] -= ptje

    def entrega_mayor(self, pos):
        retorno = [self.puntajes[1][0]]
        posiciones = [1]
        for i in range(2, len(self.puntajes)):
            if self.puntajes[i][pos] == self.puntajes[posiciones[0]][pos]:
                posiciones.append(i)
                retorno.append(self.puntajes[i][0])
            elif self.puntajes[i][pos] > self.puntajes[posiciones[0]][pos]:
                posiciones = [i]
                retorno = [self.puntajes[i][0]]
        return retorno

    def entrega_menor(self, pos):
        retorno = [self.puntajes[1][0]]
        posiciones = [1]
        for i in range(2, len(self.puntajes)):
            if self.puntajes[i][pos] == self.puntajes[posiciones[0]][pos]:
                posiciones.append(i)
                retorno.append(self.puntajes[i][pos-1])
            elif self.puntajes[i][pos] < self.puntajes[posiciones[0]][pos]:
                posiciones = [i]
                retorno = [self.puntajes[i][pos-1]]
        return retorno

    def imprime_consola(self):
        for q in range(0, len(self.puntajes[0])):
            aux = []
            for i in range(0, len(self.puntajes)):
                aux.append(self.puntajes[i][q])
            print(aux)


if __name__ == "__main__":
    print("Tonto, este modulo es para importarlo, no para abrirlo")
