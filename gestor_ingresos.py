# El programa se detiene aquí y espera a que escribas
dinero_banco = int(input("Introduce el balance en tu cuenta: "))

ingreso = int(input("¿Cuánto vas a ingresar en tu cuenta principal?: "))

# Aquí hace el cálculo en silencio
restante = dinero_banco + ingreso

# Aquí te escupe el resultado
print(f"Ahora mismo tienes {restante}€ en la cuenta.")
