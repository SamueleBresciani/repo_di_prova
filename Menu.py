while True:
    print("benvenuto nella nostra calcolatrice") 
    print("inserisci l'operazione che vuoi effettuare: ") 
    scelta =int(input("1)sottrazione\n2)addizione\n") )
    if scelta ==0 : 
        break 
    elif scelta==1: 
        sottrazzione()
    elif scelta==2: 
        somma()  
    else: 
        print("scelta non corretta !!")
