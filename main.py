import random

print("🎮 ¡Bienvenido al juego de adivinar números!")

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    try:
        numero = int(input("Adivina el número (1-100): "))
        intentos += 1

        if numero < numero_secreto:
            print("📈 El número es más alto.")
        elif numero > numero_secreto:
            print("📉 El número es más bajo.")
        else:
            print(f"🎉 ¡Correcto! Lo lograste en {intentos} intentos.")
            break

    except ValueError:
        print("❌ Introduce un número válido.")