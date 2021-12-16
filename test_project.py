import unittest
from project import CSVFile

"""
NOTE (DA CANCELLARE)

Con asserRaises controllo se viene fatta salire un eccezione ovvero controllo che il codice si pianta

Se voglio controllare che il codice non si pianta immagino che devo controllare che l'eccezione viene gestita correttamente

consiglio abdula
sanitizzazione dell'input prima della gestione dell'errore
"""

class TestCSVFile(unittest.TestCase):

    def test_init(self):
        #Contollo se tutte le variabili vengono salvate in modo corretto

        #Con il shampoo_sales.csv
        test_file = CSVFile('shampoo_sales.csv')
        self.assertEqual(test_file.name, 'shampoo_sales.csv')
        self.assertEqual(test_file.title, 'Date,Sales')
        self.assertEqual(test_file.righe, 36)
        self.assertTrue(test_file.can_read)

        #Con un file inesistente
        self.assertFalse(CSVFile('file_inesistente.csv').can_read)

        #Con un file vuoto
        test_file = CSVFile('file_vuoto.csv')
        self.assertEqual(test_file.name, 'file_vuoto.csv')
        self.assertEqual(test_file.title, None)
        self.assertEqual(test_file.righe, 0)
        self.assertTrue(test_file.can_read)

        #Se come nome del file non viene usata una stringa 
        self.assertFalse(CSVFile(69).can_read)

    def test_str(self):
        #Controllo se il file shampoo viene rappresentato in maniera corretta

        #Con il shampoo file
        test_file = CSVFile('shampoo_sales.csv')
        self.assertEqual(test_file.__str__(), '[----------]\nshampoo_sales.csv\n    Date,Sales\n    numero righe: 36\n')

        #Con un file insesistente
        test_file = CSVFile('file_inesistente.csv')
        self.assertEqual(test_file.__str__(), '[----------]\n"file_inesistente.csv" non è stato TROVATO\n')

        #Con un file vuoto
        test_file = CSVFile('file_vuoto.csv')
        self.assertEqual(test_file.__str__(), '[----------]\nfile_vuoto.csv\n    numero righe: 0\n')
    
    def test_get_data(self):
        raise Exception('Test non ancora IMPLEMENTATO')

    def test_get_dates(self):
        raise Exception('Test non ancora IMPLEMENTATO')

    def test_conta_righe(self):
        raise Exception('Test non ancora IMPLEMENTATO')