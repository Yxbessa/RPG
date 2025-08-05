from classes import Character
def get_character_input():
    name = input("Escolha seu nome:")
    print("Escolha sua classe entre:")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Arqueiro")
    character_class = input()
    return Character(name, character_class)
character = get_character_input()