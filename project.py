from datetime import datetime

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
      
    
    def get_dates(self, start = None, end = None):
        all_data = self.get_data()
        all_date = []
        for i, item in enumerate(all_data):
            #la data la trasformo in un data_object
            try:
                tempo = datetime.strptime(item[0], "%d-%m-%Y")
                item[0] = tempo
                all_date.append(item)
            except ValueError:
                print('La CONVERSIONE in data della riga {} non ha avuto sucesso\n    contenuto prima colonna: {}'.format(i, item[0]))

        
        return all_date 
    

""" 
Classe NumericalCSVFile
"""

"""
Modello
"""

#==========================
#    CORPO DEL PROGRAMMA
#===========================

#my_file = CSVFile('shampoo_sales.csv')
#print(my_file)
#print(*my_file.get_dates(), sep = '\n')