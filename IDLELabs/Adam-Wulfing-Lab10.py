import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 10                                |
# June 19, 2020                                   |
# Adam Wulfing                                    |
# -------------------------------------------------

def read_file(file_name):
    file = open(file_name, "r")
    size = int(file.readline())
    college_names = np.zeros(size, dtype=object)
    college_enrollments = np.zeros(size, dtype=int)
    i = 0
    for row in file:
        data = row.split(",")
        college_names[i] = data[0]
        college_enrollments[i] = data[1]
        i = i + 1
    return college_names, college_enrollments
# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)
    #fig = plt.figure()
   # plt = fig.add_axes([0,0,1,1])
    bar = plt.bar(college_names,college_enrollments)
    bar[0].set_color('b')
    bar[1].set_color('y')
    bar[2].set_color('b')
    bar[3].set_color('y')
    bar[4].set_color('b')
    bar[5].set_color('y')
    bar[6].set_color('b')
    plt.title('MSU Spring 2020 Enrollments by COllege')
    plt.xlabel('College Name')
    plt.ylabel('College Enrollment')

    plt.show()
# -------------------------------------------------

main("spring-2020.csv")
