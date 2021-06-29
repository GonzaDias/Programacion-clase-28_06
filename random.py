import random


num1 = random.randint(1,10)
num2 = random.randint(1,10)
num3 = random.randint(1,10)

if (num1 > num2) and (num1 > num3):
    print("num1 es el mayor")

elif (num2 > num1) and (num2 > num3):
    print("num2 es el mayor")
elif ((num1 == num2) and (num1 == num3)) or ((num2 == num3) and (num2==num1)) or ((num3 == num1) and (num3 == num2)):
    print("todos los numeros son iguales")
else:
    print("num3 es el mayor")


print("num1 es:", num1)
print("num2 es:", num2)
print("num3 es:", num3)

