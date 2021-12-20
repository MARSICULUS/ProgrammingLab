import unittest
from project import CSVFile
from project import FileVuoto

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
        self.assertFalse(test_file.can_read)

        #Se come nome del file non viene usata una stringa 
        self.assertFalse(CSVFile(69).can_read)

    def test_str(self):
        #Controllo se il file shampoo viene rappresentato in maniera corretta

        #Con il shampoo file
        test_file = CSVFile('shampoo_sales.csv')
        self.assertEqual(test_file.__str__(), '[----------]\nshampoo_sales.csv\n    Date,Sales\n    numero righe: 36\n')

        #Con un file insesistente
        test_file = CSVFile('file_inesistente.csv')
        self.assertEqual(test_file.__str__(), '[----------]\n"file_inesistente.csv" non è stato TROVATO o è VUOTO\n')

        #Con un file vuoto
        test_file = CSVFile('file_vuoto.csv')
        self.assertEqual(test_file.__str__(), '[----------]\n"file_vuoto.csv" non è stato TROVATO o è VUOTO\n')
    
    def test_get_data(self):
        data =  [['01-01-2012','100.0'],['01-02-2012','200.0'],['01-03-2012','300.0'],['01-04-2012','400.0'],['01-05-2012','500.0'],['01-06-2012','600.0'],['01-07-2012','700.0'],['01-08-2012','800.0'],['01-09-2012','900.0'],['01-10-2012','100.1'],['01-11-2012','100.2'],['01-12-2012','100.3']]
        self.assertEqual(CSVFile('file_prova_dati.csv').get_data(), data)
        test_file = CSVFile('file_vuoto.csv')
        self.assertRaises(FileVuoto, test_file.get_data(), )
        self.assertEqual(CSVFile('file_prova_dati.csv').get_data(6), data[5:])
        self.assertEqual(CSVFile('file_prova_dati.csv').get_data(3, 10), data[2:9])

    def test_get_dates(self):
        #raise Exception('Test non ancora IMPLEMENTATO')
        pass

    def test_conta_righe(self):
        self.assertEqual(CSVFile('shampoo_sales.csv').__conta_righe__(), 36)
        self.assertEqual(CSVFile('file_prova_dati.csv').__conta_righe__(), 12)
        self.assertEqual(CSVFile('file_vuoto.csv').__conta_righe__(), 0)