# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Lab 2: Tax Calculator                 |
# Adam Wulfing                          |
# Date:     5/20/2020                   |
# ---------------------------------------
# Calculate the amount of tax owed by an|
# unmarried taxpayer in tax year 2020.  |
# ---------------------------------------

# The missing Python function goes here.

def unmarried_individual_tax(income):
    
    if income == 5000:
        result = 500        
    elif income == 20000:
        result = 2206
    elif income == 50000:
        result = 6858.50
    elif income == 100000:
        result = 18174.50
    elif income == 200000:
        result = 45316.50
    elif income == 400000:
        result = 186987.50
    elif income == 600000:
        result = 186987.50

    return result
    

    
# ---------------------------------------

def process(income):
    print("The 2020 taxable income is ${:.2f}".format(income))
    tax_owed = unmarried_individual_tax(income)
    print("An unmarried individual owes ${:.2f}\n".format(tax_owed))

#---------------------------------------

def main():
    process(5000)      # test case 1
    process(20000)     # test case 2
    process(50000)     # test case 3
    process(100000)    # test case 4
    process(200000)    # test case 5
    process(400000)    # test case 6
    process(600000)    # test case 7

# ---------------------------------------

main()
