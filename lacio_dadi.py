from random import randint

N = 10

fp = open('ESERCIZIO_36.txt', 'w')

lanciAlice = [randint(1,6) for _ in range(N)]
lanciBob =[randint(1,6) for _ in range(N)]

fp.write('Alice\tBob\n')

for a, b in zip(lanciAlice,lanciBob):
    fp.write(f"{a}\t\t{b}\n")
    print(f"Alice : {a}, Bob: {b}")

fp.close()





