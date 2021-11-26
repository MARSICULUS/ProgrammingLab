class CSVFile:

    #inizializzo classe con nome del file
    def __init__(self, nome_file):
        #attributo name
        try:
            self.name = nome_file
            file_csv = open(self.name , 'r')
        except FileNotFoundError:
            print('Il file indicato non è stato TROVATO')
            print('il nome inserito era "{}"'.format(nome_file))
            self.name = "defolt.csv"
        except Exception as e:
            print('errore generico: "{}"'.format(e))
            self.name = "defolt.csv"

    
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

class NumericalCSVFile(CSVFile):

    def get_data(self):
        all_data = super().get_data()

        for item in all_data:
            item[1] = float(item[1])
        
        return all_data
        

myfile = NumericalCSVFile("shampoo_sales.csv")
#print(myfile)
#print(myfile.name)
print(*myfile.get_data(), sep = '\n')