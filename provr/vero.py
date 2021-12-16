class AidaError(Exception):
    pass
'''
def conversione(a):
    convertito = None
    if:
        convertito = float(a)
    except ValueError as e:
        print ("errore di conversione\n{}".format(e))
    
    return convertito
'''
def conversione(a):
    return float(a)

print(conversione('(lll'))