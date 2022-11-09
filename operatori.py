print("inserire il numero per l'operando:")
operatore = int(input())

print("inserisci il primo numero:")
numero1 = int(input())
print("inserisci il secondo numero:")
numero2 = int(input())

def operazione(numero1, numero2, operatore):
    if(operatore == 0):
        print(numero1 + numero2)
    elif(operatore == 1):
        print(numero1 - numero2)
    elif(operatore == 2):
        print(numero1 * numero2)
    elif(operatore == 3):
        print(numero1 / numero2)
    else:
        print("operazione non riuscita!")
    


