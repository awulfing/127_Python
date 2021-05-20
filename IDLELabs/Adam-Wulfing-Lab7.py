# -----------------------------------------------------
# CSCI 127, Lab 7
# June 10, 2020
# Adam Wulfing
# -----------------------------------------------------

class Contact:
    def __init__(self, firstName, lastName, num):
        self.x = firstName
        self.y = lastName
        self.z = num
        self.ihatepython = " "

    def get_cell_number(self):
        return self.z
        
    def get_area_code(self):
        return self.z[:3]
        
    def set_first_name(self,name):
        self.x = name
        
    def set_title(self,title):
        self.ihatepython = title

    def print_entry(self):
        if self.ihatepython == " ":
            print("{:<15}{:>22}".format(self.x + " " + self.y, self.z))
        else:
            print("{:<24}{:>13}".format(self.ihatepython + " " + self.x + " " + self.y, self.z))
        
# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
