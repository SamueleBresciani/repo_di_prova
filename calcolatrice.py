scelta = -1
while(scelta!=0):
    print("Benvenuto nella nostra calcolatrice")
    print("Inseisci l'operazione che vuoi effettuare")
    scelta = int(input("1) Sottrazzione\n2) Addizzione\n0) Exit"))

    if scelta == 1:
        n_1 = int(input("inserisci il primo numero: "))
        n_2 = int(input("inserisci il secondo numero: "))
        risultato = n_1 - n_2
        print(f"{n_1} - {n_2} =  {risultato}")
    elif scelta == 2:
        n_1 = int(input("inserisci il primo numero: "))
        n_2 = int(input("inserisci il secondo numero: "))
        risultato = n_1 + n_2
        print(f"{n_1} + {n_2} =  {risultato}")
    else:
        print("Scelta non corretta!")