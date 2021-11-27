#classe che rappresenta un CSV file 
class CSVFile:
    #metodo __init__ determina il nome del file e il titolo
    def __init__(self, nome_file):
        try:
            #inizializzo nome e titolo del file
            self.name = nome_file
            my_file = open(self.name, 'r')
            self.title = my_file.readline()
            my_file.close()
        except FileNotFoundError:
            print('---lol---')
            print('Il file non è stato TROVATO')
            print('  nome inserito: "{}"'.format(nome_file))
            print('Viene usato il file defolt.csv\n')
            self.name = 'defolt.csv'
            my_file = open(self.name, 'r')
            self.title = my_file.readline()
            my_file.close()
        except Exception as e:
            print('---lol---')
            print('Errore di tipo generico')
            print('  il file non è stato aperto correttamente')
            print('  {}\n'.format(e))

    #metodo __str__ come viene rappresentato a schermo il file
    def __str__(self):
        #return nome del file e titolo
        return '§§§§§§§\nNome file: {}\nTitolo: {}'.format(self.name, self.title)
    
    #metodo get_data() restituisce una lista di liste che rappresentano le righe
    def get_data(self):
        #aprire il file
        my_file = open(self.name, 'r')
        all_data = []
        #considerare riga per riga il file
        for i, line in enumerate(my_file):
            #elimino\n nella linea
            line = line.strip('\n')
            #se non è la prima riga
            if(i != 0):
                #lista che contiene linea divisa dalle virgole
                line_data = line.split(',')
                #se la linea non è vuota
                if(line_data[0] != ''):
                    #aggiungere questa lista in una lista che rappresenta tutto il file
                    all_data.append(line_data)
            
        #chidere il file
        my_file.close()
        #restuire la lista del file
        return all_data
 
#classe che rappresenta un CSV file con dati che sono float 
class NumericalCSVFile(CSVFile):
    
    #metodo get_data() trasforma in float tutte le coloe tranne la prima
    def get_data(self):
        #prende in considerazione la lista di lista di super.get_data()
        all_floatydata = super().get_data()
        #lista per la gestione degli errori
        trash = []
        #la scorre lista per lista
        for j, lista in enumerate(all_floatydata):
            #scorre ogni elemento della lista
            for i, elemento in enumerate(lista):
                #se non è il primo elemento
                if(i != 0):
                    try:
                        #lo trasforma in un float
                        lista[i] = float(elemento)
                    except ValueError:
                        print('---lol---')
                        print('Errore di VALORE')
                        print('  "elemento" non è convertibile in un float')
                        print('  "elemento" = {}'.format(elemento))
                        print('La linea {} verrà cancellata\n'.format(j + 2))
                        trash.append(j)
                    except Exception as e:
                        print('---lol---')
                        print('Errore di tipo generico')
                        print('  {}\n'.format(e))
        
        #invertiamo l'ordine degli indici da eliminare
        trash.reverse()
        #prendiamo ogni elemento dalla lista trash
        for indice in trash:
            #eliminiamo da all_floatydata gli indici che creano un errore
            all_floatydata.pop(indice)

        #return la nuova lista
        return all_floatydata

myfile = CSVFile("shampoo_sales.csv")
print(myfile)
print(*myfile.get_data(), sep = '\n')

myfile = NumericalCSVFile("shampoo_sales.csv")
print(myfile)
print(*myfile.get_data(), sep = '\n')