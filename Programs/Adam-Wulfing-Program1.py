# -----------------------------------------+
# Adam Wulfing                             |
# CSCI 127, Program 1                      |
# -----------------------------------------+
def grade2gpa(grade):
    
    if grade.lower() == "a":
        result = 4.0
    elif grade.lower() == "a-":
        result = 3.7
    elif grade.lower() == "b+":
        result = 3.3
    elif grade.lower() == "b":
        result = 3.0
    elif grade.lower() == "b-":
        result = 2.7
    elif grade.lower() == "c+":
        result = 2.3
    elif grade.lower() == "c":
        result = 2.0
    elif grade.lower() == "c-":
        result = 1.7
    elif grade.lower() == "d+":
        result = 1.3
    elif grade.lower() == "d":
        result = 1.0
    elif grade.lower() == "f":
        result = 0.0
    return result

def GPAcalc():
    num = int(input("How many classes are you taking? "))
    bound = 1
    currentCREDIT = 0
    currentGPA = 0
    while bound < num +1:
#        print(bound)

        grade = str(input("What is your GRADE for class # " + str(bound) + "? "))
        gp = grade2gpa(grade)
#        print(gp)

        credit = int(input("What is your CREDIT for class # " + str(bound) + "? "))
        currentCREDIT = currentCREDIT + credit
        
        gpa = gp * credit
#        print(gpa)

        currentGPA = currentGPA + gpa

        bound = bound + 1
        if bound >= num +1:
            finalGPA = currentGPA / currentCREDIT
            rounded = round(finalGPA, 2)
            print("Your final GPA is a " + str(rounded) + ". ")
    
# -----------------------------------------+

def main():
    GPAcalc()
    
# -----------------------------------------+

main()
