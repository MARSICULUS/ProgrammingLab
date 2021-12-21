from datetime import datetime
#from matplotlib import pyplot

class FileVuoto(Exception):
    pass

""" 
Classe CSVFile
Serve per leggere una classe CSV file

---attributi---
self.name -> nome del file
self.title -> intestazione del file
self.righe -> numero di righe del file
self.can_read -> se il file esiste ed è leggibile(non vuoto)

---metodi---
__init__
    inizializza tutte gli attributi

__str__
    rappresentazione del file
    titolo, intestazione e numero di righe

__conta_righe__
    conta quante righe ci sono in un file
    non conta righe vuote

get_data
    ritorna una lista di liste, le liste più piccole contengono le righe nelle quali ogni elemento rappresenta una colonna

get_dates
    converte la lista di liste di get_data in una lista di liste, dove le date sono effettivamente l'oggetto datatime
"""
class CSVFile:

    def __init__(self, nome_file):

        #NOME del file
        #Controlo Se il nome è una stringa che finisce per .csv
        if type(nome_file) == str and nome_file[-4:] == '.csv':
            t_input = True
        else:
            t_input = False
        
        #Setto in nome
        self.name = nome_file

        #CAN_READ
        #Controllo se il nome del file è corretto
        if t_input:
            try:
                #provo ad aprirlo
                my_file = open(self.name, 'r')
                #Controllo non sia vuoto
                vuoto = [1 for line in my_file if line != '']
                my_file.close()
                #Se il file è vuoto raiso un Exception
                if sum(vuoto) < 1:
                    raise FileVuoto
                #quindi dico che si può aprire
                self.can_read = True
            except FileNotFoundError:
                #Se non esiste dico che non si può aprire
                #così nei test il messaggio di errore non viene visto
                if __name__ == '__main__':
                    print('\n--lol--\nIl file "{}" non è stato TROVATO\n--lol--\n'.format(self.name))
                self.can_read = False
            except FileVuoto:
                if __name__ == '__main__':
                    print('\n--lol--\nIl file "{}" è VUOTO, quindi illeggibile\n--lol--\n'.format(self.name))  
                self.can_read = False              

        else:
            self.can_read = False

        #TITOLO e RIGHE
        #Quando il file si può leggere controllo se non è vuoto
        if self.can_read:
            #Apro il file e prendo il titolo
            my_file = open(self.name, 'r')
            titolo = my_file.readline().strip('\n')
            my_file.close()
            self.title = titolo
            self.righe = self.__conta_righe__()
        #Quando il file non si può leggere o è vuoto
        else:
            self.title = None
            self.righe = 0
             
    #Presentazione del file
    def __str__(self):

        #Se il file è leggibile o è vuoto
        if self.can_read and self.righe > 0:
            return '[----------]\n{}\n    {}\n    numero righe: {}\n'.format(self.name, self.title, self.righe)
        #Se il file è leggibile ed è vuoto (non viene visualizzato il titolo)
        elif self.can_read and self.righe == 0:
            return '[----------]\n{}\n    numero righe: {}\n'.format(self.name, self.righe)
        else:
            return '[----------]\n"{}" non è stato TROVATO o è VUOTO\n'.format(self.name)
             

    def __conta_righe__(self):
        my_file = open(self.name, 'r')

        #Creo una lista di 1 per ogni riga che c'è nel file
        lst = [1 for i, line in enumerate(my_file) if i > 0 and line != '\n']

        my_file.close()
        return sum(lst)

    def get_data(self, start = None, end = None):

        if self.can_read:        
            #Se start non è stato inserito (e quindi anche end)
            if start is None:
                #start diventa 1 (perché la prima riga va saltata)
                start = 1
            #Se start è inserito e end non è inserito
            if end is None:
                #setto end al numero di righe del file
                end = self.righe + 1

            #Apro il file
            my_file = open(self.name, 'r')
            
            #creo una lista vuota (all data)
            all_data = []

            #Prendo tutte le righe e le metto nella lista
            for i, line in enumerate(my_file):
                    #divido la riga per ogni colonna
                    l = line.strip('\n')
                    l = l.split(',')
                    #salvo la linea
                    all_data.append(l)

            #Candello le righe vuote
            nice_data = [x for x in all_data if x[0] != '']
                
            #Taglio la lista a seconda di start ed end
            right_data = nice_data[start:end]

            #chido il file
            my_file.close()
            #return all data
            return right_data
        
        else:
            raise FileVuoto('Il file è ILLEGGIBILE\n       quindi non è stato possibile leggere i dati\n')
            return None
      
    
    def __get_magic_dates__(self, data):
        all_date = []
        for i, item in enumerate(data):
            #la data la trasformo in un data_object
            try:
                tempo = datetime.strptime(item[0], "%d-%m-%Y")
                item[0] = tempo
                all_date.append(item)
            except ValueError:
                if __name__ == '__main__':
                    print('La CONVERSIONE in data della riga {} non ha avuto sucesso\n    contenuto prima colonna: {}'.format(i, item[0]))

        return all_date

    def get_dates(self, start = None, end = None):
        all_data = self.get_data(start, end)
        return self.__get_magic_dates__(all_data)
         
    

""" 
Classe NumericalCSVFile

Estende la classe CSVFile, e sovrascrive il metodo get_data e get_dates

--metodi--
get_data e get_dates: etrambi riprendono la lista ritornata dalla classe madre ma tutti gli elementi della seconda colonna in poi sono convertiti in float 

"""
class NumericalCSVFile(CSVFile):
    
    def get_data(self, start = None, end = None):
        #se il file è leggibile:
        if self.can_read is True:
            #Prende l'output della funzione madre
            all_data = super().get_data(start, end)
            all_floaty_data = []

            #Scorre riga per riga l'output
            for line in all_data:
                #lita vuota (sarà la riga di float)
                floaty_line = []

                #Scorro elemento per elemento nella riga:
                for i, elem in enumerate(line):
                    #flag
                    tutti_gli_elem = True

                    #se è il primo elemento salvalo nella lista
                    if i == 0:
                        floaty_line.append(elem)
                    #altrimenti
                    else:
                        try:
                            #a trasformare ogni elemento in float
                            floaty_elem = float(elem)
                            floaty_line.append(floaty_elem)
                        except ValueError:
                            if __name__ == '__main__':
                                #il numero della riga viene salvato in una lista a parte
                                #esco dal ciclo
                                print('Il elemento "{}" non è possibile convertirlo in un float, la riga viene saltata'.format(elem))
                                tutti_gli_elem = False
                                break
                
                if tutti_gli_elem:
                    all_floaty_data.append(floaty_line)
            
            #ritorna l'out put
            return all_floaty_data
        
        #altrimenti restituisci None
        return None
    
    def get_dates(self, start = None, end = None):
        all_floaty_data = self.get_data(start, end)
        return super().__get_magic_dates__(all_floaty_data)

"""
Modello
"""
#Classe modello che contiene fit e predict non implementati
class Model():

    def fit(self, data):
        raise NotImplementedError("Metodo non ancora implementato")
    
    def predict(self, data):
        raise NotImplementedError("Metodo non ancora implementato")
    
    #mi serve per calcolare l'incremento medio su una serie di dati
    def incremento_medio(self, data):
        #controllo se ci sono i dati
        if len(data) <= 1:
            print('i dati inseriti non sono sufficienti per calcolare l incrementomedio')
            return None

        else:
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
    
    #l'incremento medio di tutti i dati più l'ultimo dato
    def predict(self, data):

        incr_medio = super().incremento_medio(data[-3:])
        prediction = data[-1] + incr_medio
        return prediction

class FitIncrementalModel(IncrementalModel):

    def fit(self, data):
        #Considero tutti i dati tranne quelli degli ultimi tre mesi(ultimi tre dati)
        data_first_moth = data[:-3]
        
        #Calcolo l'incremento medio dei primi mesi
        incr_first_moth = self.incremento_medio(data_first_moth)
        self.global_agv_increment = incr_first_moth
        return incr_first_moth


    def predict(self, data):
        #Prendo i dati degli ultimi tre mesi
        data_last_3moth = data[-3:]

        #incremento medio degli ultimi tre mesi
        incr_last_moth = self.incremento_medio(data_last_3moth)
        #media fra gli incrementi medi
        global_incr_medio = (self.global_agv_increment + incr_last_moth) / 2

        return data[-1] + global_incr_medio

#data originale e data predict sono entrambe solo le parte di dati che vengono valutate
def valutazione(data_originale, data_predict):
    if len(data_originale) == len(data_predict):
        
        all_differenze = []

        #scorro i dati dell'originale (i)
        for i , item in enumerate(data_originale):
            #calcolo la differenza con il dato originale
            differenza = item - data_predict[i]
            #la salvo in un array
            all_differenze.append(abs(differenza))
            print('vero: {}, predic: {} --> divverenza: {}'.format(item, data_predict[i], abs(differenza)))

        #sommo tutti i dati delle differenze e li divido per la lunchezza dell'array
        errore_medio = sum(all_differenze) / len(data_originale)
        #retorno l'errore medio
        return errore_medio

    else:
        print('Errore:\n   i dati passati a "valutazione" non vanno bene\n')
        return None

#==========================
#    CORPO DEL PROGRAMMA
#===========================

"""
my_file = CSVFile('file_prova_dati.csv')
print(my_file)
print(*my_file.get_data(), sep = '\n')

my_file = CSVFile('random_file.csv')
print(my_file)
print(*my_file.get_data(), sep = '\n')

my_file = CSVFile('shampoo_sales.csv')
print(my_file)
print(*my_file.get_data(), sep = '\n')

my_file = CSVFile('shampoo_sales_messed_up.csv')
print(my_file)
print(*my_file.get_data(), sep = '\n')

my_file = CSVFile('file_vuoto.csv')
print(my_file)
#print(*my_file.get_data(), sep = '\n')
"""


my_file = NumericalCSVFile('shampoo_sales.csv')
#print(my_file.get_data())

#divido i solo il numero di vendite
just_data = [elem[1] for elem in my_file.get_data()]
data_24_mesi = just_data[:24]
data_ultimi_12_mesi = just_data[24:]
print(data_ultimi_12_mesi)

#ogetti modelli
#vendite_shampoo = IncrementalModel()
#print(vendite_shampoo.predict(just_data))
#vendite_lol = FitIncrementalModel()

#array di dati con la predict dell'incremental modello
shampoo = data_24_mesi
while len(shampoo) != len(just_data):
    next_dato = IncrementalModel().predict(shampoo) 
    shampoo.append(next_dato)

print(shampoo)

#array di dati con la predict del fit incremental model
lol = data_24_mesi
while len(lol) != len(just_data):
    FitIncrementalModel().fit(lol)
    next_dato = FitIncrementalModel().predict(lol)
    lol.append(next_dato)

print(lol)

#gli errori medi
print('valutazione incrementalmodel')
errore_medio_shampoo = valutazione(data_ultimi_12_mesi, shampoo[24:])
print(errore_medio_shampoo)

print('valutazione FitIncrementalmodel')
errore_medio_lol = valutazione(data_ultimi_12_mesi, lol[24:])
print(errore_medio_lol)


"""
pyplot.plot(just_data + [vendite_shampoo.predict(just_data)], color = 'tab:red')
pyplot.plot(just_data + [vendite_lol.predict(just_data)], color = 'tab:green')
pyplot.plot(just_data, color = 'tab:blue')

pyplot.show()
"""

