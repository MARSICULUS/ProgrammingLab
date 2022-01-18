class ExamException(Exception):
    pass

class Diff():

    def __init__(self, ratio = 1):

        #controllo se ratio va bene
        if ratio is None:
            raise ExamException('WTF dude')
        

        if type(ratio) is str:
            raise ExamException('La ratio non è un numero')

        self.ratio = ratio

        if self.ratio <= 0:
            raise ExamException('La ratio ha un valore sbagliato')

    
    def compute(self, dati):

        #contollo se dati va bene
        if dati is None:
            raise ExamException('non hai inserito nulla')
        if type(dati) is not type([]):
            raise ExamException('non hai inserito un array')
        if len(dati) < 2:
            raise ExamException('lista troppo corta')
        for item in dati:

            try:
                a = float(item)
                if item is None:
                    raise Exception

            except Exception:
                raise ExamException('i dati inseriti non sono validi')


        #CALCOLO la Diff
        #mi creo un arrey
        diff = []
        #prendo elemento per elemento i dati
        for i, item in enumerate(dati):
            #calcolo la differenza e li aggiungo ad un array
            if i == len(dati) - 1:
                break
            else:
                diff.append((dati[i + 1] - dati[i]) / self.ratio)
        
        return diff

#test
'''
a = [2, 4, 8, 16]
diff_test = Diff()
if diff_test.compute(a) != [2, 4, 8]:
    print('porco cane')
else:
    print('OK!')

a = [2, 4, 8, 16]
diff_test = Diff(2)
if diff_test.compute(a) != [1, 2, 4]:
    print('porco cane')
else:
    print('OK!')
    '''