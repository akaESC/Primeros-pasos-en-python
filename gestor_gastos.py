# El programa se detiene aquí y espera a que escribas
presupuesto = int(input("Introduce tu presupuesto total: "))

gasto = int(input("¿Cuánto te has gastado hoy?: "))

# Aquí hace el cálculo en silencio
restante = presupuesto - gasto

# Aquí te escupe el resultado
print(f"Te quedan {restante}€ en la cuenta.")
