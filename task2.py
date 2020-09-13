# Viktoria Cseke R00180598
# System scripting Assignment 2: Python scripting
# task2
# ----------------------------------------------------
# Algorithm:
# a function that accepts two parameters
# first param: list of items >> create a copy of list to print later as tuple
# second: int value of num of indexes
# loop around:
# random generator to generate indexes between 2 to 5 and * by second param (need to import random)
# remove generated index from list
#
# return list as tuple
#
# ask user for at least 12 items for list
# ------added a function to ensure at least 12 items, loops around until its met
# ensure 2nd param is between 2 and 6
# ------added a function to ensure num is between 2 to 6, loops around until its met
# print tuple
# print original list

import random

def delete_at_index(userList,num):
    new_list=userList.copy()

    print("┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")
    for x in range(num):
        value=random.randint(2, 5)
        print("deleted at index", value,"the element:",new_list[value])
        del new_list[value]

    return tuple(new_list)

def check_length(userList):
    while True:
        if(len(userList)<12):
            print("Please add more values, the length is only ",len(userList))
            input_string = input("Enter value(s):")
            addList = input_string.split(',')

            for i in range(len(addList)):
                userList.append(addList[i])
        else:
            return userList

def check_num(num):
    while True:
        if(num>=6):
            num = int(input("um, wrong value... try again, only up to 6:"))
        elif(num<=2):
            num = int(input("um, wrong value... try again, only between 2 to 6:"))
        else:
            return num


def main():
    print("Welcome!")
    input_string = input("Enter at least 12 items separated by ',' a comma:")
    userList = input_string.split(',')

    userList=check_length(userList)

    num = int(input("Enter number between 2-6, for amount to be deleted:"))
    num=check_num(num)

    new_list=delete_at_index(userList,num)

    print("┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")
    print("Result tupple:",new_list)
    print("Original list:",userList)

main()