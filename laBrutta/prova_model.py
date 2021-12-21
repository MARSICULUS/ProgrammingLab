class Model():

    def fit(self, data):
        raise NotImplementedError("Metodo non ancora implementato")
    
    def predict(self, data):
        raise NotImplementedError("Metodo non ancora implementato")
    
    #mi serve per calcolare l'incremento medio su una serie di dati
    def incremento_medio(self, data):
        #controllo se ci sono i dati
        if len(data) <= 1:
            print('i dati inseriti non sono sufficienti per calcolare l incrementomedio')
            return None

        else:
            #lunghezza dei dati
            lun = len(data)
            #incrementi
            incrementi = []

            for i, item in enumerate(data):
                if i < lun - 1:
                    incrementi.append(data[i + 1] - data[i])
            
            #incremento medio
            incr_medio = sum(incrementi) / len(incrementi)
            return incr_medio
            
        
class IncrementalModel(Model):
    
    #l'incremento medio di tutti i dati più l'ultimo dato
    def predict(self, data):

        incr_medio = super().incremento_medio(data[-3:])
        prediction = data[-1] + incr_medio
        return prediction

class FitIncrementalModel(IncrementalModel):

    def fit(self, data):
        #Considero tutti i dati tranne quelli degli ultimi tre mesi(ultimi tre dati)
        data_first_moth = []
        lun = len(data)
        for i in range(lun - 3):
            data_first_moth.append(data[i])
        
        #Calcolo l'incremento medio dei primi mesi
        incr_first_moth = self.incremento_medio(data_first_moth)
        self.global_agv_increment = incr_first_moth
        return incr_first_moth


    def predict(self, data):
        #Prendo i dati degli ultimi tre mesi
        index_last_3moth = len(data) - 3
        data_last_3moth = data[index_last_3moth:]

        #incremento medio degli ultimi tre mesi
        incr_last_moth = self.incremento_medio(data_last_3moth)
        #media fra gli incrementi medi
        global_incr_medio = (self.global_agv_increment + incr_last_moth) / 2

        return data[-1] + global_incr_medio

#data originale e data predict sono entrambe solo le parte di dati che vengono valutate
def valutazione(data_originale, data_predict):
    if len(data_originale) == len(data_predict):
        
        all_differenze = []

        #scorro i dati dell'originale (i)
        for i , item in enumerate(data_originale):
            #calcolo la differenza con il dato originale
            differenza = item - data_predict[i]
            #la salvo in un array
            all_differenze.append(abs(differenza))
            print('vero: {}, predic: {} --> divverenza: {}'.format(item, data_predict[i], abs(differenza)))

        #sommo tutti i dati delle differenze e li divido per la lunchezza dell'array
        errore_medio = sum(all_differenze) / len(data_originale)
        #retorno l'errore medio
        return errore_medio

    else:
        print('Errore:\n   i dati passati a "valutazione" non vanno bene\n')
        return None


dati = [8,19,31,41,50,52,60]

model_1 = IncrementalModel()
model_2 = FitIncrementalModel()

model_2.fit(dati)

print(dati)

print('pred 1')
print( model_1.predict(dati)) 
print('pred 2')
print( model_2.predict(dati))