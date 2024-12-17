import calcolatrice as clc
while True:
    print("benvenuto nella nostra calcolatrice") 
    print("inserisci l'operazione che vuoi effettuare: ") 
    scelta =int(input("1)sottrazione\n2)addizione\n") )
    if scelta ==0 : 
        break 
    elif scelta==1: 
        clc.sottrazzione()
    elif scelta==2: 
        clc.somma()  
    else: 
        print("scelta non corretta !!")
