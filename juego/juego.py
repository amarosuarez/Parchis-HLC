from random import *

class Parchis:
    TAM_TABLERO = 10
    dado1 = 0
    dado2 = 0

    def __init__(self, nombreJ1, nombreJ2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nombreJ1 = nombreJ1
        self.nombreJ2 = nombreJ2

    def tiraDados():
        Parchis.dado1 = randint(1, 6)
        Parchis.dado2 = randint(1, 6)

    # def pintaTablero(self):
    #     cadena = ""

    #     # Bucle para pintar los números
    #     for i in range(Parchis.TAM_TABLERO + 1):
    #         if (i == 0):
    #             cadena += "\tI\t"
    #         elif (i == Parchis.TAM_TABLERO):
    #             cadena += "F\n"
    #         else:
    #             cadena += str(i) + "\t"

    #     # Concatenamos el nombre del jugador 1
    #     cadena += self.nombreJ1 + "\tI"
    #     for i in range(self.fichaJ1):
    #         cadena += "\t"

    #     # Si la ficha no es igual a 0, pintamos la ficha
    #     if (self.fichaJ1 != 0):
    #         cadena += "O"

    #     # Pintamos un salto de línea
    #     cadena += "\n"

    #     # Concatenamos el nombre del jugador 2
    #     cadena += self.nombreJ2 + "\tI"
    #     for i in range(self.fichaj2):
    #         cadena += "\t"
        
    #     # Si la ficha no es igual a 0, pintamos la ficha
    #     if (self.fichaj2 != 0):
    #         cadena += "O"

    #     return cadena

    def pintaTablero(self):
        cadena = ""

        for i in range(1, 4):
            if i == 2:
                cadena += self.nombreJ1
            elif i == 3:
                cadena += self.nombreJ2
            
            cadena += "\tI"

            for j in range(1, Parchis.TAM_TABLERO):
                cadena += "\t"

                if i == 1:
                    cadena += str(j)
                elif i == 2:
                    if j == self.fichaJ1:
                        cadena += "O"
                elif i == 3:
                    if j == self.fichaJ2:
                        cadena += "O"
                
            cadena += "\tF\n"
        return cadena
    
    def avanzaPosiciones (self, jugador):
        posicion = self.actualizarPosicion(self.fichaJ1 if jugador == 0 else self.fichaJ2)

        if jugador == 0:
            self.fichaJ1 = posicion
        else:
            self.fichaJ2 = posicion

        return posicion
    
    def actualizarPosicion(self, ficha):
        sumaDados = (Parchis.dado1 + Parchis.dado2)
        posicion = sumaDados

        # Si la suma de la posición actual más la suma de los dados es mayor que el tablero, usamos la fórmula para el rebote
        if (ficha + posicion > Parchis.TAM_TABLERO):
            posicion = (Parchis.TAM_TABLERO * 2) - (ficha + posicion)

            # Si la fórmula ha resultado negativa, la corregimos restándole a la suma de los dados el tam tablero y sumando
            # esto a la posicion calculada anteriormente
            if (posicion < 0):
                posicion += (sumaDados - Parchis.TAM_TABLERO)

        return posicion