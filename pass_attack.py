import random
import time

# Hedef şifre
target = input("Tahmin edilmesini istediğiniz şifreyi girin (sadece küçük harf ve rakam): ").lower()

# Kullanılacak karakterler
chars = list("abcdefghijklmnopqrstuvwxyz0123456789")

attempt = ""
attempts = 0

while attempt != target:
    attempt = ""
    for i in range(len(target)):
        attempt += random.choice(chars)
    attempts += 1
    print(f"Deneme #{attempts}: {attempt}")
    time.sleep(0.05)

print(f"Şifre bulundu: {attempt} ({attempts} denemede)")
