# 1. Base de datos
black_list = ["david johnson", "spam", "scam", "fake", "axis prime consulting"]
# 2. El bucle (El programa no se apaga)
while True:
    print("\n--- ESCÁNER DE SEGURIDAD ACTIVO ---")
    name = input("Nombre...").lower()

    if name == "salir":
        print("Apagando el sistema...")
        break  # Esto rompe el bucle y cierra/apaga el programa
    if name in black_list:
        print(f"¡ALERTA! El nombre '{name}' está en la lista negra. ¡Acceso denegado!")
    else:
        print(f"El nombre '{name}' es seguro. ¡Acceso permitido!")
