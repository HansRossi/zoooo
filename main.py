# Tuto část dopiš

def pridej(zvire: str, pocet: int):
    global tygri,lvy,opice
    if pocet >= 0:
        if zvire == "tygri":
            tygri += pocet
            return tygri
        elif zvire == "lvy":
            lvy += pocet
            return lvy
        elif zvire == "opice":
            opice += pocet
            return opice
        else:
            print("Neco si zadal špatně")


def odeber(zvire: str, pocet: int):
    global tygri,lvy,opice
    if zvire == "tygri" and tygri >= 0:
        tygri -= pocet
        return tygri
    elif zvire == "lvy" and lvy >= 0:
        lvy -= pocet
        return lvy
    elif zvire == "opice" and opice >= 0:
        opice -= pocet
        return opice
    else:
        print("Neco si zadal špatně")


def vypis():
    global tygri, lvy, opice
    print(f"V zoo jsou {tygri} tygru, {lvy} lvu a {opice} opic")

# --------------------------------------------------------------------


# Tuto část nepřepisovat

# Počty zvířat v zoo
tygri = 0
lvy = 0
opice = 0

# informace pro cyklus zda se má opakovat či ne
opakovat = "ano"

while (opakovat == "ano"):

    # výpis akcí co lze provádět
    print("Vyberte jednu z akcí(pište pouze číslo): ")
    print("1. přidat zvíře")
    print("2. odebrat zvíře")
    print("3. vypsat seznam zvířat")

    # načtení akce od uživatele
    cislo = int(input())

    # Jednotlivá načtení potřebných informací a volání funkce
    if cislo == 1:
        zvire = input("Zadejte zvířata která chcete přidat(tygri,lvy,opice)")
        pocet = int(input("Zadejte počet těchto zvířat"))
        pridej(zvire, pocet)
    elif cislo == 2:
        zvire = input("Zadejte zvířata která chcete přidat(tygri,lvy,opice)")
        pocet = int(input("Zadejte počet těchto zvířat"))
        odeber(zvire, pocet)
    elif cislo == 3:
        vypis()

    # update proměnné opakovat, aby nedošlo k zacyklení programu
    opakovat = input("Chcete opakovat program?(ano/ne)")
