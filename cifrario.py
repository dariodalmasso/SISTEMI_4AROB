

# esercizio cifrario

dizionario = {"a":"b", "b":"c", "c":"d", "d":"e","e":"f", "f":"g","g":"h","h":"i","i":"l", "l":"m", "m":"n", "n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"z","z":"a"}

print("inserisci una parola: ")
parola = input()


for elemento in parola:
  print(dizionario[elemento])

decodificatore ={}

for k,v in dizionario.items(): #ciclo for fatto contemporaneamente su due varibili
  #print(k,v) #stampa il dizionario
  decodificatore[v]=k

#print(decodificatore)
for elemento in parola:
  print(decodificatore[elemento])


