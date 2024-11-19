from juego.juego import Parchis

def test_avanzaPosiciones5_2_7():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 5
    Parchis.dado2 = 2
    parchis.fichaJ1 = 0

    posicionEsperada = 7

    assert parchis.avanzaPosiciones(0) == posicionEsperada

def test_avanzaPosiciones5_5_10():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 5
    Parchis.dado2 = 5
    parchis.fichaJ1 = 0

    posicionEsperada = 10
    assert parchis.avanzaPosiciones(0) == posicionEsperada

def test_avanzaPosiciones5_5_7():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 5
    Parchis.dado2 = 5
    parchis.fichaJ2 = 3

    posicionEsperada = 7
    assert parchis.avanzaPosiciones(1) == posicionEsperada

def test_avanzaPosiciones5_3_7():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 5
    Parchis.dado2 = 3
    parchis.fichaJ1 = 6

    posicionEsperada = 6
    assert parchis.avanzaPosiciones(0) == posicionEsperada

def test_avanzaPosiciones6_6_7():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    Parchis.dado1 = 6
    Parchis.dado2 = 6
    parchis.fichaJ1 = 9

    posicionEsperada = 1
    assert parchis.avanzaPosiciones(0) == posicionEsperada

def test_avanzaPosiciones6_6_12():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 15
    Parchis.dado1 = 6
    Parchis.dado2 = 6
    parchis.fichaJ1 = 12

    posicionEsperada = 6
    assert parchis.avanzaPosiciones(0) == posicionEsperada

def test_avanzaPosiciones6_6_17():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 20
    Parchis.dado1 = 6
    Parchis.dado2 = 6
    parchis.fichaJ1 = 17

    posicionEsperada = 11
    assert parchis.avanzaPosiciones(0) == posicionEsperada

def test_avanzaPosiciones6_6_19():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 20
    Parchis.dado1 = 6
    Parchis.dado2 = 6
    parchis.fichaJ2 = 19

    posicionEsperada = 9
    assert parchis.avanzaPosiciones(1) == posicionEsperada