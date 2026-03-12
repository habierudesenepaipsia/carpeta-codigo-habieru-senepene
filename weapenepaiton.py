import random

numero = random.randint(1, 6)

print("Girando la ruleta... 🎲")
print("Salió:", numero)

if numero == 1:
    print("💀 Fuiste bueno... te tocó el castigo!")
else:
    print("😎 Te salvaste esta vez.")