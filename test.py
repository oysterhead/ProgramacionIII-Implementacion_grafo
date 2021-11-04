# from grafo_completo import *
from grafo import *

g = Grafo()

g.borrarGrafo()
assert g.existev(1) == False

g.agregarv(1)
g.agregarv(2)
g.agregarv(3)
assert g.existev(1) == True
assert g.existev(2) == True
assert g.existev(3) == True
g.borrarv(3)
assert g.existev(3) == False
assert g.existea(1, 2) == False
g.agregara(1, 2, 45)
assert g.existea(1, 2) == True
assert g.peso(1, 2) == 45
g.borrara(1, 2)
assert g.existea(1, 2) == False
g.agregara(1, 2, 45)
g.borrarv(2)
assert g.existea(1, 2) == False
assert g.vecinos(0) == []

g.cargardearchivo("grafo1.txt")
assert g.existev(1) == True
assert g.existev(2) == True
assert g.existev(3) == True
#assert g.existev(4) == True
assert g.existev(4) == False
assert g.existea(1, 2) == False
assert g.existea(2, 2) == False

g.cargarEjemplo1()

# Este es para punto estrella
g.cargardearchivo("grafo2.txt")

# calcular dfs y gfs
# assert g.bfs('A') == ['A', 'F', 'G', 'B', 'U', 'X', 'Z', 'D']
# assert g.bfs('D') == ['D']
# assert g.bfs('I') == []

print("Si llegaste acá es por que pasaste todas las pruebas")
