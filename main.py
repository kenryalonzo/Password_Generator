import random as rd

def get_infos(message:str):
    
    result_num = 0
    
    print()
    result = input(message)
    
    try:
        result_num = int(result)
        return result_num
    except: 
        print("Attention valeur incorrecte")
        print()
        
        return get_infos(message)
    

def get_alphabet(type:int):
    miniscule = "abcdefghijklmnopqrstuvwxyz"
    majuscule = miniscule.upper()
    chiffre = "0123456789"
    symbole = "!@#$%^&*|`~/\\?"
    
    if type == 1:
        return miniscule
    elif type == 2:
        return miniscule+majuscule
    elif type == 3:
        return miniscule+majuscule+chiffre
    elif type == 4:
        return miniscule+majuscule+chiffre+symbole
    else:
        print("Erreur: valeur non pris en charge")


def get_password(type:int, lenght:int):
    alphabet = get_alphabet(type)
    password = "".join(rd.choices(population=alphabet, k=lenght))
    
    return password
     

def main():
    password_type = get_infos("Quel seras le type de mot de passe ?\n1- Minisule\n2- Miniscule + Majuscule\n3- Miniscule + Majuscule + Chiffre\n4- Miniscule + Majuscule + Chiffre + Symbole\n")
    password_lenght = get_infos("Quel est la longueur du mot de passe ")
    
    nbre = 5
    
    for i in range(nbre):
        password = get_password(password_type,password_lenght)
        print(f'Proposition {i+1} : {password}')


main()