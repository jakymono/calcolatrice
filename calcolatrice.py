#calcolatrice
def controllo_int(testo_scelta):
    while True:
        try:
            intero=int(input(testo_scelta))
            break
        except:
            print("error, not int")
    return intero

def divisione():
    y=controllo_int("inscerisci il primo numero")
    x=controllo_int("inscerisci il secondo numero")
    somma=y/x
    return somma

def moltiplicazione():
    y=controllo_int("inscerisci il primo numero")
    x=controllo_int("inscerisci il secondo numero")
    somma=y*x
    return somma
