class AidaError(Exception):
    pass

class Prova():

    def conversione(a):
        convertito = None
        try:
            convertito = float(a)
        except ValueError as e:
            raise AidaError ("errore di conversione\n{}".format(e))
        
        return convertito


#print(conversione('(lll'))