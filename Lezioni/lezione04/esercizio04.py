class CSVFile:

    #inizializzo classe con nome del file
    def __init__(self, nome_file):
        #attributo name
        self.name = nome_file
    
    #metodo restituisce una lista di liste conteneti i dati(sono stringhe)
    def get_data(self):
        #lista che conterrà i dati
        all_data = []
        #apro file
        file_csv = open(self.name , 'r')

        #guardo il file linea per linea
        for line in file_csv:
            #la salvo in all_data, con le modifiche del caso
            line = line.strip('\n')
            elemento = line.split(',')
            if(elemento[0] != 'Date'):
                all_data.append(elemento)
        
        #chiudo il file e ritorno all_data
        file_csv.close()
        return all_data
        

myfile = CSVFile('shampoo_sales.csv')
print(myfile)
print(myfile.name)
print(*myfile.get_data(), sep = '\n')