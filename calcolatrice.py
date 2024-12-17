def somma():  
    n_1=int(input("inserisci il primo numero !")) 
        n_2=int(input("inserisci il secondo numero !")) 
        risultato=n_1+n_2
        print(f"{n_1}+{n_2}={risultato}")
while True:
    print("benvenuto nella nostra calcolatrice") 
    print("inserisci l'operazione che vuoi effettuare: ") 
    scelta =int(input("1)sottrazione\n2)addizione\n") )
    if scelta ==0 : 
        break 
    elif scelta==1: 
        n_1=int(input("inserisci il primo numero !")) 
        n_2=int(input("inserisci il secondo numero !")) 
        risultato=n_1-n_2
        print(f"{n_1}-{n_2}={risultato}")
 
    elif scelta==2: 
          somma()  
    else: 
        print("scelta non corretta !!")
