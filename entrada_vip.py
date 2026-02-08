# 1. Pedimos la edad al usuario y la convertimos a número (int)
edad = int(input("Por favor, introduce tu edad:  "))

# 2. Lógica de decisión
if edad >= 18:
    print("Acceso permitido. ¡Bienvenido al club!")
else:
    # Calculamos cuántos años le faltan para ser mayor
    faltan = 18 - edad
    print("Acceso denegado.")
    print("Vuelve dentro de", faltan, "años.")
    #Actualización final
    