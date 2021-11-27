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
            line = line.strip('\n')   #
            elemento = line.split(',')
            if(elemento[0] != 'Date'):
                all_data.append(elemento)
        
        #chiudo il file e ritorno all_data
        file_csv.close()
        return all_data

class NumericalCSVFile(CSVFile):

    def get_data(self):
        #predo la lista di liste della classe genitrice
        all_data_float = super().get_data()

        #lista in cui ci sono gli indici j che devono essere poppati
        bleah = []

        #considero una lista alla volta
        for j, item in enumerate(all_data_float):
            #in ogni lista prendo il primo elemento e il suo indice
            for i, elemento in enumerate(item):
                if(i != 0):
                    try:
                        #converto in float
                        item[i] = float(elemento)

                    except ValueError:
                        print('----------')
                        print("Errore di TIPO: 'elemento' non può essere convertito in un float")
                        print("Tipo 'elemento': {}".format(type(elemento)))
                        print('"elemento" =  "{}"'.format(elemento))
                        bleah.append(j)  
                    except Exception as e:
                        print('----------')
                        print("Errore generico: 'elemento' non può essere convertito in un float")
                        print('"elemento" =  "{}"'.format(elemento))
                        bleah.append(j)

        bleah.reverse()
        for riga in bleah:
            all_data_float.pop(riga)

        return all_data_float
        

myfile = NumericalCSVFile("shampoo_sales.csv")
#print(myfile)
#print(myfile.name)
print(*myfile.get_data(), sep = '\n')
#for item in myfile.get_data():
#    for i in item:
#        print(type(i))