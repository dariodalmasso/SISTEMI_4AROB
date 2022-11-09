#TUTTI I MODI OER FARE UN CICLO FOR

lista1 =["a","b","c","d"]

lista2 =[1,2,3,4]

#for su lista 1 con c style
#for su lista1 con python style
#for su lista1 su enumerate
#for su lista1 e lista2 python style(zip)
#for su lista 1 e lista2 ma C style(range)

#for su lista1 con python style
for elemento in lista1:
    print(elemento, end =" ")
print("\n")
#for su lista1 con python style
for i in range(0,len(lista1)):
    print(lista1[i],end=" ")
print("\n")
#for su lista1 su enumerate
for indice, elemento in enumerate(lista1):
    print(elemento,end=" ")
print("\n")
#for su lista1 e lista2 python style(zip)
for a, b in zip(lista1, lista2):
    print(a,b,end=" ")

diz = {"a": 0,"b": 1,"c": 2,"d": 3,"e": 4,}
# for su diz usando items
print("\n")
for indice, elemento in diz.items():
   print(indice, elemento,end=" ")
#for su diz nsenz aitem
print("\n")
for chiave in diz:
    print(chiave,end=" ")
