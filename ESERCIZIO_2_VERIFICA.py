numero = int(input("inserisci il numero:"))

lista = [1] * numero
lista[0],lista[-1] = 0,0
print(lista)