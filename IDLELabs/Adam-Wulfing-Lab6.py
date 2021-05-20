#they are treated differntly because all of them are comma seperated as well as spaced to be programmed
# --------------------------------------
# CSCI 127, Lab 7                      |
# February 28, 2019                    |
# Adam Wulfing                         |
# --------------------------------------

def create_dictionary(file_name):
    char2ascii = {}
    file = open(file_name,"r")
    for line in file:
        temp = line.replace("\n", "")
        (data, key) = temp.split(",")
        char2ascii[key] = data

    return char2ascii

def translate(sentence, dictionary, file_name):
    file = open(file_name,"w")
    for char in sentence:
        if char in dictionary:
            file.write(char + " " + str(dictionary[char]) + "\n")
        elif char == " ":
            file.write("  " + str(dictionary["space"]) + "\n")
        elif char == ",":
            file.write(", " + str(dictionary["comma"]) + "\n")
        else:
            file.write(char + " " + "UNKNOWN" + "\n")
# --------------------------------------

def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Bozeman, MT  59717"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "The value is ~$25.00"
    translate(sentence, dictionary, "output-3.txt")
    
# --------------------------------------

main()
