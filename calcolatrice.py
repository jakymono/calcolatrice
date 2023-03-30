# calcolatrice
def main():
    menu = """scegliere l'operazione:
    1. somma
    2. sottrazione
    3. divisione
    4. moltiplicazione
    5.potenza
    6.pulisci risultato
    7.fine"""
    tot = input("inserire il primo numero")
    while True:
        scelta = input(menu)
        match scelta:
            case 1:
                y = input("inserire nuovo il numero")
                tot = somma(tot,y)
            case 2:
                y = input("inserire il nuovo numero")
                tot = sottrazione(tot,y)
            case 3:
                y = input("inserire il nuovo numero")
                tot = divisione(tot,y)
            case 4:
                y = input("inserire il nuovo numero")
                tot = moltiplicazione(tot,y)
            case 5:
                y = input("inserire il nuovo numero")
                tot = potenza(tot,y)
            case 6:
                tot = 0
                tot = input("inserire il primo numero")
            case 7:
                print("arivederci")
                break
            case _:
                print("inserito numero non valido")
        input("premere un tasto per continuare..")

