# Creador: Eduardo Javier Maldonado Acevedo
# Port a python 3 y adaptaciones Matías Bordone
import os
import sys


class Grafo:
    def __init__(self):
        self.grafo = {}

    def cargarEjemplo1(self):  # carga un grafo de ejemplo para probar funciones
        self.grafo = {'A': {'F': 0, 'G': 0},
                      'F': {},
                      'G': {'B': 0, 'U': 0, 'X': 0},
                      'B': {},
                      'U': {'Z': 0, 'D': 0},
                      'X': {},
                      'Z': {},
                      'D': {},
                      }

    def cargarEjemplo2(self):  # carga un grafo de ejemplo para probar funciones
        self.grafo = {'TIJ': {'MTY': 800},
                      'MZT': {'TIJ': 400, 'BJX': 300},
                      'MTY': {'BJX': 700},
                      'BJX': {'SAN': 900, 'TAM': 400, 'MEX': 350},
                      'GDL': {'MZT': 500, 'BJX': 250, 'MEX': 500, 'MTY': 450},
                      'CUN': {'GDL': 650},
                      'MEX': {'CUN': 650, 'MID': 450, 'CH': 50},
                      'TAM': {'MID': 450},
                      'SAN': {'MID': 1200},
                      'MID': {},
                      'CH': {'TAM': 50},
                      }

    def agregarv(self, v):  # agrega un vertice al grado
        if v not in self.grafo:
            self.grafo[v] = {}

    def existev(self, v):  # v -> Bool
        return v in self.grafo

    def existea(self, v, a):
        if v in self.grafo:
            return a in self.grafo[v]

    def borrarv(self, v):  # borra el vertice v del grafo
        if v in self.grafo:
            del self.grafo[v]
            for w in self.vertices():
                if v in self.vecinos(w):
                    del self.grafo[w][v]

    def agregara(self, v, w, p):  # agrega la arista vw al grafo con el peso p (deben existir v y w)
        if v != w and v in self.grafo and w in self.grafo:
            diccionario_vecinos = self.grafo[v]  # diccionario de V con los otros "W"
            diccionario_vecinos[w] = p

    def borrara(self, v, w):  # borra la arista vw
        if v in self.grafo and w in self.grafo:
            del self.grafo[v][w]

    def peso(self, v, w):  # devuelve el peso de la arista vw
        if v in self.grafo and w in self.grafo:
            return self.grafo[v][w]
        else:
            return "Verificar vertices"

    def vecinos(self, v):  # v -> [v]
        if v in self.grafo:
            return list(self.grafo[v].keys())
        else:
            return []

    def nvertices(self):  # devuelve la cantidad de vertices de G
        return len(self.vertices())

    def vertices(self):  # devuelve una lista con los vertices de G
        return list(self.grafo.keys())

    def borrarGrafo(self):  # borra el grafo
        self.grafo.clear()

    def cargardearchivo(self, archivo):  # carga el grafo desde "archivo"
        self.grafo = {}

        def es_entero(variable):
            try:
                int(variable)
                return True
            except:
                return False

        f = open(archivo, 'r')
        n, m = list(f.readline().split())
        for line in f.readlines():
            data = list(line.split())
            if len(data) == 3:
                v1, v2, p = data
            if len(data) == 2:
                v1, v2, p = data, 0
            if es_entero(v1):
                v1 = int(v1)
            if es_entero(v2):
                v2 = int(v2)
            self.agregarv(v1)
            self.agregarv(v2)
            self.agregara(v1, v2, int(p))
        f.close()
        print(self.grafo)

    def GrafoCompleto(self):
        for key, datos in self.grafo.items():
            print(key, datos)
        input("Presione enter para continuar")



if __name__ == "__main__":
    g = Grafo()
    g.cargarEjemplo1()
#    g.seleccion()