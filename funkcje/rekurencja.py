import sys
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(16))

# def incrementator(i):
#     print(i)
#     incrementator(i+1)

# incrementator(1)

lista = [10, 20, 30, 40, 50]

def rekuprint(lista):
    print(lista[0])
    if len(lista) > 1:
        rekuprint(lista[1:])

rekuprint(lista)

# 5! = 5*4! = 5*4*3! = 5*4*3*2! = 5*4*3*2*1! = 5*4*3*2*1*0! = 5*4*3*2*1*1