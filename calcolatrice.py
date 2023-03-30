# calcolatrice
import os


def main():
    menu = """scegliere l'operazione:
    1. somma
    2. sottrazione
    3. divisione
    4. moltiplicazione
    5.potenza
    6.pulisci risultato
    7.fine"""
    tot = inputnumeroint("inserire il primo numero")
    while True:
        os.system("CLS")
        print(tot)
        scelta = inputnumeroint(menu)
        match scelta:
            case 1:
                y = inputnumeroint("inserire nuovo il numero")
                tot = somma(tot,y)
            case 2:
                y = inputnumeroint("inserire il nuovo numero")
                tot = sottrazione(tot,y)
            case 3:
                y = inputnumeroint("inserire il nuovo numero")
                tot = divisione(tot,y)
            case 4:
                y = inputnumeroint("inserire il nuovo numero")
                tot = moltiplicazione(tot,y)
            case 5:
                y = inputnumeroint("inserire il nuovo numero")
                tot = potenza(tot,y)
            case 6:
                tot = 0
                tot = inputnumeroint("inserire il primo numero")
            case 7:
                print("arivederci")
                break
            case _:
                print("inserito numero non valido")
        input("premere un tasto per continuare..")

def inputnumeroint(st):
#controllo dell imput
    while True:
        try:
            print(st)
            n = int(input(" :   "))
            break
        except:
            print("qualcosa è andato storto riprovare...")
    return n  
        
        
        
#alessando
def somma(x,y):
	return x+y
  
def sottrazione(x,y):
	return x-y
def potenza(x,y):
	return x**y
#roberto
def divisione(x,y):
    somma=x/y
    return somma

def moltiplicazione(x,y):
    somma=x*y
    return somma

main()
