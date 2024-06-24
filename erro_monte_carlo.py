import random
import numpy as np

class X():
    def __init__(self, t, d, p) -> None:
        self.t = t
        self.d = d
        self.p = p
        self.instancia = 0
        self.string = ""
    
    def gera_instancia(self):
        erros = 0
        nova_sequencia = True
        for _ in range(self.t):
            if random.random() < self.p:
                self.string += "1"

                if nova_sequencia:
                    erros += 1
                    if erros == self.d:
                        self.instancia += 1
                        erros = 0
                        nova_sequencia = False
            else:
                erros = 0
                self.string += "0"
                nova_sequencia = True
        

    # INCOMPLETO
    def gera_instancia_otimizado(self):
        # IDEIA:
        # p**i é probabilidade de ter i falhas consecutivas a partir do último caracter da sequência
        prob_sequencia_erros_no_final = [self.p**i for i in range(self.d, 0, -1)]
        print(prob_sequencia_erros_no_final)
        
        # print(prob_sequencia_erros_no_final)
        i = 0
        sequencia_atual = 0
        while i < self.t:
            rd = random.random()
            print("alê:", rd)
            erros_no_final = self.d - busca_binaria(prob_sequencia_erros_no_final, 0, self.d, rd)
            print("erros no final:", erros_no_final)
            if sequencia_atual + erros_no_final >= self.d:
                self.instancia += 1
                sequencia_atual = 0
            else:
                sequencia_atual += erros_no_final
            
            if erros_no_final == 0:
                sequencia_atual = 0
            
            # i += erros_no_final if erros_no_final > 0 else 1
            i += self.d


def busca_binaria(lista, esq, dir, n):
    if n < lista[esq]:
        return esq
    if n > lista[dir-1]:
        return dir

    meio = (esq + dir) // 2
    if lista[meio-1] < n <= lista[meio]:
        return meio
    if n < lista[meio]:
        return busca_binaria(lista, esq, meio-1, n)
    else:
        return busca_binaria(lista, meio, dir, n)

def main():
    # days = [2, 3, 4, 5, 10]
    # probs = [0.01, 0.05, 0.1, 0.2, 0.4]

    # for d in days:
    #     for p in probs:
    #         print(d, p, experimento(X(365, d, p), 100_000))

    x = X(70, 5, 0.5)
    x.gera_instancia_otimizado()

    return x.instancia

    

def experimento(x: X, n):
    instancias = []
    # n = 1_000
    for _ in range(n):
        x.gera_instancia()
        instancias.append(x.instancia)

    return sum(instancias) / n

if __name__ == "__main__":
    print(main())