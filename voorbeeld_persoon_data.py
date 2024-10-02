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

# Print de lijst met behulp van tabulate voor een nette weergave
from tabulate import tabulate
print(tabulate(personen, headers=kolommen, tablefmt="grid"))
