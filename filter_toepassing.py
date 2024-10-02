from tabulate import tabulate

# Lijst van voornamen, leeftijden en woonplaatsen in Belgisch Limburg
personen = [
    ["John", 28, "Hasselt"],
    ["Lisa", 34, "Genk"],
    ["Mark", 22, "Maasmechelen"],
    ["Anna", 29, "Bree"],
    ["Tom", 31, "Hasselt"],
    ["Sophie", 27, "Bilzen"],
    ["Peter", 30, "Genk"],
    ["Laura", 25, "Lommel"],
    ["David", 32, "Tongeren"],
    ["Maria", 33, "Maasmechelen"],
    ["James", 26, "Lanaken"],
    ["Emma", 29, "Hasselt"],
    ["Michael", 24, "Borgloon"],
    ["Sarah", 27, "Bilzen"],
    ["Chris", 35, "Lommel"]
]

# Kolomkoppen voor overzicht
kolommen = ["Voornaam", "Leeftijd", "Woonplaats"]


# Functie om personen uit een bepaalde gemeente te tonen
def toon_personen_uit_gemeente(gemeente):
    gefilterde_personen = []

    # Gebruik een normale for-loop om de lijst te doorlopen
    for persoon in personen:
        if persoon[2] == gemeente:
            gefilterde_personen.append(persoon)

    # Print de resultaten
    if gefilterde_personen:# als er minstens 1 item in lijst is.
        print(f"\nPersonen uit {gemeente}:")
        print(tabulate(gefilterde_personen, headers=kolommen, tablefmt="pretty_grid"))
    else:
        print(f"\nGeen personen gevonden in {gemeente}.")


# Vraag de gebruiker om een gemeente in te voeren
gemeente_input = input("Voer de naam van een gemeente in: ")
toon_personen_uit_gemeente(gemeente_input)
