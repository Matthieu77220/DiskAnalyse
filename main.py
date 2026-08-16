from Finder.find_path import get_input, clear_input, is_valid_input

def main():
    value = get_input()
    clear_value = clear_input(value)
    is_valid = is_valid_input(clear_value)
    
    if is_valid:
        print("Chemin valide")
    else:
        print("Chemin invalide")

main()