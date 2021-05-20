# --------------------------------------
# CSCI 127, Lab 3                      |
# May 28, 2020                         |
# --------------------------------------
# Calculate the length of a string     |
# using three techniques.              |
# --------------------------------------
def length_built_in(sentence):
    built_in = len(sentence)
    return built_in

# --------------------------------------
def length_iterative(sentence):
    count = 0
    for letter in sentence:
        count = count + 1
    return count

# --------------------------------------      
def length_recursive(sentence):
    if sentence == '':
        return 0
    
    return 1 + length_recursive(sentence[1:])
# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating length of the sentence using ...")
        print("---------------------------------------")
        print("Built-in function =", length_built_in(sentence))
        print("Iteration =", length_iterative(sentence))
        print("Recursion =", length_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
