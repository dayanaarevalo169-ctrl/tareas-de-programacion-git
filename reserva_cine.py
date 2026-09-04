asientos = [[0 for _ in range(4)] for _ in range(3)]
 
while True:
     try:
         fila = int(input("Ingrese la fila (0 a 2): "))
         columna = int(input("Ingrese la columna (0 a 3): "))
         if 0 <= fila <= 2 and 0 <= columna <= 3:
             break
         else:
             print(" Valores fuera de rango. Intente nuevamente.")
     except ValueError:
         print(" Ingrese números enteros solamente.")
 
asientos[fila][columna] = 1
 
print("\n Estado de la sala de cine:")
print("-" * 18)
for fila in asientos:
     for lugar in fila:
         print(f"│ {lugar} ", end="")
     print("│")
     print("-" * 18)