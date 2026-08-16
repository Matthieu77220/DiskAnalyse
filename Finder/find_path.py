import os

def get_input() :
    
    value = None   
    
    print("Entrer le chemin du dossier à analyser : \n")
    value = input()
    return value

def clear_input(value):
    
    clearValue = None
    
    clearValue = value.strip(' \'\"')
    return clearValue

def is_valid_input(clearValue):
    
    if clearValue is None :
        print("Valeur nulle.")
        return False
    
    if os.path.exists(clearValue) == False :
        print("Chemin innexistant.")
        return False
    
    if os.path.isdir(clearValue) == False :
        print("le chemin ne correspond pas à un dossier.")
        return False
    
    return True