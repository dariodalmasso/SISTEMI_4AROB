dizionario={"w":"avanti","a":"sinistra","s":"indietro","d":"destra",
"i":"avanti","j":"sinistra","k":"indietro","l":"destra",}

for chiave in dizionario:
    print(chiave) #mi stampa solo le chiavi del dizionario

comando = "avanti"

lista=[]

for elemento in dizionario:
    if dizionario[elemento]== comando:
        lista.append(elemento)

print(lista)

#enumerate fa ciclare sia su indice sia su elemento.
#while ciclo
#while(condizione)= codice;
#istruzioni controllo PASS E BREAK: interrompe il primo ciclo che si trova alle spalle, il primo ciclo;
#quando viene chiamata in un ciclo, lui schizza via al giro successivose faccio break all iterazione 5 si blocca la 5;
#WHILE(true){}

#come si definisce una funzione
# def = nomefunzione(i parametri): il codice indentato

        
        