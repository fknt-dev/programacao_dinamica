
# Atributos
# 1. Numerador; 2. Denominador

# Métodos
# somar; subtrair; multiplicar; dividir; inverter; negar; simplificar

class Fração:
    def __init__(self, numer, denom):
        self.numerador = numer

        if denom == 0:
            self.denominador = 1
        else:
            self.denominador = denom

    def somar(self, outra):
        if self.denominador == outra.denominador:
            denom = self.denominador
            numer = self.numerador + outra.numerador
            return numer / denom
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

    def simplificar(self):
        pass

a = Fração(4, 5)
b = Fração(-2, 7)
resultado = a.multiplicar(b)
