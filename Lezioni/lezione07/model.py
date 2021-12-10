def sottrazione_lista(l1, l2):
    l_sott =[]
    for item in l1:
        if item not in l2:
            l_sott.appen(item)
    
    return l_sott

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
        data_last_3moth = data
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
data = [8, 19, 31, 41, 50, 52, 60]

print(pippo.fit(data))
print(pippo.predict(data))

from matplotlib import pyplot
pyplot.plot(data + pippo.predict(data), color='tab:red')
pyplot.plot(data, color='tab:blue')
pyplot.show()