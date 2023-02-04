def mdc(a, b):
    divisores_de_a = [x for x in range(1, a) if (x % 2 == 0)]
    divisores_de_b = [y for y in range(1, b) if (y % 2 == 0)]

    if len(divisores_de_a) >= len(divisores_de_b):
        tamanho = int(len(divisores_de_b))
    else:
        tamanho = int(len(divisores_de_a))

    multiplos_de_a = []
    multiplos_de_b = []

    for num in range(1, tamanho):
        if a / num == int(a / num):
            multiplos_de_a.append(num)
        if b / num == int(b / num):
            multiplos_de_b.append(num)

    novo = [num for num in multiplos_de_a if num in multiplos_de_b]

    maior_divisor_comum = novo[len(novo) - 1]
    return maior_divisor_comum

if __name__ == '__main__':
    from sys import argv
    mdc(int(argv[1]), int(argv[2]))
