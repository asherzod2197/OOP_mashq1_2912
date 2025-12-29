import random

yashirin_son = random.randint(1, 10)
urinishlar = 0

print("🎯 Men 1 dan 10 gacha son o‘yladim.")
print("Topib ko‘r!")

while True:
    taxmin = int(input("Soningni kiriting: "))
    urinishlar += 1

    if taxmin < yashirin_son:
        print("📉 Kichikroq son")
    elif taxmin > yashirin_son:
        print("📈 Kattaroq son")
    else:
        print(f"🎉 To‘g‘ri! {urinishlar} urinishda topding.")
        break
