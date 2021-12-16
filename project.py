#Se devo salvare errori particolari, non l'ho usata per adesso!!
class ErroreAida(Exception):
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
    #NON IMPLEMENTATO

__conta_righe__
    conta quante righe ci sono in un file
    non conta righe vuote
    #NON IMPLEMENTATO

get_data
    ritorna una lista di liste, le liste più piccole contengono le righe nelle quali ogni elemento rappresenta una colonna
    #NON IMPLEMENTATO

get_dates
    converte la lista di liste di get_data in una lista di liste, dove le date sono effettivamente l'oggetto datatime
    #NON IMPLEMENTATO
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
                my_file.close()
                #quindi dico che si può aprire
                self.can_read = True
            except FileNotFoundError:
                #Se non esiste dico che non si può aprire
                #così nei test il messaggio di errore non viene visto
                if __name__ == '__main__':
                    print('\n-lol-\nIl file "{}" non è stato TROVATO\n-lol-\n'.format(self.name))
                self.can_read = False
        else:
            self.can_read = False

        #TITOLO e RIGHE
        #Quando il file si può leggere controllo se non è vuoto
        if self.can_read:
            #Apro il file e prendo il titolo
            my_file = open(self.name, 'r')
            titolo = my_file.readline().strip()
            seconda_riga = my_file.readline().strip()
            #se il file non è vuoto
            if titolo != '' and seconda_riga != '':
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

        #Se il file è leggibile o è vuoto
        if self.can_read and self.righe > 0:
            return '[----------]\n{}\n    {}\n    numero righe: {}\n'.format(self.name, self.title, self.righe)
        #Se il file è leggibile ed è vuoto (non viene visualizzato il titolo)
        elif self.can_read and self.righe == 0:
            return '[----------]\n{}\n    numero righe: {}\n'.format(self.name, self.righe)
        else:
            return '[----------]\n"{}" non è stato TROVATO\n'.format(self.name)
             

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

#==========================
#    CORPO DEL PROGRAMMA
#===========================

my_file = CSVFile('lol.csv')
print(my_file)