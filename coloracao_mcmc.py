class Vertice():
    contador = 0
    def __init__(self, vizinhos, cor=None):
        self.id = Vertice.contador
        self.vizinhos = vizinhos
        self.cor = cor

        Vertice.contador += 1

    def __str__(self) -> str:
        return str(self.vizinhos)


class Grafo():
    n = 0
    vertices = {}
    def __init__(self, vertices):
        for v in vertices:
            self.vertices[self.n] = v
            self.n += 1
    
    def __str__(self) -> str:
        string = ""
        for i in range(self.n):
            string += f"{i, str(self.vizinhos[i])}, "
        return string[:-2]
        

def main():

    # estado inicial com os vértices de cores diferentes
    vertices = [
        Vertice([4, 5, 1], 0),
        Vertice([0, 6, 2], 1),
        Vertice([1, 7, 3], 2),
        Vertice([2, 8, 4], 3),
        Vertice([3, 9, 0], 4),
        Vertice([0, 7, 8], 5),
        Vertice([1, 8, 9], 6),
        Vertice([2, 5, 9], 7),
        Vertice([3, 5, 6], 8),
        Vertice([4, 6, 7], 9),
    ]



    g = Grafo(vertices)
    return g
        
def grafo_valido(g: Grafo):
    for i in range(g.n):
        for vizinho in g.vizinhos[i]:
            if 

if __name__ == "__main__":
    print(main())