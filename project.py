#Se devo salvare errori particolari, non l'ho usata per adesso!!
class ErroreAida(Exception):
    pass

""" 
Classe CSVFile
Serve per leggere una classe CSV file

-attributi-
self.name -> nome del file
self.title -> intestazione del file
self.righe -> numero di righe del file
self.can_read -> se esiste il nome del file

-metodi-
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
        if type(nome_file) == str:
            if nome_file[-4:] == '.csv':
                t_input = True
            else:
                t_input = False
        else:
            t_input = False
        
        #se passa il test allora setto in nome
        if t_input:
            self.name = nome_file
        #altrimenti il file non si può leggere
        else:
            self.can_read = False

        #CAN_READ
        #Controllo se esiste il file
        if t_input:
            try:
                #provo ad aprirlo
                my_file = open(self.name, 'r')
                my_file.close()
                #quindi dico che si può aprire
                self.can_read = True
            except FileNotFoundError:
                #Se non esiste dico che non si può aprire
                print('il file "{}" non è stato TROVATO'.format(self.name))
                self.can_read = False

        #TITOLO e RIGHE
        #Quando il file si può leggere controllo se non è vuoto
        if self.can_read:
            my_file = open(self.name, 'r')
            titolo = my_file.readline().strip()
            #se il file non è vuoto
            if titolo != '':
                t_pieno = True
                #setto il titotlo e il numero di righe
                self.title = titolo
                self.righe = self.__conta_righe__()
            else:
                t_pieno = False
            my_file.close()
        
        #Quando il file non si può leggere o è vuoto
        if not self.can_read or not t_pieno:
            self.title = None
            self.righe = 0
             
    #Presentazione del file
    def __str__(self):
        pass

    def __conta_righe__(self):
        my_file = open(self.name, 'r')

        #Creo una lista di 1 per ogni riga che c'è nel file
        lst = [1 for i, line in enumerate(my_file) if i > 0 and line != '']

        my_file.close()
        return sum(lst)

    def get_data(self, start = None, end = None):
        pass
    
    def get_dates(self, start = None, end = None):
        pass
    

""" 
Classe NumericalCSVFile
"""

"""
Modello
"""