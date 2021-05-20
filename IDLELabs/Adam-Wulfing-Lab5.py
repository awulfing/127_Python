# --------------------------------------
# CSCI 127, Lab 6                      |
# June 16, 2019                        |
# Adam Wulfing                         |
# --------------------------------------
def average_magnitude(file_name):
    file = open(file_name,"r")
    file.readline()
    added = 0.0
    count = 0
    for line in file:
        data = line.split(",")
        added = added + float(data[8])
        count = count + 1
    file.close()
    return added/count

def earthquake_locations(file_name):
    file = open(file_name,"r")
    file.readline()
    count = 0
    locations = []
    for line in file:
        data = line.split(",")
        if data[11] not in locations:
            locations.append(data[11])
        locations.sort()
    e = 0
    for x in locations:
        print(locations[e])                
        e = e + 1
    print("")
    file.close()
    
def count_earthquakes(file_name, lower_bound, upper_bound):
    file = open(file_name,"r")
    file.readline()
    count = 0
    for line in file:
        data = line.split(",")
        if float(data[8]) >= lower_bound and float(data[8]) <= upper_bound:
            count = count + 1
    file.close()
    return count
# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    earthquake_locations(file_name)

    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
