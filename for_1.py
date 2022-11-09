#cicli for
lista =[1,4,9,7]

#modo preferito(pythonico)
for elemento in lista:
    print(elemento,end=" ")
print()
# modo C STYLE/JAVA STYLE
for i in range(0,len(lista)):
    print(lista[i],end=" ")
print()
#esempio
lista2 =[3,4,5,2,6,1]
max = lista2[0]
min = lista2[0]

for elemento in lista2:
    if(elemento > max):
        max = elemento
    elif(min > elemento):
        min = elemento

print(f"valore maggiore: {max} valore minore: {min}")