
# Atributos
# 1. Numerador; 2. Denominador

# Métodos
# somar; subtrair; multiplicar; dividir; inverter; negar; simplificar

from mdc import mdc

class Fração:
    def __init__(self, numer, denom):
        self.numerador = numer

        if denom == 0:
            self.denominador = 1
        else:
            self.denominador = denom

    def mdc_(self):
        return mdc(self.numerador, self.denominador)

    def somar(self, outra):
        if self.denominador == outra.denominador:
            denom = self.denominador
            numer = self.numerador + outra.numerador
        else:
            numer = self.numerador*outra.denominador + self.denominador*outra.numerador
            denom = self.denominador*outra.denominador
        return Fração(numer, denom)

    def subtrair(self, outra):
        return self.somar(outra.negar())

    def multiplicar(self, outra):
        numer = self.numerador * outra.numerador
        denon = self.denominador * outra.denominador
        return Fração(numer, denon)

    def dividir(self, outra):
        return self.multiplicar(outra.inverter())

    def inverter(self):
        return Fração(self.denominador, self.numerador)

    def negar(self):
        return Fração(-self.numerador, self.denominador)

    def mdc(self):
        return mdc(self.numerador, self.denominador)

    def simplificar(self):
        if self.denominador % self.numerador == 0:
            numerador = 1
            denominador = int(self.denominador / self.numerador)
        else:
            if self.denominador >= self.numerador:
                maior = self.denominador
                menor = self.numerador
            else:
                maior = self.numerador
                menor = self.denominador

            if maior % menor == 0 or menor % maior == 0:
                while (maior % menor != 0) and menor != 0: menor -= 1
                numerador = int(menor / 2)
                denominador = int(maior / maior)
            else:
                numerador = int(self.numerador / Fração.mdc(self))
                denominador = int(self.denominador / Fração.mdc(self))

        return Fração(numerador, denominador)

    def __repr__(self):
        numerador = self.numerador
        denominador = self.denominador

        if len(str(numerador)) > len(str(denominador)):
            tamanho = len(str(numerador)) + 2
        else:
            tamanho = len(str(denominador)) + 2

        underlines = tamanho * '-'

        if numerador < 0 and denominador >= 1:
            representação = f'{numerador:^{tamanho}}\n{underlines}\n{denominador:^{tamanho + 1}}'
        elif denominador < 0 and numerador >= 1:
            representação = f'{numerador:^{tamanho + 1}}\n{underlines}\n{denominador:^{tamanho}}'
        else:
            representação = f'{numerador:^{tamanho}}\n{underlines}\n{denominador:^{tamanho}}'

        return representação

if __name__ == '__main__':
    a = Fração(3, 2)
    b = Fração(6, 5)
    resultado = Fração.somar(a, b)
    print(f'[Soma]\n{resultado}', end='\n\n')

    c = Fração(3, 6)
    d = Fração(1, 6)
    resultado = Fração.subtrair(c, d)
    print(f'[Subtração]\n{resultado}', end='\n\n')

    e = Fração(3, 5)
    f = Fração(12, 5)
    resultado = Fração.multiplicar(e, f)
    print(f'[Multiplicação]\n{resultado}', end='\n\n')

    g = Fração(2, 3)
    h = Fração(7, 5)
    resultado = Fração.dividir(g, h)
    print(f'[Divisão]\n{resultado}', end='\n\n')

    i = Fração(4, 7)
    resultado = Fração.inverter(i)
    print(f'[Inversão]\n{resultado}', end='\n\n')

    j = Fração(6, 2)
    resultado = Fração.negar(j)
    print(f'[Negação]\n{resultado}', end='\n\n')

    k = Fração(24, 32)
    resultado = Fração.simplificar(k)
    print(f'[Simplificação]\n{resultado}')
