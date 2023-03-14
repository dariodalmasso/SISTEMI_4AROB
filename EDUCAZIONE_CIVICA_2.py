
import matplotlib.pyplot as plt
import csv

anni = []
media_temperatura = []
data_file = open("C:\\Users\\Lorena\\Documents\\SCUOLA\\QUARTA\\SISTEMI\\ESERCIZI PYTHON\\Temperature_Anomaly.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader:
 anni.append(int(row[0]))
 media_temperatura.append(float(row[1]))

fig, (ax1) = plt.subplots(1,1)
fig.suptitle('Anno dal 1880 ad oggi e valori di anomalia della temperatura del pianeta')

ax1.plot(anni, media_temperatura, 'o-g')
ax1.set_xlabel('anno')
ax1.set_ylabel('valori anomalia temperatura')

plt.show()