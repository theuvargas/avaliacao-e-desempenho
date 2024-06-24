import random

def main():
    clausulas = [
        [True, False, True, True],
        [False, False, True, None],
        [False, None, None, False],
        [None, True, True, False],
        [False, True, True, None]
    ]

    return countDNF_monte_carlo(100_000, clausulas)

# calcula a cardinalidade de todos os conjuntos Qi,
# isto é, o tamanho dos conjuntos que satisfazem a clausula i
def calcula_tamanhos(clausulas):
    tamanhos = []
    for c in clausulas:
        contador = 0
        for var in c:
            if var is not None:
                contador += 1
        tamanhos.append(2**(len(c) - contador))
    return tamanhos

def countDNF_monte_carlo(t, clausulas):
    cardinalidades = calcula_tamanhos(clausulas)
    soma = sum(cardinalidades)

    acertos = 0
    for _ in range(t):
        i = sorteia_indice(cardinalidades, soma)
        instancia = sorteia_instancia(clausulas[i])

        if acerto(i, instancia):
            acertos += 1

    return acertos/t * soma

# sorteia uma instância das variáveis que satisfaçam a cláusula dada
def sorteia_instancia(clausula):
    conjunto = []
    for c in clausula:
        if c is not None:
            conjunto.append(c)
        else:
            conjunto.append(random.random() < 0.5)
    return conjunto

# sorteia qual conjunto Qi será amostrado, com o peso de Qi dado por |Qi|
def sorteia_indice(cardinalidades, soma):
    cumsum = [sum(cardinalidades[:i+1])/soma for i in range(len(cardinalidades))]
    rand = random.random()

    for i in range(len(cardinalidades)):
        if rand <= cumsum[i]:
            return i

# verifica se a instância dada pertence a S*, o que inclui verificar se
# ela satisfaz a i-ésima cláusula e se ela não satisfaz nenhuma cláusula
# anterior j < i
def acerto(i, instancia):
    c = [c1, c2, c3, c4, c5]

    if not c[i](*instancia):
        return False
    for j in range(i):
        if c[j](*instancia):
            return False
        
    return True

def c1(x1, x2, x3, x4):
    return x1 and not x2 and x3 and x4

def c2(x1, x2, x3, x4):
    return not x1 and not x2 and x3

def c3(x1, x2, x3, x4):
    return not x1 and not x4

def c4(x1, x2, x3, x4):
    return x2 and x3 and not x4

def c5(x1, x2, x3, x4):
    return not x1 and x2 and x3

if __name__ == "__main__":
    print(main())