# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Weather CSV Library           |
# Adam Wulfing                             |
# Last Modified: ??, 2019                  |
# -----------------------------------------+
# Provide a brief overview of the program. |
# -----------------------------------------+

def coldest_temperature(input_file):
    file = open(input_file,"r")
    file.readline()
    small = 1000.0
    for line in file:
        data = line.split(",")
        if float(data[7]) < float(small):
            small = data[7]
            location = data[1] 
            date = data[4]

    file.close()
    statement = "Coldest: " + str(small) + "\nLocation: " + location + "\nDate: " + date
    return print(statement)

#-------------------------------------------
def average_temperature(input_file, location):
    file = open(input_file,"r")
    file.readline()
    i = 0
    t = 0
    for line in file:
        data = line.split(",")
        loc = data[1]+","+data[6]
        loc = loc.replace('"', "")
#        print(loc)
 #       print(location)
        if loc == location:
            t = int(data[0]) + t
            i = i + 1
    if i == 0:
        statement = "Not Applicable"
    else:
        ave = t/i
        output = round(ave, 2)
        statement = "Number of readings " + str(i) + "\nAverage temp: " + str(output) + "*F"
    file.close()
    return print(statement)


#-------------------------------------------
def all_stations_by_state(input_file, state):
    file = open(input_file,"r")
    file.readline()
    i = 1
    city = []
    for line in file:
        data = line.split(",")
        if data[12] == state:
            if data[1] not in city:
                city.append(data[1])
                print(str(i) + ". " + city[i-1])
                i = i + 1
    file.close()

#-------------------------------------------
def timemachine(input_file, date, loc):
    file = open(input_file,"r")
    file.readline()
    i = 0
    for line in file:
        data = line.split(",")
        if data[1] == loc:
            if (data[4].find(date +'/') != -1):
                print() 
                print("The average temperature in " + loc + " on " + data[4] +" was " + data[0])
                i = i + 1
    if (i == 0):
        print("No samples taken that day")
        
            
    
# -----------------------------------------+
# Do not change anything below this line   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+

def menu():
    print()
    print("1. Identify coldest temperature.")
    print("2. Identify average temperature for a given location.")
    print("3. Identify all recording station locations by state.")
    print("4. Something interesting, non-trivial and not a variation of the above options.")
    print("5. Quit.")
    print()

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+

def main():
    input_file = "weather.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            coldest_temperature(input_file)
        elif (choice == 2):
            location = input("Enter desired location (e.g. Miles City, MT): ")
            average_temperature(input_file, location)
        elif (choice == 3):
            state = input("Enter name of state (e.g. Montana): ")
            all_stations_by_state(input_file, state)
        elif (choice == 4):
            date = str(input("Enter a sunday in 2016 (e.g 1/3): "))
            loc = input("Enter name of a city(e.g. San Diego): ")
            timemachine(input_file, date, loc)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()
