#Se devo salvare errori particolari, non l'ho usata per adesso!!
class ErroreAida(Execption):
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
    inizializza tutte le variabili

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

    def __init__(self):
        pass
    
    #presentazione del file
    def __str__(self):
        pass

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