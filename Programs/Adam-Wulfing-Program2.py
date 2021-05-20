# -----------------------------------------+
# Adam Wulfing                             |
# CSCI 127, Program 2                      |
# Last Updated: 5/31, 2020                 |
# -----------------------------------------|
# A simplified Cribbage scoring system.    |
# -----------------------------------------+

def print_hand(h, n):

    c = evaluate_hand(h)
    flush_pts = flush(h)
    pair_pts = pairs(h)
    fifteens_pts = fifteens(c)
    total = fifteens_pts + flush_pts + pair_pts
    x = 0
    y = 0
    print("Hand " + str(n) + ": ", end =" ")
    for x in range(0,5):       
        for y in range(0,2):
            if x == 4 and y == 1: 
                print(h[x][y])
            else:
                print(h[x][y], end =", ")
    print("Points: " + str(total))
    print()
    

# -----------------------------------------
def evaluate_hand(h):
    c = []
    
    for x in range(0, 5):
        if str(h[x]).find("Two") != -1:
            c.append(2)
        elif str(h[x]).find("Three") != -1:
            c.append(3)
        elif str(h[x]).find("Four") != -1:
            c.append(4)
        elif str(h[x]).find("Five") != -1:
            c.append(5)
        elif str(h[x]).find("Six") != -1:
            c.append(6)
        elif str(h[x]).find("Seven") != -1:
            c.append(7)
        elif str(h[x]).find("Eight") != -1:
            c.append(8)
        elif str(h[x]).find("Nine") != -1:
            c.append(9)
        elif str(h[x]).find("Ten") != -1:
            c.append(10)
        elif str(h[x]).find("Ace") != -1:
            c.append(11)
        elif str(h[x]).find("Jack") != -1:
            c.append(10)
        elif str(h[x]).find("Queen") != -1:
            c.append(10)
        elif str(h[x]).find("King") != -1:
            c.append(10)
    return c

# -----------------------------------------
def flush(h):   
    spade = "Spades"
    heart = "Hearts"
    club = "Clubs"
    diamond = "Diamonds"

    if str(h[0]).find(club) != -1:
        for x in range(1, 5):
            if str(h[x]).find(club) != -1:
                result = 5
            else:
                result = 0
                return result
            
    elif str(h[0]).find(heart) != -1:
        for x in range(1, 5):
            if str(h[x]).find(heart) != -1:
                result = 5
            else:
                result = 0
                return result

    elif str(h[0]).find(spade) != -1:
        for x in range(1, 5):
            if str(h[x]).find(spade) != -1:
                result = 5
            else:
                result = 0
                return result

    elif str(h[0]).find(diamond) != -1:
        for x in range(1, 5):
            if str(h[x]).find(diamond) != -1:
                result = 5
            else:
                result = 0
                return result

    return result

# -----------------------------------------
def pairs(h):
    count = 0
    for x in range(0,5):       
        for y in range(x+1,5):
            if h[x][0] == h[y][0]:
                count = count + 2
    return count
# -----------------------------------------
def fifteens(c):
    count = 0
    for x in range(0,5):       
        for y in range(x+1,5):
            if c[x] + c[y] == 15:
                count = count + 2
    return count

# -----------------------------------------+
# Do not change anything below this line.  |
# -----------------------------------------+

def process_hands(cribbage_input, cards_in_hand):
    number = 1
    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0].capitalize(), hand[1].capitalize()])
            hand = hand[2:]
        print_hand(hand_as_list, number)
        evaluate_hand(hand_as_list)
        number += 1

# -----------------------------------------+

def main():
    cribbage_file = open("cribbage.txt", "r")
    process_hands(cribbage_file, 5)
    cribbage_file.close()

# -----------------------------------------+

main()
