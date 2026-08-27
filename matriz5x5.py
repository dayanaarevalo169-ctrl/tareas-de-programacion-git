matriz = [[0 for _ in range(5)] for _ in range(5)]

for fila in range(5):
    for columna in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{fila}][{columna}]: "))
        matriz[fila][columna] = valor

print("\n=== MATRIZ INGRESADA ===")
for fila in range(5):
    for columna in range(5):
        print(f"{matriz[fila][columna]:4}", end="")
    print()  # Salto de línea por fila