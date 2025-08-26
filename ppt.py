import random

opcoes = ["pedra", "papel", "tesoura"]

print("✊✋✌️ Pedra, Papel ou Tesoura!")
usuario = input("Escolha (pedra/papel/tesoura): ").lower()
computador = random.choice(opcoes)

print(f"Você escolheu: {usuario}")
print(f"Computador escolheu: {computador}")

if usuario == computador:
    print("🤝 Empate!")
elif (usuario == "pedra" and computador == "tesoura") or \
     (usuario == "papel" and computador == "pedra") or \
     (usuario == "tesoura" and computador == "papel"):
    print("🎉 Você venceu!")
else:
    print("💻 O computador venceu!")