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
    result = ''

    for i in range(leading_char_length):
        result += str(leading_char)

    return result + characters
    

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
    g = year % 19 

    # Siècle
    c = year // 100 

    # Calculs intermédiaires (évite les répétitions)
    d = c - c // 4
    e = (8 * c + 13) // 25
    h = (d - e + 19 * g + 15) % 30
    k = h // 28
    p = 29 // (h + 1)
    q = (21 - g) // 11

    # Nombre de jour entre le 21 mars et la Lune écclésiastique
    i = h - k * (1 - k * p * q)

    # Jour de la semaine de la Lune écclésiastique (dimanche=0 ... samedi=6)
    j = (year + year // 4 + i + 2 - d) % 7

    # Date de Paques au mois de mars (du 22 mars au 23 mai)
    r = 28 + i - j
    
    if r <= 31:
        return format_date(r, 3, year)
    
    return format_date(r-31, 4, year)

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