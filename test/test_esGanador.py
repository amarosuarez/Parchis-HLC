from juego.juego import Parchis

def test_esGanadorN():
    parchis = Parchis("Amaro", "Ruben")
    parchis.fichaJ1 = 0
    parchis.fichaJ2 = 0
    cadenaEsperada = ""
    
    assert parchis.esGanador() == cadenaEsperada

def test_esGanadorJ1():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 20
    parchis.fichaJ1 = 20
    parchis.fichaJ2 = 10
    cadenaEsperada = "Amaro"
    
    assert parchis.esGanador() == cadenaEsperada

def test_esGanadorJ2():
    parchis = Parchis("Amaro", "Ruben")
    Parchis.TAM_TABLERO = 10
    parchis.fichaJ1 = 0
    parchis.fichaJ2 = 10
    cadenaEsperada = "Ruben"
    
    assert parchis.esGanador() == cadenaEsperada

def test_esGanadorN1():
    parchis = Parchis("Amaro", "Ruben")
    parchis.fichaJ1 = 5
    parchis.fichaJ2 = 5
    cadenaEsperada = ""
    
    assert parchis.esGanador() == cadenaEsperada

def test_esGanadorJ1():
    parchis = Parchis("Mario", "Ruben")
    Parchis.TAM_TABLERO = 20
    parchis.fichaJ1 = 20
    parchis.fichaJ2 = 0
    cadenaEsperada = "Mario"
    
    assert parchis.esGanador() == cadenaEsperada

def test_esGanadorJ2():
    parchis = Parchis("Amaro", "Pablo")
    Parchis.TAM_TABLERO = 15
    parchis.fichaJ1 = 0
    parchis.fichaJ2 = 15
    cadenaEsperada = "Pablo"
    
    assert parchis.esGanador() == cadenaEsperada