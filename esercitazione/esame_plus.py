class ExamException(Exception):
    pass

class MovingAverage():

    def __init__(self, finestra):
        #controllo se finestra è un numero intero e se maggiore di zero

        if type(finestra) is not int:
            raise ExamException('Il valore inserito non è un intero')
        if finestra <= 0:
            raise ExamException('il numero è minore di zero')

        #variabile globale della finestra
        self.finestra = finestra

    def compute(self, dati):

        #controllo se i dati sono dei numeri, e non None 
        try:
            a = len(dati)
            for item in dati:
                a = float(item)
        except Exception:
            raise ExamException('Nel compute:\n    I dati non sono tutti numeri')
        #controllo se la lunghezza dei dati va bene
        if self.finestra > len(dati):
            raise ExamException('la lista data è troppo piccola')

        lunghezza = len(dati)
        medie_mobili = []

        #CALCOLO DELLA MEDIA MOBILE
        #considero dato per dato con i (da o a lunghezza dell'array - ???)
        for i in range(lunghezza - self.finestra + 1):
            #prendo finestra di numeri che mi servono
            dati_da_mediare = dati[i : i + self.finestra]
            #faccio la media
            media = sum(dati_da_mediare) / len(dati_da_mediare)
            #aggiungo all'array
            medie_mobili.append(media)

        #retorno l'array
        return medie_mobili

#8==========================D
#test

moving_avrage_test = MovingAverage(2)
result = moving_avrage_test.compute([2,4,8,16])
if result == [3, 6, 12]:
    print('test passato')
else:
    print('dio vecio\ntest non passato')
    print(result)

moving_avrage_test = MovingAverage(1)
result = moving_avrage_test.compute([2,4,8,16])
if result == [2, 4, 8, 16]:
    print('test passato')
else:
    print('dio vecio\ntest non passato')
    print(result)

#8==========================D


moving_avrage_test = MovingAverage(3)
result = moving_avrage_test.compute([2,4,8,16])
print(result)