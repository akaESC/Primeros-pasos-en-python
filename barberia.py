# Lista de clientes esperando en la barbería
clientes = ["Fran", "Juan", "Pedro", "Luis"]

# PASO 1: "Fran" entra a pelarse, así que hay que quitarlo de la lista.
# El método .pop(0) elimina al que está en la posición 0.
clientes.pop(0)

# PASO 2: Llega "Leo", es un cliente VIP y quiere ser el segundo en la cola.
# El método .insert(posicion, nombre) sirve para esto. 
# Recuerda: la primera posición es 0, la segunda es 1.
# ESCRIBE AQUÍ LA LÍNEA PARA INSERTAR A "LEO" EN LA POSICIÓN 1:
clientes.insert(1, "Leo")

# PASO 3: Imprimimos la lista para ver si lo has hecho bien.
print("La nueva cola de la barbería es:", clientes) 