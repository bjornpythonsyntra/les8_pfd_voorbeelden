from tabulate import tabulate


# Lijst van dagen
dagen = ["Loper", "Dag 1", "Dag 2", "Dag 3"]

# Lijst van lopers en hun afstanden (in kilometers)
lopers = [
    ["Alice", 5, 7, 6],
    ["Bob", 6, 8, 7],
    ["Charlie", 4, 6, 5],
    ["Diana", 7, 8, 9]
]

# Functie om het totaal per loper te berekenen en aan de tabel toe te voegen
def voeg_totale_lopers_toe(lopers):
    for loper in lopers:
        totaal = sum(loper[1:])  # Totale kilometers
        loper.append(totaal)
    if "Totaal (km)" not in dagen:
        dagen.append("Totaal (km)")  # Voeg een kolom "Totaal" toe aan de kopteksten

# Functie om het totaal per dag te berekenen
def bereken_totaal_per_dag(lopers):
    totaal_per_dag = ["Totaal per dag"]
    for i in range(1, len(dagen) - 1):  # -1 omdat we de laatste kolom ("Totaal") niet meenemen
        totaal = sum([loper[i] for loper in lopers])
        totaal_per_dag.append(totaal)
    totaal_per_dag.append("")  # Geen totaal voor de "Totaal" kolom
    return totaal_per_dag

# Functie om een loper toe te voegen
def voeg_loper_toe(lopers, naam, kilometers):
    if len(kilometers) != len(dagen) - 1:  # -1 omdat de eerste kolom de naam is
        print("Aantal ingevoerde dagen komt niet overeen met het aantal dagen.")
        return
    lopers.append([naam] + kilometers)
    print(f"Loper {naam} is toegevoegd.")

# Functie om een loper te verwijderen
def verwijder_loper(lopers, naam):
    gevonden = False
    for i, loper in enumerate(lopers):
        if loper[0] == naam:
            del lopers[i]
            gevonden = True
            print(f"Loper {naam} is verwijderd.")
            break
    if not gevonden:
        print(f"Loper {naam} niet gevonden.")

# Functie om het totaal van alle lopers samen te berekenen
def totaal_alle_lopers(lopers):
    totaal = sum([sum(loper[1:]) for loper in lopers])
    return totaal

# Functie om de statistieken per dag te berekenen (som, max, min, gemiddelde)
def bereken_statistieken_per_dag(lopers):
    statistieken = [["Dag", "Som", "Max", "Min", "Gemiddelde"]]
    for i in range(1, len(dagen) - 1):  # Voor elke dag
        dag_kilometers = [loper[i] for loper in lopers]
        som = sum(dag_kilometers)
        maximum = max(dag_kilometers)
        minimum = min(dag_kilometers)
        gemiddelde = som / len(lopers)
        statistieken.append([f"Dag {i}", som, maximum, minimum, f"{gemiddelde:.2f}"])
    return statistieken

# Functie om de tabel te printen
def print_tabel(lopers, dagen):
    # Voeg totale kilometers toe voor elke loper
    voeg_totale_lopers_toe(lopers)

    # Voeg de rij "Totaal per dag" toe
    totaal_per_dag = bereken_totaal_per_dag(lopers)
    lopers.append(totaal_per_dag)

    # Print de tabel met tabulate
    print(tabulate(lopers, headers=dagen, tablefmt="grid"))

    # Verwijder de "Totaal per dag" rij om de data consistent te houden voor verdere berekeningen
    lopers.pop()

# Functie om de statistiekentabel te printen
def print_statistieken_tabel(lopers):
    statistieken = bereken_statistieken_per_dag(lopers)
    print("\nStatistieken per dag:")
    print(tabulate(statistieken, headers="firstrow", tablefmt="grid"))

# Testfuncties voor het toevoegen en verwijderen van lopers en het berekenen van statistieken
def test_lopers():
    # Tabel printen voor toevoegen
    print("Originele Tabel:")
    print_tabel(lopers, dagen)

    # Voeg een nieuwe loper toe
    nieuwe_loper = "Frank"
    kilometers_frank = [6, 7, 5]  # Gelopen kilometers voor Dag 1, Dag 2, Dag 3
    voeg_loper_toe(lopers, nieuwe_loper, kilometers_frank)

    # Tabel na toevoegen van Frank
    print("\nTabel na toevoegen van Frank:")
    print_tabel(lopers, dagen)

    # Verwijder een loper
    verwijder_loper(lopers, "Charlie")

    # Tabel na verwijderen van Charlie
    print("\nTabel na verwijderen van Charlie:")
    print_tabel(lopers, dagen)

    # Totaal van alle lopers
    totaal = totaal_alle_lopers(lopers)
    print(f"\nTotaal door alle lopers gelopen: {totaal} km")

    # Print de statistiekentabel
    print_statistieken_tabel(lopers)

# Test de functionaliteit
test_lopers()
