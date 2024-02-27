# Q1: La fonction doit calculer la date de Pauqes d'une année donnée
# Q2: La fonction a pour paramètre 'year' un int
# Q3: La fonction retourne un string du format JJ-MM-AAAA
# Q4: Le nom de la fonction est 'find_date_of_easter'
# Q5: find_date_of_easter(2024) = '31-03-2024'

"""date_of_easter.py : Caclul les dates de Paques

Ce fichier permet de calculer la date du dimanche de Paques d'une année donnée en utilisant
l'algorithme défini par le concile de Nicée en 325 après J.-C. Pour plus d'information,
consultez 'https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques'.

@Date: 16 février 2024
@Author: Mathieu Ducharme
@Contact: mathieu.ducharme@umontreal.ca
@Matricule: 20297456
"""

def zfill(characters, total_length, leading_char=0):
    """Retourne un string d'un longueur 'total_length' avec le caractère
    'leading_char' qui remplit l'espace vide à gauche du string initial.
    """
    characters = str(characters)
    leading_char_length = total_length - len(characters) # Nombre de caractère à ajouter à gauche

    return str(leading_char) * leading_char_length + characters

    

def format_date(day, month, year):
    """Prend en paramètre 3 int - soit le jour, le mois et l'année
    puis retounre un string de la date sous la forme 'JJ-MM-AAAA'.
    """
    return zfill(day, 2) + '-' + zfill(month, 2) + '-' + str(year)

def find_date_of_easter(year):
    """Trouve la date de Paques qui correspond au dimanche qui suit la première pleine
    lune du printemps en utilisant l'algorithme définit par le Concule de Nicée en 325.

    Args:
        year (int): l'année dans l'intervalle [1583, 4999] que l'on souhaite connaitre la date de Paques
    Returns:
        ? (str): date de Paques sous la forme JJ-MM-YYYY ('%d-%m-%Y')
    """
    
    # Golden year
    golden_year = year % 19 

    # Siècle
    century = year // 100 

    # Différence entre le calendrier julien et le calendrier grégorien
    solar_equation = century - century // 4

    # Différence entre le calendrier julien et le cycle métonique
    lunar_equation = (8 * century + 13) // 25

    # Age de la lune au 22 mars
    epact = (solar_equation - lunar_equation + 19 * golden_year + 15) % 30

    lunar_date = epact // 28

    # Nombre de jour entre le 21 mars et la Lune écclésiastique
    paschal_moon_offset = epact - lunar_date * (1 - lunar_date * (29 // (epact + 1)) * ((21 - golden_year) // 11))

    # Jour de la semaine de la Lune écclésiastique (dimanche=0 ... samedi=6)
    paschal_moon_day = (year + year // 4 + paschal_moon_offset + 2 - solar_equation) % 7

    # Date de Paques au mois de mars (du 22 mars au 23 mai)
    date = 28 + paschal_moon_offset - paschal_moon_day
    
    if date <= 31:
        return format_date(date, 3, year)
    
    return format_date(date-31, 4, year)

def test_find_date_of_easter():
    assert find_date_of_easter(1583) == '10-04-1583'
    assert find_date_of_easter(1655) == '28-03-1655'
    assert find_date_of_easter(2000) == '23-04-2000'
    assert find_date_of_easter(2007) == '08-04-2007'
    assert find_date_of_easter(2024) == '31-03-2024'
    assert find_date_of_easter(2040) == '01-04-2040'
    assert find_date_of_easter(2100) == '28-03-2100'
    assert find_date_of_easter(3100) == '22-04-3100'
    assert find_date_of_easter(4999) == '07-04-4999'

if __name__ == '__main__':
    test_find_date_of_easter()