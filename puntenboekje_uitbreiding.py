from tabulate import tabulate
from colorama import Fore, Style, init

# Initialiseer Colorama
init(autoreset=True)#default font

# Lijst van vakken
vakken = ["Leerling", "Wiskunde", "Nederlands", "Geschiedenis", "Biologie", "Engels"]

# Lijst van leerlingen en hun cijfers (per vak op 10)
data = [
    ["Alice", 7, 4, 9, 6, 5],  # Cijfers van Alice
    ["Bob", 9, 7, 8, 7, 6],    # Cijfers van Bob
    ["Charlie", 6, 4, 5, 7, 8],  # Cijfers van Charlie
    ["Diana", 10, 9, 9, 4, 7],  # Cijfers van Diana
    ["Eve", 8, 6, 7, 5, 9]      # Cijfers van Eve
]

# Functie om punten onder 5/10 rood te maken
def kleur_cijfers(cijfers):
    gekleurde_cijfers = []
    for leerling in cijfers:
        gekleurde_leerling = [leerling[0]]  # Eerste item is de naam, die laten we ongemoeid
        for punt in leerling[1:]:
            if punt < 5:  # Minder dan 5/10 (10/20)
                gekleurde_leerling.append(f"{Fore.RED}{punt}{Style.RESET_ALL}")
            else:
                gekleurde_leerling.append(str(punt))
        gekleurde_cijfers.append(gekleurde_leerling)
    return gekleurde_cijfers

# Functie om het totaal per leerling te berekenen en aan de tabel toe te voegen
def voeg_totale_cijfers_toe(cijfers):
    for leerling in cijfers:
        totaal = sum(leerling[1:]) * 2  # Totale punten op 100 (iedere score op 10 wordt x2 gedaan)
        leerling.append(totaal)
    if "Totaal (op 100)" not in vakken:
        vakken.append("Totaal (op 100)")  # Voeg een kolom "Totaal" toe aan de kopteksten

# Functie om het gemiddelde per vak te berekenen
def bereken_gemiddelde_per_vak(cijfers):
    gemiddelden = ["Gemiddelde"]
    aantal_leerlingen = len(cijfers)
    for i in range(1, len(vakken)-1):  # -1 omdat we de laatste kolom ("Totaal") niet meenemen
        som = sum([leerling[i] for leerling in cijfers])
        gemiddelde = som / aantal_leerlingen
        gemiddelden.append(f"{gemiddelde:.2f}") #.2f decimalen na de comma
    gemiddelden.append("")  # Geen totaal voor de gemiddelde rij
    return gemiddelden

# Functie om een leerling toe te voegen
def voeg_leerling_toe(cijfers, naam, punten):
    if len(punten) != len(vakken) - 1:  # -1 omdat de eerste kolom de naam is
        print("Aantal ingevoerde punten komt niet overeen met het aantal vakken.")
        return
    cijfers.append([naam] + punten)
    print(f"Leerling {naam} is toegevoegd.")

# Functie om een leerling te verwijderen
def verwijder_leerling(cijfers, naam):
    gevonden = False
    for i, leerling in enumerate(cijfers):
        if leerling[0] == naam:
            del cijfers[i]
            gevonden = True
            print(f"Leerling {naam} is verwijderd.")
            break
    if not gevonden:
        print(f"Leerling {naam} niet gevonden.")

# Functie om de tabel te printen
def print_tabel(cijfers, vakken):
    # Voeg totale cijfers toe voor elke leerling
    voeg_totale_cijfers_toe(cijfers)

    # Voeg kleuren toe aan de cijfers
    gekleurde_cijfers = kleur_cijfers(cijfers)

    # Voeg de gemiddelde rij toe
    gemiddelde_rij = bereken_gemiddelde_per_vak(cijfers)
    gekleurde_cijfers.append(gemiddelde_rij)

    # Print de tabel met tabulate
    print(tabulate(gekleurde_cijfers, headers=vakken, tablefmt="fancy_grid"))

# Testfuncties voor het toevoegen en verwijderen van leerlingen
def test_toevoegen_verwijderen_leerlingen():
    # Tabel printen voor toevoegen
    print("Originele Tabel:")
    print_tabel(data, vakken)

    # Voeg een nieuwe leerling toe
    nieuwe_leerling = "Frank"
    punten_frank = [5, 7, 6, 8, 4]  # Scores voor Wiskunde, Nederlands, Geschiedenis, Biologie, Engels
    voeg_leerling_toe(data, nieuwe_leerling, punten_frank)

    # Tabel na toevoegen van Frank
    print("\nTabel na toevoegen van Frank:")
    print_tabel(data, vakken)

    # Verwijder een leerling
    verwijder_leerling(data, "Charlie")

    # Tabel na verwijderen van Charlie
    print("\nTabel na verwijderen van Charlie:")
    print_tabel(data, vakken)

# Test de toevoeg- en verwijderfunctionaliteit
test_toevoegen_verwijderen_leerlingen()
