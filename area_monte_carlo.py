import random, math

def main():
    return monte_carlo(1_000_000)

def monte_carlo(n):
    num_acertos = 0

    for _ in range(n):
        if acerto(ponto_aleatorio()):
            num_acertos += 1
    
    porcentagem_acertos = num_acertos / n

    return porcentagem_acertos * math.pi / 2

def f(x):
    return x / math.tan(x)

def ponto_aleatorio():
    eixo_x = random.random() * math.pi / 2
    eixo_y = random.random()

    return [eixo_x, eixo_y]

def acerto(ponto):
    x, y = ponto

    return y <= f(x)


if __name__ == "__main__":
    print(main())