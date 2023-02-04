def mdc(a, b):
    divisores_de_a = [x for x in range(1, a+1) if (x % 2 == 0)]
    divisores_de_b = [y for y in range(1, b+1) if (y % 2 == 0)]

    if len(divisores_de_a) >= len(divisores_de_b):
        # tamanho = int(len(divisores_de_b))
        maior = divisores_de_a
        menor = divisores_de_b
    else:
        # tamanho = int(len(divisores_de_a))
        maior = divisores_de_b
        menor = divisores_de_a
    tamanho = int(len(menor))

    divisores = [num for num in menor if num in maior]

    multiplos_de_a = []
    multiplos_de_b = []

    for i in range(tamanho):
        if a / divisores[i] == int(a / divisores[i]):
            multiplos_de_a.append(divisores[i])
        if b / divisores[i] == int(b / divisores[i]):
            multiplos_de_b.append(divisores[i])

    novo = []
    for num in multiplos_de_a:
        if num in multiplos_de_b:
            novo.append(num)

    maior_divisor = novo[len(novo) - 1]

    return maior_divisor

if __name__ == '__main__':
    from sys import argv
    mdc(int(argv[1]), int(argv[2]))
