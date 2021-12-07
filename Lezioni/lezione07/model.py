class Model():
    def fit(self, data):
        raise NotImplementedError("Metodo non ancora implementato")
    
    def predict(self, data):
        raise NotImplementedError("Metodo non ancora implementato")
    
class IncrementalModel(Model):
    
    def predict(self, data):
        #controllo se ci sono i dati

        #lunghezza dei dati
        lun = len(data)
        #incrementi
        incrementi = []

        for i, item in enumerate(data):
            print(item)
            if i < lun - 1:
                incrementi.append(data[i + 1] - data[i])
        
        #incremento medio
        incr_medio = sum(incrementi) / len(incrementi)

        prediction = data[-1] + incr_medio
        return prediction

vendite_shampo = IncrementalModel()
data = [50, 52, 60]

print(vendite_shampo.predict(data))