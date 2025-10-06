import numpy as np

class Operaciones:
    def __init__(self):
        self.base = 0
        self.altura = 0
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

    def areaTriangulo(self):
        self.resultado = np.divide(np.multiply(self.base, self.altura), 2)
        print(f"Área del triángulo = (bxh)/2 = {self.resultado}")

    def areaRectangulo(self):
        self.resultado = np.multiply(self.base, self.altura)
        print(f"Área del rectángulo = bxh = {self.resultado}")