class ExamException(Exception):
    pass

class CSVFile:

    #Inizializzazione
    def __init__(self, name):

        #setto il nome
        self.name = name
        
        #Controlo Se il nome è una stringa che finisce per .csv
        if type(name) != str:
           raise ExamException('Errore: il tipo del file non è .csv')

            
    #Presentazione del file
    def __str__(self):
        return '[----------]\n{}\n[----------]'.format(self.name)


    #Leggere i dati
    def get_data(self):

        #controllo se il file esiste
        try:
            my_file = open(self.name, 'r')
            my_file.close()
        except Exception:
            raise ExamException('Errore: il file non può essere aperto (inesistente)')

        #controllo che il file non sia vuoto
        my_file = open(self.name, 'r')
        vuoto = [1 for line in my_file if line != '\n' ]
        my_file.close()
        if sum(vuoto) < 1:
            raise ExamException('Errore: il file passato è vuoto')

        
        #Prendo tutti i dati così come sono tranne le righe vuote
        my_file = open(self.name, 'r')
        
        all_data = []

        for line in my_file:
            l = line.strip('\n')
            l = l.split(',')
            riga_vuota = True
            for colonna in l:
                if colonna != '':
                    riga_vuota = False
            if not riga_vuota:
                all_data.append(l)

        my_file.close()

        return all_data

class CSVTimeSeriesFile(CSVFile):

    #Lista di liste formata da coppia data-intero
    def get_data(self):
        old_data = super().get_data()
        floaty_data = []

        #Per ogni lista, se ci sono due dati il primo lo aggiungo
        #    il secondo lo converto in int
        for lista in old_data:
            if len(lista) >= 2:
                
                linea = []
                for i, item in enumerate(lista):
                    if i == 0:
                        linea.append(item)
                    if i == 1:
                        try:
                            floaty_item = int(item)
                            if floaty_item < 0:
                                raise Exception
                            linea.append(floaty_item)
                        except:
                            linea.append(None)
    
                if linea[0] == 'date':
                    pass
                else:
                    floaty_data.append(linea)

        if not self.__time_check__(floaty_data):
            raise ExamException('Errore: ordine temporale sbagliato')
                        
        return floaty_data

    def __time_check__(self, dati):

        tutto_a_posto = True

        #considero solo le date (le righe con None o testo non vanno considerate)
        only_date =[]
        for lista in dati:
            only_date.append(lista[0])

        right_data = []
        for item in only_date:
            try:
                l = item.split('-')
                if len(l) != 2:
                    raise Exception
                l[0] = int(l[0])
                l[1] = int(l[1])
                right_data.append(l)
            except:
                right_data.append(None)

        #tutte le date
        anni = []
        for item in right_data:
            try:
                anni.append(item[0])
            except:
                pass

                
        #Controllo prima tutti gli anni
        anni_a_posto = True
        for i, item in enumerate(anni):
            if i == len(anni) - 1:
                pass
            else:
                if item > anni[i + 1]:
                    anni_a_posto = False


                    
        #tutti i mesi
        mesi = []
        for item in right_data:
            try:
                mesi.append(item[1])
            except:
                pass

        #controllo tutti i mesi siano giusti
        mesi_a_posto = True
        for i, item in enumerate(mesi):
            if i < len(mesi) - 1:
                if mesi[i] >= mesi[i + 1]:
                    if mesi[i] == mesi[i + 1]:
                        mesi_a_posto = False
                    else:
                        if anni[i] == anni[i + 1]:
                            mesi_a_posto = False

        #return
        if mesi_a_posto and anni_a_posto:
            return True
        else:
            return False

def compute_avg_monthly_difference(time_series, first_year, last_year):

    if not isinstance(first_year, str) or not isinstance(first_year, str):
        raise ExamException('Errore: le date inserite non sono stringhe')
    
    try:
        first_year = int(first_year)
        last_year = int(last_year)
    except:
        raise ExamException('Errore: le date non sono del tipo giusto')

    if last_year < first_year:
        raise ExamException('Errore:  non si può tornare indietro nel tempo')
    

    modified_data = []
    for item in time_series:
        l = item[0].split('-')
        if len(l) == 2:
            l.append(item[1])
            modified_data.append(l)

    data = []
    for item in modified_data:
        linea = []
        add = True
        for i in range(2):
            try:
                linea.append(int(item[i]))
            except:
                add = False
        if add:
            linea.append(item[2])
            data.append(linea)

    
    wanted_data = []

    for item in data:
        if item is None:
            wanted_data.append(item)
        else:
            if item[0] >= first_year and item[0] <= last_year:
                wanted_data.append(item)
   
    
    passeggieri = []
    for i in range(12):
        mese = []
        for item in wanted_data:
            if item [1] == i + 1:
                mese.append(item[2])
        passeggieri.append(mese)

    print(passeggieri)

    
    difference_year = last_year - first_year + 1
    result = [0,0,0,0,0,0,0,0,0,0,0,0]    

    for i, mesi in enumerate(passeggieri):
        diff = 0
        counter = 0

        for j in range(len(mesi) - 1):
            if mesi[j] is None or mesi[j + 1] is None:
                pass
            else:
                diff = diff + abs(mesi[j] - mesi[j + 1])
                counter = counter + 1

        if diff == 0:
            result[i] = diff
        else:
            if counter == 0:
                result[i] = diff
            else:
                result[i] = diff / counter
    

    
    return result


file = CSVTimeSeriesFile(name = 'dati.csv')
print('get data:')
print(file.get_data())
print('.......')
print(compute_avg_monthly_difference(file.get_data(), '0', '20000'))