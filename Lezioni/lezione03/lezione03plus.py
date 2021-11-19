# sommare volmi di vendita di shampooo

def sommavendire(nome_file, anno):

    #lista in cui ci saranno i valori di tute le vendite
    valori_vendite = []

    #apro il file
    file_s = open(nome_file, 'r')

    #considero il file riga per riga
    for riga in file_s:
        #divido le date dalle vendite
        elementi = riga.split(',')
        
        #prendo in considerazione tutte le righe tranne la prima
        if elementi[0] != 'Date':
            #prendo in considerazione le righe che hanno l'anno uguale a quello dato
            elementi_date = elementi[0].split('-')
            #print(elementi_date[2])
            if elementi_date[2] == anno:
                #aggiungo alla lista vallori vendite
                valori_vendite.append(float(elementi[1]))
    
    #chiudo il lfile
    file_s.close()

    #sommo tutti i valori delle vendite
    return sum(valori_vendite)

print(sommavendire('shampoo_sales.csv', '2012'))