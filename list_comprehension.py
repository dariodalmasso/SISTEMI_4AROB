#esiste il costrutto list comprehension(che permette al volo di costruire una lista come l'esercizio precedente.)

print("inserire un numero:")
numero = int(input())

lista=[i for i in range(1,numero + 1)]#questo
print(lista)

#fare la lista con list comprehension che permetta di inserire i quadrati di prima

lista2=[i**2 for i in range(1,10+1)]#questo qua l'esercizio
print(lista2)