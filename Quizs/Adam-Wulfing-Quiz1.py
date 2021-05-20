# --------------------------------------
# CSCI 127, Quiz 1                     |
# Adam Wulfing                         |
# --------------------------------------
import random

def thething():
    rowsize = input("How many rows? ")
    columnsize = input("How many columns? ")
    y = 0
    x = 0
    for y in range(0,int(rowsize)):
        for x in range(0,int(columnsize)):
            line = []
            val = random.random()
            if val > .5:
                cur = "*"
            else:
                cur = "-"
            print(cur, end ="")
        print("")
    ans = input("would you like to go again?  ")
    if ans == "yes":
        thething()
    elif ans == "y":
        thething()
    elif ans == "no":
        print("Hey fuck you i worked hard on this")
    elif ans == "n":
        print("Okay... dick")
def main():
    thething()
    

main()
