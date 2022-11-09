file = open("./MATEMATICI.csv", "r")

lista_righe = file.readlines()
#print(lista_righe)

dizionario = {"id":[], "nomi":[]}

for riga in lista_righe[1:]:
    riga_senza_linefeed = riga[::1]
    #print(riga_senza_linefeed)
    lista_campi = riga_senza_linefeed.split(",")
    #print(lista_campi)


    id = lista_campi[0]
    nome = lista_campi[1]
    print(id, nome)
    dizionario["id"].append(id)
    dizionario["nomi"].append(nome)
    print(dizionario)
    #ricercare il matematico con una funzione

 #FUNZIONE MAIN
def main():
    file = open("./MATEMATICI.csv", "r")

         lista_righe = file.readlines()
           #print(lista_righe)

         dizionario = {"id":[], "nomi":[]}
         

file.close()
