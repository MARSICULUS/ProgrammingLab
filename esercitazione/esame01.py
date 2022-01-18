class ExamException(Exception):
    pass

class MovingAverage():

    def __init__(self, finestra):
        #controllo se finestra è un numero
        try:
            a = float(finestra)
        except Exception:
            print('La finestra data: {} non è un numero'.format(finestra))
            raise ExamException('Nell inizializzazione:\n    La finestra data non è un numero')
        #provo se finestra è un int e maggiore di zero
        if type(finestra) is not int:
            raise ExamException('il numero non è un itero')
        if finestra <= 0:
            raise ExamException('il numero è minore di zero')
        #variabile globale della finestra
        self.finestra = finestra

    def media_lista(self, dati):
        return (sum(dati) / len(dati))

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
        for i, dato in enumerate(dati):
            if(i <= lunghezza - self.finestra):
                #media fra i idue numeri
                #prendo n(fimestra) di numeri che mi servono
                dati_da_mediare = []
                for n in range(self.finestra):
                    dati_da_mediare.append(dati[i + n])
                #aggiungo la media a un array
                media = self.media_lista(dati_da_mediare)
                medie_mobili.append(media)
            else:
                break



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

moving_avrage_test = MovingAverage(1)
result = moving_avrage_test.compute([2,4,8,16])
if result == [2, 4, 8, 16]:
    print('test passato')
else:
    print('dio vecio\ntest non passato')

#8==========================D
