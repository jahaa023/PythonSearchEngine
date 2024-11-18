import os

# Henter hver ord og linje i en tekstfil, og setter det i en set i en liste, hvor den første verdien er linjenummeret, og den andre verdien er ordet
def lesInnTekst(filnavn):
    reader = open(f"./txt/{filnavn}", "r")
    line_number = 0
    global list
    list = []
    for line in reader:
        line_number += 1
        temp_list = line.split()
        for element in temp_list:
            list_set = set([line_number, element])
            list.append(list_set)
    global list_lower
    list_lower = []
    for element in list:
        for element2 in element:
            if (isinstance(element2, str)):
                list_lower.append(element2.lower())
    reader.close()

# Skriver ut ordene i tekstfilen, med linjenummer ved siden av
def printTekst():
    reader = open(f"./txt/{tekstfil}", "r")
    count = 0
    with reader as file:
        for line in file:
            count += 1
            print(str(count) + ": " + line.rstrip())

# Leter etter ord i liste og printer ut ordet hvis den blir funnet
def printOrd(ord):
    ord_lower = ord.lower()
    try:
        list_lower.index(ord_lower)
        print(ord)
    except ValueError:
        print("Kunne ikke finne ord")

# Leter etter ord i liste og sier om ordet finnes eller ikke
def finnOrd(ord):
    ord_lower = ord.lower()
    try:
        list_lower.index(ord_lower)
        print("Fant ord")
    except ValueError:
        print("Kunne ikke finne ord")

# Leter etter ordet i listen, og sjekker hva linjenummeret er for det ordet
def finnLinje(ord):
    ord_lower = ord.lower()
    ord_funnet = False
    list_of_lines = []
    for element in list:
        for element2 in element:
            if (isinstance(element2, str)):
                set_ord = element2.lower()
                if (set_ord == ord_lower):
                    ord_funnet = True
                    list_of_lines.append(line_number)
            else:
                line_number = element2
    if (ord_funnet == True):
        print(f"Fant ordet '{ord}' i disse linjene:")
        for linje_nummer in list_of_lines:
            print(linje_nummer)
    else:
        print("Kunne ikke finne dette ordet.")

# Teller antall ganger ett ord kommer opp i listen
def tellOrd(ord):
    count = 0
    ord_lower = ord.lower()
    for element in list_lower:
        if (element == ord_lower):
            count +=1
    if (count > 0):
        if (count == 1):
            print(f"Ordet '{ord}' kom opp 1 gang.")
        else :
            print(f"Ordet '{ord}' kom opp {count} ganger.")
    else:
        print(f"Ordet '{ord}' kom aldri")

# Spør brukeren om å velg hvilken tekstfil de vil søke fra
def velgTxtFil():
    if (os.path.exists("txt") == False or len(os.listdir("txt")) == 0):
        print ("'txt' mappen finnes ikke eller er tom.")
    else :
        print("Velg .txt fil å søke fra:")
        count = 0
        filename_list = []
        for filename in os.listdir('txt'):
            if os.path.isfile("txt/" + filename):
                count += 1
                filename_list.append(filename)
                print(f"{count}: {filename}")
        while (True):
            try:
                answer = int(input("Velg ett tall fra listen: "))
                if (answer not in range(1, (len(filename_list) + 1))):
                    print("Ugyldig svar")
                    continue
                else:
                    break
            except ValueError:
                print("Ugyldig svar")
                continue
        global tekstfil
        tekstfil = filename_list[(answer - 1)]
        lesInnTekst(tekstfil)
        hovedMeny()

# Printer ut en hovedmeny hvor brukeren kan navigere rundt
def hovedMeny():
    os.system("cls")
    print(f"Nåværende txt fil: {tekstfil}")
    print(
        "|------------------Hovedmeny-----------------| \n"
        "| 1. Print ut innhold i filen med linjenummer| \n"
        "| 2. Print ord                               | \n"
        "| 3. Finn ord                                | \n"
        "| 4. Finn linje                              | \n"
        "| 5. Tell ord                                | \n"
        "| 6. Endre txt fil                           | \n"
        "| 7. Avslutt                                 | \n"
        "|--------------------------------------------| \n"
        )
    while (True):
        try:
            valg = int(input("Velg ett tall fra menyen: "))
            if (valg not in range(1, 8)):
                print("Ugyldig svar")
                continue
            else:
                break
        except ValueError:
            print("Ugyldig svar")
    os.system("cls")
    if (valg == 1):
        printTekst()
    elif (valg == 2):
        ord = input("Skriv ord å printe ut: ")
        printOrd(ord)
    elif (valg == 3):
        ord = input("Skriv et ord for å sjekke om det finnes: ")
        finnOrd(ord)
    elif (valg == 4):
        ord = input("Skriv et ord å finne linjen til: ")
        finnLinje(ord)
    elif (valg == 5):
        ord = input("Skriv et ord å telle: ")
        tellOrd(ord)
    elif (valg == 6):
        velgTxtFil()
    elif (valg == 7):
        exit()
    
    input("Trykk Enter for å gå videre. ")
    hovedMeny()

# TODO: Search query: highlight every place where the input is found

velgTxtFil()