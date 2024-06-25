import random
from typing import Dict, List

class Vertice():
    contador = 0
    def __init__(self, vizinhos: List[int], cor=None):
        self.id = Vertice.contador
        self.vizinhos = vizinhos
        self.cor: int = cor

        Vertice.contador += 1

    def __str__(self) -> str:
        return str(self.vizinhos)

        
def constroi_grafo(vertices: List[Vertice]):
    g = {}
    for i in range(len(vertices)):
        g[i] = vertices[i]

    return g

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

    g = constroi_grafo(vertices)

    for _ in range(100_000):
        #g = transiciona_uniforme(g)
        g = transiciona_menores(g)

    return conta_cores(g)

def conta_cores(g: Dict[int, Vertice]):
    conjunto_cores = set()
    for i in range(len(g)):
        conjunto_cores.add(g[i].cor)
    return len(conjunto_cores)

def transiciona_menores(g: Dict[int, Vertice]):
    id_vertice = random.randint(0, len(g)-1)
    
    cor_antiga = g[id_vertice].cor
    qtd_cores_antiga = conta_cores(g)

    nova_cor = random.choice([i for i in range(len(g)) if i != id_vertice])

    g[id_vertice].cor = nova_cor

    if not coloracao_valida(g):
        g[id_vertice].cor = cor_antiga
        return g
    
    qtd_cores_nova = conta_cores(g)

    if qtd_cores_nova <= qtd_cores_antiga:
        return g
    else:
        if random.random() < 0.9:
            return g
    
    g[id_vertice].cor = cor_antiga
    return g

def transiciona_uniforme(g: Dict[int, Vertice]):
    id_vertice = random.randint(0, len(g)-1)
    nova_cor = random.choice([i for i in range(len(g)) if i != id_vertice])    

    cor_antiga = g[id_vertice].cor
    g[id_vertice].cor = nova_cor

    if coloracao_valida(g):
        return g
    
    g[id_vertice].cor = cor_antiga
    return g


def coloracao_valida(g: Dict[int, Vertice]) -> bool:
    """
    Diz se um grafo possui coloração válida
    """

    for i in range(len(g)):
        for vizinho in g[i].vizinhos:
            if g[i].cor == g[vizinho].cor:
                return False
    
    return True

if __name__ == "__main__":
    print(main())