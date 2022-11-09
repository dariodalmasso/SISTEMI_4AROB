# il dizionario
#indicizzazione mediante le chiavi, voglio sapere i voti del numero due della classe (printf(d[abello]))

rubrica ={"giordy": 3492434538, "zoeassa": 3489237483, "favour":3459899809,"bocaciuccio": 32402411338}

print(rubrica["zoeassa"])
print("inserisci un nuovo contatto: ")
nome = input()
rubrica[nome] = int(input())

print(rubrica)
