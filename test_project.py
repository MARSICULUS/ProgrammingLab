import unittest
from project import CSVFile
from project import FileVuoto
from project import NumericalCSVFile
from project import Model
from project import IncrementalModel
from project import FitIncrementalModel

"""
NOTE (DA CANCELLARE)

Con assertRaises controllo se viene fatta salire un eccezione ovvero controllo che il codice si pianta

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
        try:
            CSVFile('file_vuoto.csv').get_data()
        except FileVuoto:
            self.assertTrue(True)
        self.assertEqual(CSVFile('file_prova_dati.csv').get_data(6), data[5:])
        self.assertEqual(CSVFile('file_prova_dati.csv').get_data(3, 10), data[2:9])

    def test_get_dates(self):
        self.assertEqual(CSVFile('random_file.csv').get_dates(), [])

    def test_conta_righe(self):
        self.assertEqual(CSVFile('shampoo_sales.csv').__conta_righe__(), 36)
        self.assertEqual(CSVFile('file_prova_dati.csv').__conta_righe__(), 12)
        self.assertEqual(CSVFile('file_vuoto.csv').__conta_righe__(), 0)

    #--
    #NumericalCSVFile
    #--
    
    def test_get_floaty_data(self):
        data = [['01-01-2012',100.0],['01-02-2012',200.0],['01-03-2012',300.0],['01-04-2012',400.0],['01-05-2012',500.0],['01-06-2012',600.0],['01-07-2012',700.0],['01-08-2012',800.0],['01-09-2012',900.0],['01-10-2012',100.1],['01-11-2012',100.2],['01-12-2012',100.3]]
        self.assertEqual(NumericalCSVFile('file_prova_dati.csv').get_data(), data)

    #Model
    def test_model(self):
        dati = [50, 52, 60]
        self.assertEqual(Model().incremento_medio(dati), 5)
        shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]
        self.assertEqual(int(Model().incremento_medio(shampoo_sales)), 10)
        origin_dati = [67, 72]
        pred_dati = [65, 76]
        self.assertEqual(Model().valutazione(origin_dati, pred_dati), 3)
        self.assertEqual(Model().valutazione(dati, dati), 0)
        origin_dati = [8, 19, 31, 41, 50, 52, 60]
        pred_dati = [10, 21, 33, 43, 48, 50, 58]
        self.assertEqual(Model().valutazione(origin_dati, pred_dati), 2)

    def test_incremental_model(self):
        dati = [50, 52, 60]
        self.assertEqual(IncrementalModel().predict(dati), 65)

    def test_fitincremental_model(self):
        dati = [8, 19, 31, 41, 50, 52, 60]
        prova_fit_model = FitIncrementalModel()
        self.assertEqual(prova_fit_model.fit(dati), 11)
        self.assertEqual(prova_fit_model.predict(dati), 68)