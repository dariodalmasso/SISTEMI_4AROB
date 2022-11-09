print("inserire un numero:")
numero = int(input())
if (numero % 3 == 0):
    print("il numero è divisibile per 3!")
elif(numero % 5 == 0):
        print("il numero è divisibile per 5!")
elif(numero % 2 == 0):
    print("il numero è divisibile per 2")
elif(numero % 2 == 0 & numero % 3 == 0):
    print("il numero è divisibile per 2 e 3")
elif(numero % 2 == 0 & numero % 5 == 0):
    print("il numero è divisibile per 2 e 5")
elif(numero % 3 == 0 & numero % 5 == 0):
    print("il numero è divisibile per 3 e 5")
elif(numero % 2 == 0 & numero % 5 == 0 & numero % 5 == 0):
    print("il numero è divisibile per 2 e 5 e 3")
else:
    print("numero non divisibile")




    
