import random


def generare_ticket()->str:
    """Generare serie ticket"""
    LETTERS:str = "qwertyuiopasdfghjklzxcvbnm"
    begin:int = random.randint(1, 2)
    serie_ticket:str = ''
    if begin == 1:
        while len(serie_ticket) < 10:
            serie_ticket += random.choice(LETTERS.upper())
            if len(serie_ticket) == 3 or len(serie_ticket) == 7:
                serie_ticket += '-'
            else: serie_ticket += str(random.randint(1, 9))
        serie_ticket += random.choice(LETTERS.upper())
    else:
        while len(serie_ticket) < 10:
            serie_ticket += str(random.randint(1, 9))
            if len(serie_ticket) == 3 or len(serie_ticket) == 7:
                serie_ticket += '-'
            else: serie_ticket += random.choice(LETTERS.upper())
        serie_ticket += str(random.randint(1, 9))
    return serie_ticket

def extragere_numar()->int:
    return random.randint(1, 10)
