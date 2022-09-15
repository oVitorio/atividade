
def exercicio_1():
    n = int(input("Digigte um numero: "))

    if n >= 20:
        print(f"seu numero: {n} é maior ou igual a 20")
    else:
        print(f"seu numero: {n} é menor a 20")

def exercicio_2():
    n1 = int(input("Digite um numero para a soma: "))
    n2 = int(input("Digite um outro numero para a soma: "))

    result_soma = n1 + n2 

    if result_soma >= 10 :
        print(f"Seu resultdo: {result_soma} é mairo ou igual a 10")
    else:
        print(f"Seu resultdo: {result_soma} é menor ou igual a 10")

def exercicio_3():
    x = int(input("Digigte um numero: "))
    if x > 0:
        x = x**(1/2)
        print(f"Seu resultdo:{x}")
    else:
        x = x*x
        print(f"Seu resultdo:{x}")

def exercicio_4():
    x = int(input("Digigte um numero: "))
    if x%3 == 0:
        print(f"Seu resultdo:{x} é multiplo de 3")
    else:
        print(f"Seu resultdo:{x} não é multiplo de 3")


def exercicio_5():
    x = int(input("Digigte um numero: "))
    if x%3 == 0 and x%7:
        print(f"Seu resultdo:{x} é multiplo")
    else:
        print(f"Seu resultdo:{x} não é multiplo ")

def exercicio_6():
    x = int(input("Digigte um numero: "))
    if x%10 == 0 and x%5 == 0 and x%2 == 0:
        print(f"Seu resultdo:{x} é multiplo de 10,5 e 2")
    else:
        print(f"Seu resultdo:{x} não é multiplo de 10,5 e 2 ")

def exercicio_7():
    x = 1
    while x < 51:
        print(x)
        x =+ 1


def exercicio_8():

    print(" com for ")
    for x in range(0,101,2):
            print(x)
    print("com o while")
    x=0
    while x < 100:
        print(x)
        x =+1
print("exercio1 ")      
exercicio_1()
print()

print("exercio2")         
exercicio_2()
print()

print("exercio3")      
exercicio_3()
print()
print("exercio4")     
exercicio_4()
print()

print("exercio5")         
exercicio_5()
print()

print("exercio6") 
exercicio_6()
print()

print("exercio7")         
exercicio_7()
print()

print("exercio8") 
exercicio_8()
print()