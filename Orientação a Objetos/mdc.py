def mdc(a, b):
    multiplos_de_a = [x for x in range(1, a + 1) if ((a / x) == int(a / x))]
    multiplos_de_b = [y for y in range(1, b + 1) if ((b / y) == int(b / y))]

    novo = [num for num in multiplos_de_a if num in multiplos_de_b]

    maior_divisor_comum = novo[len(novo) - 1]
    return maior_divisor_comum

if __name__ == '__main__':
    from sys import argv
    mdc(int(argv[1]), int(argv[2]))
