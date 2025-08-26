import random

print("🪙 Cara ou Coroa")
escolha = input("Escolha (cara/coroa): ").lower()
resultado = random.choice(["cara", "coroa"])

print("Resultado:", resultado)
if escolha == resultado:
    print("🎉 Você ganhou!")
else:
    print("😅 Você perdeu!")