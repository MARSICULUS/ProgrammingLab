# sommare volmi di vendita di shampooo

def sommavendire():
    valoriVendite = []

    file_s = open('shampoo_sales.csv', 'r')

    for line in file_s:
        #line = file_s.readline()
        #era sbagliato pklo facio due volte (lo fa già nel for)
        elementi = line.split(',')

        if elementi[0] != 'Date':
            valoriVendite.append(float(elementi[1]))

    file_s.close()
    return sum(valoriVendite)

print(sommavendire())