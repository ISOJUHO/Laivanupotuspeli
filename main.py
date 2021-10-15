
num1 = float(input ("Anna 1.numero: "))
op = input ("Syötä laskutapa: ")
num2 = float(input ("Anna 2.numero: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("viallinen laskutapa")