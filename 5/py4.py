#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


def sinal(n):
    if n>0:
        print("P")
    else:
        print("N")
sinal(5)
sinal(-5)
