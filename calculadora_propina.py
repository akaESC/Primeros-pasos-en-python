cuenta = float(input("¿Cuánto te ha costado toda la cuenta?: "))
propina = float(input("¿Qué porcentaje de propina quieres dejar 10% o 15%?: "))
propina_calculada = cuenta * (propina / 100)
total = cuenta + propina_calculada
print(f"Tu propina es de {propina_calculada}€ y el total a pagar es de {total}€.")