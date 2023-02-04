def mdc(a, b):
    divisores_de_a = [x for x in range(1, a) if (x % 2 == 0)]
    divisores_de_b = [y for y in range(1, b) if (y % 2 == 0)]

    multiplos_de_a = [x for x in range(1, a + 1) if ((a / x) == int(a / x))]
    multiplos_de_b = [y for y in range(1, b + 1) if ((b / y) == int(b / y))]

    novo = [num for num in multiplos_de_a if num in multiplos_de_b]

    maior_divisor_comum = novo[len(novo) - 1]
    return maior_divisor_comum

if __name__ == '__main__':
    from sys import argv
    mdc(int(argv[1]), int(argv[2]))
