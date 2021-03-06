from matplotlib import pyplot

class Model():
    def fit(self, data):
        raise NotImplementedError("Metodo non ancora implementato")
    
    def predict(self, data):
        raise NotImplementedError("Metodo non ancora implementato")

    def incremento_medio(self, data):
        #controllo se ci sono i dati

        #lunghezza dei dati
        lun = len(data)
        #incrementi
        incrementi = []

        for i, item in enumerate(data):
            if i < lun - 1:
                incrementi.append(data[i + 1] - data[i])
        
        #incremento medio
        incr_medio = sum(incrementi) / len(incrementi)
        return incr_medio

    
class IncrementalModel(Model):
    
    def predict(self, data):

        incr_medio = incremento_medio(data)
        prediction = data[-1] + incr_medio
        return prediction

class FitIncrementalModel(IncrementalModel):

    def predict(self, data):
        #faccio un array
        data_last_3moth = []
        for item in data:
            data_last_3moth.append(item)

        while len(data_last_3moth) > 3:
            data_last_3moth.pop(0)

        incr_last_moth = self.incremento_medio(data_last_3moth)

        global_incr_medio = (self.global_agv_increment + incr_last_moth) / 2

        return data[-1] + global_incr_medio


    def fit(self, data):
        data_first_moth = []
        lun = len(data)
        for i in range(lun - 3):
            data_first_moth.append(data[i])
        
        incr_first_moth = self.incremento_medio(data_first_moth)
        self.global_agv_increment = incr_first_moth
        return incr_first_moth

class CSVFile:

    #metodo per sapere il numero di righe totali del file
    def __conta_righe__(self, nome_file):
        my_file = open(nome_file, 'r')
        #contatore
        i = 0
        #scorro il file riga per riga
        for line in my_file:
            #ad ogni ciclo aggiungo uno al contatore
            i = i + 1
        #returno il contatore
        return i

    #funzioni per inizializzare le variabili
    def __inizializzazione__(self, nome_file):
        #nome
        self.name = nome_file
        #titolo del file
        my_file = open(self.name, 'r')
        self.title = my_file.readline().strip()
        my_file.close()
        #numero di righe del file
        self.n_righe = self.__conta_righe__(self.name)

    #in caso di errori si usa un opzione di default
    def __inizializzazione_defoult__(self):
        self.name = 'shampoo_sales_default.csv'
        self.title = 'Data,Sales'
        self.start = 1
        self.end = 1
        self.righe = 2
  
    #metodo __init__ determina il nome del file e il titolo
    def __init__(self, nome_file):
        #controllo se l'input sia una stringa
        if type(nome_file) != str:
            #se non lo ?? raiso un errore generico
            raise Exception ('\nIl nome del fle non ?? una stringa\n    nome_file = "{}"'.format(nome_file))
                
        try:            
            #inizializzo nome e titolo del file
            self.__inizializzazione__(nome_file)
        except FileNotFoundError:
            print('---lol---')
            print('Il file non ?? stato TROVATO')
            print('  nome inserito: "{}"'.format(nome_file))
            print('Viene usato il file defolt.csv\n')
            self.__inizializzazione_defoult__()
        except Exception as e:
            print('---lol---')
            print('Errore di tipo generico')
            print('  il file non ?? stato inizializzato correttamente\n  {}\n'.format(e))
            self.__inizializzazione_defoult__()

    #metodo __str__ come viene rappresentato a schermo il file
    def __str__(self):
        #return nome del file e titolo
        return '_______\nNome file: {}\nTitolo: {}'.format(self.name, self.title)


    #metodo get_data() restituisce una lista di liste che rappresentano le righe
    def get_data(self, start = None, end = None):
        #aprire il file
        my_file = open(self.name, 'r')
        all_data = []

        #controllo se start e end hanno vallri corretti
        #se start ?? minore di end
        #se start ?? maggiore di zero e minore del numero massimo delle righe del file
        #se end ?? pi?? piccolo del numero massimo delle righe di un file

        #trasformo le variabili di start e end cos?? le posso usare in ogni caso
        #se start e end non ?? inserito
        if start is None:
            start = 1
            end = self.__conta_righe__(self.name)
        #se start ?? inserito e end non ?? inserito
        elif start is not None and end is None:
            end = self.__conta_righe__(self.name)
        #se sono entrambi inseriti non sono necessarie modifiche

        #considerare riga per riga il file
        for i, line in enumerate(my_file):
            #elimino\n nella linea
            line = line.strip('\n')
            #se non ?? la prima riga ed ?? in range(start, end)
            if i in range(start - 1, end) and i != 0:
                #lista che contiene linea divisa dalle virgole
                line_data = line.split(',')                    
                #se la linea non ?? vuota
                if(line_data[0] != ''):
                    #aggiungere questa lista in una lista che rappresenta tutto il file
                    all_data.append(line_data)
            
        #chidere il file
        my_file.close()
        #restuire la lista del file
        return all_data

        ##forse si pu?? fare con il get data() veccio e poi tagliare le parti che non ci piacciono, me ?? pi?? lungo

    def get_date(self):
        all_data = self.get_data()
        all_date = []
        for item in all_data:
            print(line)
            #la data la trasformo in un data_object
            tempo = datetime.strptime(item[0], "%d-%m-%Y")
            all_date.append(tempo)
        
        print(all_date)
        return all_date        
 
#classe che rappresenta un CSV file con dati che sono float 
class NumericalCSVFile(CSVFile):
    
    #metodo get_data() trasforma in float tutte le coloe tranne la prima
    def get_data(self, start = None, end = None):
        #prende in considerazione la lista di lista di super.get_data()
        all_floatydata = super().get_data(start, end)
        #lista per la gestione degli errori
        trash = []
        #la scorre lista per lista
        for j, lista in enumerate(all_floatydata):
            #scorre ogni elemento della lista
            for i, elemento in enumerate(lista):
                #se non ?? il primo elemento
                if(i != 0):
                    try:
                        #lo trasforma in un float
                        lista[i] = float(elemento)
                    except ValueError:
                        print('---lol---')
                        print('Errore di VALORE')
                        print('  "elemento" non ?? convertibile in un float')
                        print('  "elemento" = {}'.format(elemento))
                        print('La linea {} verr?? cancellata\n'.format(j + 2))
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

myfile = NumericalCSVFile("shampoo_sales.csv")


pippo = []
for item in myfile.get_data():
    for i, colonna in enumerate(item):
        if i > 0:
            pippo.append(colonna)

modello = FitIncrementalModel()
print(modello.fit(pippo))
print(modello.predict(pippo))

pyplot.plot(pippo + [modello.predict(pippo)], color='tab:red')
pyplot.plot(pippo, color='tab:blue')
pyplot.show()