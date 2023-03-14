
import matplotlib.pyplot as plt
import csv

#questa parte di codice legge il file csv e salva in liste diverse tutte le righe del file

mesi_n = []  
temperature_boves = []
#apre il file csv
data_file = open("C:\\Users\\Lorena\\Documents\\SCUOLA\\QUARTA\\SISTEMI\\ESERCIZI PYTHON\\EDUCAZIONE_CIVICA.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)

for row in data_reader:
   mesi_n.append(row[1])
   temperature_boves.append(row[2])

#parte di codice dove si sviluppano i grafici
#fig variabile di figura

      #tupla di assi
fig, (ax1) = plt.subplots(1, 1) #due righe e una colonna, serve per dividire la schermata per dividere il foglio
#titolo della figura o del grafico
fig.suptitle('Media dei voti di tutte le materie eore di studio giornaliere medie nel periodoGennaio-Giugno')
#primo grafico con chiamate dei suoi assi
#prima la lista che va in asse x e poi quella in asse y
ax1.plot(mesi_n, temperature_boves, 'o-g')#g sta per green
ax1.set_xlabel('Mese')
#questo richiama funzione per asse y
ax1.set_ylabel('Temperature medie a boves')



plt.show()