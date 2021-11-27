def stampa(lista):
    print('####')
    for i, item in enumerate(lista):
        print('{}: {}'.format(i, item))

def statistiche(lista):
    dati = []

    #dati[0] conterrà somma
    dati.append(sum(lista))
    #dati[1] conterrà media
    dati.append(dati[0] / len(lista))
    #dati[2] conterrà minimo
    dati.append(min(lista))
    #dati[3] conterrà massimo   
    dati.append(max(lista)) 

    return dati

def somma_vettoriale(l1, l2):
    somma = []
    #se le due liste sono della stessa lunghezza
    if(len(l1) == len(l2)):
        #se le due liste sono composte solo da interi
        flag = True
        for item in l1:
            if(type(item) != int):
                flag = False
        for item in l2:
            if(type(item) != int):
                flag = False
        if(flag):
            #considero un indice alla volta
            for i in range(len(l1)):
                #la somma dei due elementi va aggiunta ne return
                somma.append(l1[i] + l2[i])

    return somma

sequenza = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stampa(sequenza)
stat = statistiche(sequenza)
stampa(stat)
stampa(somma_vettoriale(sequenza, sequenza))