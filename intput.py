# ==========================================
# Voorbeeld Opdracht
# Voer je naam in met de input() methode en print daarna je naam in de console.
# ==========================================

naam = input('Voer je naam in: ')  # voorbeeld invoer: Bart
print('Je naam is: ', naam)  # Het resultaat is: Je naam is: Bart


# ==========================================
# Opgave 1:
# Gegeven is het woord 'Python'. Schrijf een programma dat de gebruiker vraagt om input. Als de gebruiker het woord 'Python' invoert, print dan de boolean True, anders print False.
# ==========================================

programma_naam = input('Wat is de beste programmeer taal? ')
if programma_naam == 'Python' or programma_naam == 'python':
    print('True')
else:
    print ('False')


# ==========================================
# Opgave 2:
# Schrijf een programma dat de gebruiker vraagt om een getal. Voer daarna nog een getal in en print de som van de twee getallen.
getal_1 = int(input('Voer een getal in: '))
getal_2 = int(input('Welk getal wil je toevoegen aan het vorige getal? '))
print('De som van', getal_1, 'en', getal_2, 'is: ', getal_1 + getal_2)
# Verwachte uitkomst bij invoer van getallen 2 en 3:  De som van 2 en 3 is : 5
# ==========================================

