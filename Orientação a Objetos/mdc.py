def mdc(a, b):
    divisores_a = [x for x in range(1, a+1) if (x % 2 == 0)]
    divisores_b = [y for y in range(1, b+1) if (y % 2 == 0)]

    if len(divisores_a) >= len(divisores_b):
        tamanho = int(len(divisores_b))
        maior = divisores_a
        menor = divisores_b
    else:
        tamanho = int(len(divisores_a))
        maior = divisores_b
        menor = divisores_a

    divisores = [num for num in menor if num in maior]

    multiplos_a = []
    multiplos_b = []

    for i in range(tamanho):
        if a / divisores[i] == int(a / divisores[i]):
            multiplos_a.append(divisores[i])
        if b / divisores[i] == int(b / divisores[i]):
            multiplos_b.append(divisores[i])

    novo = []
    for num in multiplos_a:
        if num in multiplos_b:
            novo.append(num)

    maior_divisor = novo[len(novo) - 1]

    return maior_divisor
