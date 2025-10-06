from clases.areas import Operaciones

def main():
    op = Operaciones()

    while True:
        print("\n--- MENÚ ---")
        print("1. Área Triángulo")
        print("2. Área Cuadrada")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "3":
            print("Saliendo del programa...")
            break

        if opcion == "1":
            op.leer_datos()
            op.areaTriangulo()
        elif opcion == "2":
            op.leer_datos()
            op.areaRectangulo()
        else:
            print("Opción inválida. Intenta de nuevo. ")

if __name__ == "__main__":
    main()
