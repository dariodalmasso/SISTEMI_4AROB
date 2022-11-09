lista =["Gauss","Conmay","Eulero","Hilbert"]

#creare una lista che formi una lista dagli intellettuali che iniziano con g o con h

lista =["Gauss","Conmay","Eulero","Hilbert"]
lista2 = [nome for nome in(if nome[0] == "G" or nome[0] == "H")]
print(lista2)