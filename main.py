from clases.areas import Operaciones

def main():
    op = Operaciones()

    while True:
        print("\n--- MENÚ ---")
        print("1. Área Triángulo")
        print("2. Área Cuadrada")
        print("3. Área Circulo")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "4":
            print("Saliendo del programa...")
            break

        if opcion == "1":
            op.leer_datos()
            op.areaTriangulo()
        elif opcion == "2":
            op.leer_datos()
            op.areaRectangulo()
        elif opcion == "3":
            op.leer_radio()
            op.areaCirculo()
        else:
            print("Opción inválida. Intenta de nuevo. ")

if __name__ == "__main__":
    main()
