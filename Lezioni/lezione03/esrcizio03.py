# sommare volmi di vendita di shampooo

def sommavendire():

    #lista in cui ci saranno i valori di tute le vendite
    valoriVendite = []

    #apro il file
    file_s = open('shampoo_sales.csv', 'r')

    #considero il file riga per riga
    for line in file_s:
        #line = file_s.readline()
        #era sbagliato pklo facio due volte (lo fa già nel for)
        elementi = line.split(',')

        if elementi[0] != 'Date':
            valoriVendite.append(float(elementi[1]))

    file_s.close()

    #sommo tutti i valori delle vendite
    return sum(valoriVendite)

print(sommavendire())