#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num=(int(input(print("Num:"))))

for i in range(num):
    if i>0:
        num=num*i
print(num)
