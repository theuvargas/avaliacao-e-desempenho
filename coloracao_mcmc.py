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
    vizinhos = {}
    def __init__(self, vertices):
        for i, v in enumerate(vertices):
            self.vizinhos[i] = v
            self.n += 1
    
    def __str__(self) -> str:
        string = ""
        for i in range(self.n):
            string += f"{i, str(self.vizinhos[i])}, "
        return string[:-2]
        

def main():
    vertices = [
        Vertice([4, 5, 1]),
        Vertice([0, 6, 2]),
        Vertice([1, 7, 3]),
        Vertice([2, 8, 4]),
        Vertice([3, 9, 0]),
        Vertice([0, 7, 8]),
        Vertice([1, 8, 9]),
        Vertice([2, 5, 9]),
        Vertice([3, 5, 6]),
        Vertice([4, 6, 7]),
    ]
    g = Grafo(vertices)
    return g
        
    

if __name__ == "__main__":
    print(main())