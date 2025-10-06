import numpy as np

class Operaciones:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.radio = 0
        self.resultado = 0

    def leer_datos(self):
        while True:
            try:
                self.base = float(input("\nBase (b): "))
                break
            except ValueError:
                print("Entrada inválida, intenta de nuevo.")

        while True:
            try:
                self.altura = float(input("Altura (h): "))
                break
            except ValueError:
                print("Entrada inválida, intenta de nuevo.")

    def leer_radio(self):
        while True:
            try:
                self.radio = float(input("\nRadio (r): "))
                break
            except ValueError:
                print("Entrada inválida, intenta de nuevo.")

    def areaTriangulo(self):
        self.resultado = np.divide(np.multiply(self.base, self.altura), 2)
        print(f"Área del triángulo = (b x h) / 2 = {self.resultado}")

    def areaRectangulo(self):
        self.resultado = np.multiply(self.base, self.altura)
        print(f"Área del rectángulo = b x h = {self.resultado}")

    def areaCirculo(self):
        self.resultado = np.pi * np.power(self.radio, 2)
        print(f"Área del círculo = π x r² = {self.resultado}")