import unittest
from prog_lab import CSVFile

class TestCSVFile(unittest.TestCase):

    def test_init(self):
        csv_file = CSVFile("shampoo_sales.csv")

        #controllo che gli attributi vengano salvati correttamente
        #controllo nome
        self.assertEqual(csv_file.name, 'shampoo_sales.csv')
        #controllo titolo
        self.assertEqual(csv_file.title, 'Date,Sales')

        csv_file = CSVFile('shampoo_sales_default.csv')
        #controllo che gli attributi vengano salvati correttamente
        #controllo nome
        self.assertEqual(csv_file.name, 'shampoo_sales_default.csv')
        #controllo titolo
        self.assertEqual(csv_file.title, 'Data,Sales,Buh')

    def test_conta_righe(self):
        csv_file = CSVFile("shampoo_sales.csv")
        self.assertEqual(csv_file.__conta_righe__('shampoo_sales.csv'), 37)

        csv_file = CSVFile("shampoo_sales_default.csv")        
        self.assertEqual(csv_file.__conta_righe__('shampoo_sales_default.csv'), 1)
    
    def test_str(self):
        csv_file = CSVFile("shampoo_sales.csv")

        self.assertEqual(csv_file.__str__(), '_______\nNome file: shampoo_sales.csv\nTitolo: Date,Sales')
    
    def test_get_data(self):
        csv_file = CSVFile("shampoo_sales.csv")
        all_data = csv_file.get_data()

        self.assertEqual(all_data[0], ['01-01-2012','266.0'])
        self.assertEqual(all_data[5], ['01-06-2012','168.5'])