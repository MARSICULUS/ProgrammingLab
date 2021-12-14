
#==============================
#  Classe per file CSV
#==============================

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self):
        
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []
    
            # Apro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
                
                # Posso anche pulire il carattere di newline 
                # dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()
                
                # p.s. in realta' strip() toglie anche gli spazi
                # bianchi all'inizio e alla fine di una stringa.
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'Date':
                        
                    # Aggiungo alla lista gli elementi di questa linea
                    data.append(elements)
            
            # Chiudo il file
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data



#==============================
# Classe per file NumericalCSV
#==============================

class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        
        # Chiamo la get_data del genitore 
        string_data = super().get_data()
        
        # Preparo lista per contenere i dati ma in formato numerico
        numerical_data = []
        
        # Ciclo su tutte le "righe" corrispondenti al file originale 
        for string_row in string_data:
            
            # Preparo una lista di supporto per salvare la riga
            # in "formato" nuumerico (tranne il primo elemento)
            numerical_row = []
            
            # Ciclo su tutti gli elementi della riga con un
            # enumeratore: cosi' ho gratis l'indice "i" della
            # posizione dell'elemento nella riga.
            for i,element in enumerate(string_row):
                
                if i == 0:
                    # Il primo elemento della riga lo lascio in formato stringa
                    numerical_row.append(element)
                    
                else:
                    # Converto a float tutto gli altri. Ma se fallisco, stampo
                    # l'errore e rompo il ciclo (e poi saltero' la riga).
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                
            # Alla fine aggiungo la riga in formato numerico alla lista
            # "esterna", ma solo se sono riuscito a processare tutti gli
            # elementi. Qui controllo per la lunghezza, ma avrei anche potuto
            # usare una variabile di supporto o fare due break in cascata.
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data

class Model():

    def fit(self, data):
        pass
    
    def predict(self, data):
        pass


class IncrementModel(Model):

    def __str__(self):
        return 'IncrementModel'

    def compute_avg_increment(self, data):
        # Variabile di supporto per il valore precedente
        prev_item = None

        # Preparo una variabile di supporto per calcolare l'incremento medio
        increments = 0
        
        # Processo i mesi in input su cui fare la predizione
        for item in data:

            # Caloclo l'incremento ma non se son o al primo
            # giro ovvero se non e' definito il "prev_item"
            if prev_item is not None:
                increments += item - prev_item

            # Assegno questo valore come precedente
            prev_item = item

        # Calcolo l'incremento medio divivendo la somam degli incrmenti sul totale dei dati (meno uno)
        avg_increment = increments / (len(data)-1)
        
        return avg_increment

    def predict(self, predict_data):
        
        #Calcolo l'incremento medio sui dati della predict
        avg_increment = self.compute_avg_increment(predict_data)

        # Torno la predizione (incremento medio sommato all'ultimo valore)
        return predict_data[-1] + avg_increment


class FitIncrementModel(IncrementModel):

    def __str__(self):
        return 'FitIncrementModel'

    def fit(self, fit_data):

        # Calcolo l'incremento medio sui dati di fit
        self.global_avg_increment = self.compute_avg_increment(fit_data)

    def predict(self, predict_data):
        
        # Chiamo la predict della classe genitore "IncrementModel"
        parent_prediction = super().predict(predict_data)

        # Sottraggo l'ultimo valore alla predizione del genitore
        # cosi' da avre l'incremento "originale"
        parent_predict_increment = parent_prediction - predict_data[-1]

        # Ora medio l'incremento del fit con quello della predict
        prediction_increment = (self.global_avg_increment + parent_predict_increment) / 2

        # E lo ri-sommo all'ultimo elemento
        prediction = predict_data[-1] + prediction_increment

        return prediction


#=========================================#
#        Corpo del programma              #
#=========================================#

# Mini-dataset di test
test_fit_data = [8,19,31,41]
test_predict_data = [50,52,60]

# Test rapido su IncrementModel (non unit test in questo caso)
increment_model = IncrementModel()
prediction = increment_model.predict(test_predict_data) 
if not prediction == 65:
    raise Exception('IncrementModel sul dataset di test non mi torna 65 ma "{}"'.format(prediction))
else:
    print('IncrementModel test passed')

# Test rapido su FitIncrementModel (non unit test in questo caso)
fit_increment_model = FitIncrementModel()
fit_increment_model.fit(test_fit_data)
prediction = fit_increment_model.predict(test_predict_data)
if not prediction == 68:
    raise Exception('FitIncrementModel sul dataset di test non mi torna 68 ma "{}"'.format(prediction))
else:
    print('FitIncrementModel test passed')

# Linea vuota
print('')
 

# I dati delle mie vendite di shampoo. In questo caso le sto direttamente scrivendo nel codice,
# ma nella realta' avrei usato l'oggetto CSVFile e caricato i dati dal file. Ma cosi' evito di
# avere troppe cose su cui sto lavorando assieme, e visto che i dati sono piccoli, posso farlo
# ed e' comodo (se avevo migliaia di valori forse era meglio di no).
shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

# Definiscxo quanti mesi usare per la valutazione
# che verranno sottratti al dataset nel caso del fit
eval_months = 12
cutoff_month = len(shampoo_sales) - eval_months

# Istanzio nuovo modello senza fit
increment_model = IncrementModel()

# Istanzio nuovo modello con fit
fit_increment_model = FitIncrementModel()
# Fitto sui dati fino al mese di cutoff
fit_increment_model.fit(shampoo_sales[0:cutoff_month])

# Metto entrambi i modelli in una lista
models = [increment_model, fit_increment_model]

# Swicth per il plot (se messo a True bisogna chiudere la finestra del plot 
# per far proseguire il programma dopo la valutazione del primo modello)
plot = False

# Valuto entrambi i modelli
for model in models:

    error = 0
    print('Evaluating model "{}"'.format(model))

    # Predizioni sul dataset di "valutazione" ovvero le vendite
    # dello shampoo dal mese di cutoff in poi
    predictions = []
    for i in range(eval_months):
        predict_data = shampoo_sales[cutoff_month+i-3-1:cutoff_month+i-1]
        prediction = model.predict(predict_data)
        real = shampoo_sales[cutoff_month+i]
        print('"{}" (pred) vs "{}" (real)'.format(int(prediction), int(real)))

        # Aggiungo se volessi poi plottare
        predictions.append(prediction)

        error += abs(prediction - shampoo_sales[cutoff_month+i])
    
    error = error / eval_months

    print('Average error: "{}"\n'.format(error))

    # Plotto se richiesto
    if plot:
        from matplotlib import  pyplot
        pyplot.plot(shampoo_sales[0:cutoff_month] + predictions, color='tab:red')
        pyplot.plot(shampoo_sales, color='tab:blue')
        pyplot.show()
