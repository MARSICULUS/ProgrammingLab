class CSVFile:

    def __init__(self, nome_file):
        #inizializzo classe con nome del file
        self.name = nome_file
    
    def get_data(self):
        #apro file
        file_csv = open(self.name , 'r')
        #lista che conterrà i dati
        all_data = []

        #guardo il file linea per linea
        for line in file_csv:
            #la linea la divido e la salvo in all_data
            elemento = line.split(',')
            if(elemento[0] != 'Date'):
                all_data.append(elemento)
        
        #chiudo il file e ritorno all_data
        file_csv.close()
        return all_data
        

myfile = CSVFile('shampoo_sales.csv')
print(myfile)
print(myfile.name)
print(myfile.get_data())