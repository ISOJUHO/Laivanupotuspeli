print("Tervetuloa käyttämään funktiolaskinta")
print("Tämä laskin pystyy laskemaan yhteen-, vähennys-, jako- ja kertolasuja")
print("1 yhteenlasku\n2 vähennyslasku\n3 jakolasku\n4 kertolasku")
laskutapa = input("Valitse laskutapa kirjoittamalla numero: ")

def yhteenlasku():
    luku1 = int(input("Anna 1.yhteenlaskettava luku: "))
    luku2 = int(input("Anna 2.yhteenlaskettava luku: "))
    print(luku1 + luku2)

def vähennyslasku():
    luku1 = int(input("Anna luku: "))
    luku2 = int(input("Anna vähennettävä luku: "))
    print(luku1 - luku2)

def jakolasku():
    luku1 = int(input("Anna jaettava luku: "))
    luku2 = int(input("Anna jakaja: "))
    print(luku1 / luku2)

def kertolasku():
    luku1 = int(input("Anna 1.luku: "))
    luku2 = int(input("Anna 2.luku: "))
    print(luku1 * luku2)


if laskutapa == "1":
    yhteenlasku()
elif laskutapa == "2":
    vähennyslasku()
elif laskutapa == "3":
    jakolasku()
elif lskutapa == "4":
    kertolasku()