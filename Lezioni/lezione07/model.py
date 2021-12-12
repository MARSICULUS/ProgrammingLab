from matplotlib import pyplot

class Model():
    def fit(self, data):
        raise NotImplementedError("Metodo non ancora implementato")
    
    def predict(self, data):
        raise NotImplementedError("Metodo non ancora implementato")

    def incremento_medio(self, data):
        #controllo se ci sono i dati

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
    
    def predict(self, data):

        incr_medio = incremento_medio(data)
        prediction = data[-1] + incr_medio
        return prediction

class FitIncrementalModel(IncrementalModel):

    def predict(self, data):
        #faccio un array
        data_last_3moth = []
        for item in data:
            data_last_3moth.append(item)

        while len(data_last_3moth) > 3:
            data_last_3moth.pop(0)

        incr_last_moth = self.incremento_medio(data_last_3moth)

        global_incr_medio = (self.global_agv_increment + incr_last_moth) / 2

        return data[-1] + global_incr_medio


    def fit(self, data):
        data_first_moth = []
        lun = len(data)
        for i in range(lun - 3):
            data_first_moth.append(data[i])
        
        incr_first_moth = self.incremento_medio(data_first_moth)
        self.global_agv_increment = incr_first_moth
        return incr_first_moth

pippo = FitIncrementalModel()
dati = [8, 19, 31, 41, 50, 52, 60]

print(pippo.fit(dati))
print(dati)
dati.append(pippo.predict(dati))
print(dati)


print('halo?')
pyplot.plot(dati + [pippo.predict(dati)], color='tab:red')
pyplot.plot(dati, color='tab:blue')
pyplot.show()
print('halo?')
print(pippo.fit(dati))
dati.append(pippo.predict(dati))