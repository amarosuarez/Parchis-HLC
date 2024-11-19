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
    
    def actualizarPosicion(self, ficha):
        sumaDados = (Parchis.dado1 + Parchis.dado2)
        
        # Por defecto, le damos el valor de sumaDados
        posicion = sumaDados

        # Si la suma de la posición actual más la suma de los dados es mayor que el tablero, usamos la fórmula para el rebote
        if (ficha + sumaDados > Parchis.TAM_TABLERO):
            # Caso práctico
            # TAM -> 10
            # Jugador en 6
            # Suma dados -> 8
            # 20 - 14 (6+8) = 6, esta es la posición final
            # Usamos absoluto para los negativos
            posicion = abs((Parchis.TAM_TABLERO * 2) - (ficha + sumaDados))

        return posicion
    
    def estadoCarrera(self):
        cadenaRes = "Empate"
        
        if (self.fichaJ1 > self.fichaJ2):
            cadenaRes = f"Va ganando {self.nombreJ1}"
        elif (self.fichaJ1 < self.fichaJ2):
            cadenaRes = f"Va ganando {self.nombreJ2}"

        return cadenaRes
    
    def esGanador(self):
        cadenaRes = ""

        if (self.fichaJ1 == Parchis.TAM_TABLERO):
            cadenaRes = self.nombreJ1
        elif (self.fichaJ2 == Parchis.TAM_TABLERO):
            cadenaRes = self.nombreJ2

        return cadenaRes