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

def find_date_of_easter(year):
    """Trouve la date de Paques qui correspond au dimanche qui suit la première pleine
    lune du printemps en utilisant l'algorithme définit par le Concule de Nicée en 325.

    Args:
        year (int): l'année dans l'intervalle [1583, 4999] que l'on souhaite connaitre la date de Paques
    Returns:
        ? (str): date de Paques sous la forme JJ-MM-YYYY ('%d-%m-%Y')
    """
    
    pass

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