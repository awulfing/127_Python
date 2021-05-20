import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Adam Wulfing                          |
# Last Modified: ??, 2019               |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

class Pokemon:
    def __init__(self, name, number, combatPoints, types):
        self.name = name
        self.num = number
        self.cP= combatPoints
        self.type = types
        
    def __str__(self):
        return "Number: " + str(self.num) + ", Name: " + str(self.name) + \
               ", CP: " + str(self.cP) + ": Type: " + " and ".join(self.type)
    def getName(self):
        return self.name
    def getNumber(self):
        return self.num
    def getCombatPoints(self):
        return self.cP
    def getTypes(self):
        return self.type

#-----------------------------------------
def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit")

# 1
def print_pokedex(pokedex):
    print()
    print("                      The Pokedex")
    print("----------------------------------------------------------")
    for line in pokedex:
        print(line)
# 2

def lookup_by_name(pokedex, name):
    count = 0
    for x in range(len(pokedex)):
        if name.lower() == pokedex[x].getName():
            print(pokedex[x])
            count = count + 1
    if count == 0:
        print("There is no Pokemon named " + name)

# 3
def lookup_by_number(pokedex, number):
    count = 0
    for x in range(len(pokedex)):
        if number == pokedex[x].getNumber():
            print(pokedex[x])
            count += 1
    if count == 0:
        print("There is no Pokemon " + str(number))

# 4
def total_by_type(pokedex, pokemonType):
    count = 0
    for x in range(len(pokedex)):
        types = pokedex[x].getTypes()
        for y in range(len(types)):
            if pokemonType.lower() == types[y]:
                count += 1
    print("Number of Pokemon that contain type " + pokemonType.lower() + " = " + str(count))

# 5
def average_hit_points(pokedex):
    power = 0
    count = 0
    for x in range(len(pokedex)):
        power += pokedex[x].getCombatPoints()
        count += 1
    print("Average Pokemon combat points = " + str((power / count).__round__(2)))






# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()
