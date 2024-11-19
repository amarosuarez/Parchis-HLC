from juego.juego import Parchis

def test_EstadoCarreraEmpate():
    parchis = Parchis("Amaro", "Ruben")
    parchis.fichaJ1 = 0
    parchis.fichaJ2 = 0
    cadenaEsperada = "Empate"
    
    assert parchis.estadoCarrera() == cadenaEsperada
    
def test_EstadoCarreraJ1():
    parchis = Parchis("Amaro", "Ruben")
    parchis.fichaJ1 = 5
    parchis.fichaJ2 = 3
    cadenaEsperada = "Va ganando Amaro"
    
    assert parchis.estadoCarrera() == cadenaEsperada
        
def test_EstadoCarreraJ2():
    parchis = Parchis("Amaro", "Julian")
    parchis.fichaJ1 = 6
    parchis.fichaJ2 = 8
    cadenaEsperada = "Va ganando Julian"
    
    assert parchis.estadoCarrera() == cadenaEsperada