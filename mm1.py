from random import random, randint
import math

def exponencial(Lambda):
    return -1/Lambda * math.log(1 - random())

def main():
    n = 100
    t_max = 10_000
    l = 0.5
    mu = 1

    tempos = [0] * n # timestamp a partir do qual cada servidor ficará ocioso

    # o primeiro cliente chega no tempo 0
    servico_primeiro_cliente = exponencial(mu)
    tempos[randint(0, n-1)] = servico_primeiro_cliente
    tempo_no_sistema = servico_primeiro_cliente

    t = 0
    i = 0
    while True:
        t += exponencial(l * n) # timestamp da chegada de um cliente
        
        if t > t_max:
            break

        tempo_servico = exponencial(mu)

        fila_roteada = randint(0, n-1)

        tempo_no_sistema += max(0, tempos[fila_roteada] - t) + tempo_servico

        tempos[fila_roteada] = max(tempos[fila_roteada], t) + tempo_servico

        i += 1
    
    print(f"Tempo médio no sistema: {tempo_no_sistema/i}s")


if __name__ == "__main__":
    main()