"""Scrivete una funzione che sommi
tutti gli elementi di una lista*.
Poi, committate il file in cui l’avete scritta"""

def SumList(lista):
    somma = 0
    for item in lista:
        somma = somma + item
    return somma
        
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("sum lista: {}".format(SumList(numeri)))