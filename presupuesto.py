# 1. Definimos los precios
procesador = 200
grafica = 400

# 2. Calcula el total sumando las dos variables anteriores
total = procesador + grafica

# 3. Lógica de decisión (IF)
# Si el total es más de 500, imprime "Te estás pasando de presupuesto"
# Si no, imprime "Presupuesto aceptado"

if total > 500:
	print("Te estás pasando de presupuesto")
else:
	print("Presupuesto aceptado")

# 4. Imprime el total final
print("El coste total es:", total)