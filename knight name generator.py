# Knight Name Generator - www.101computing.net/name-knight-generator
import random


def knightNameGenerator():
    # Initialise list of possible first names and nicknames
    firstnames = ["Lancelot", "Charles", "Henry", "William", "James", "Richard", "Edward"]
    nicknames = ["Brave", "Horrific", "Courageous", "Terrific", "Fair", "Conqueror", "Victorious", "Glorious",
                 "Invicible"]

    # Randomely pick one first name and one nickname
    firstname = random.choice(firstnames)
    nickname = random.choice(nicknames)

    # Use String concatenation to generate and return the full name
    return firstname + " The " + nickname


def generateCoatOfArms():
    colours = ["Red", "Golden", "Blue", "Purple", "White", "Silver"]
    animals = ["Lion", "Dragon", "Unicorn", "Horse", "Tiger"]

    colour = random.choice(colours)
    colour1 = random.choice(colours)
    animal = random.choice(animals)

    if colour == colour1:
        return f"Your coat of arms is a {colour} {animal}"
    else:
        return f"Your coat of arms is a {colour} and {colour1} {animal}"

def favorite_weapon():
    weapons = ["Iron mace", "Golden flail", "Silver axe", "Silver sword","Wooden Shield"]
    weapon = random.choice(weapons)
    return f"Your favorite weapon is {weapon}."

def top_qulities():
    qulaities = ['brave','inteligent','best fighter','tezan']
    quality = random.choice(qulaities)
    return f"You ar {quality}."

def they_live():
    areas = ['haunted castle','hidden mansion', 'fortified tower']
    area = random.choice(areas)
    return f"You live in {area}."


# Main code to test our function
player1 = knightNameGenerator()
print(f"Player 1: Your name is:{player1} \n{generateCoatOfArms()}"
      f"\n{favorite_weapon()}\n{top_qulities()}\n{they_live()} ")


player2 = knightNameGenerator()
print(f"\nPlayer 2: Your name is:{player2} \n{generateCoatOfArms()}"
      f"\n{favorite_weapon()}\n{top_qulities()}\n{they_live()} ")
