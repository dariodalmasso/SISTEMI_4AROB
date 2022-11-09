def leggi_file():
    file = open("./MATEMATICI.csv","r")
    righe = file.readlines()
    file.close()
    diz = {"id":{}, "nome":{}}
    for riga in righe[1:]:
        campi_riga =riga[:-1].split(",");
        #aggiunge nella parte del dizionario id la parte dei campi riga di id;
        diz["id"].append(int(campi_riga[0]))
        diz["nome"].append(campi_riga[1][1:])
        print(diz)
        return diz

def nome_Id(diz):
    listaId = diz["id"]
    listaNomi = diz["nome"]
    print(listaNomi)
    print(listaId)
    #funzione che ti scorre due liste insieme
    for i,n in zip(listaId,listaNomi):
        print(i,n)
        if i == id:
            return n



def main():

    diz= leggi_file()
    id = 2
    nome = nome_Id(id, diz)
    print(nome)