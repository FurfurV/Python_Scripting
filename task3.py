# Viktoria Cseke R00180598
# System scripting Assignment 2: Python scripting
# task3
# ----------------------------------------------------
# Algorithm:
# create a function called reducer()
# accepts an integer called number
# if number is even %2 == 0 then reducer divides it by 2, made sure it returns int and not float
# else if odd, then return (number *3)+1
#
# user enters the int number
# call reducer until number = 1
# print numbers returned from reducer
#the question does not mention negative numbers, it does not work on them... it loops forever(needs different forumla)
#just added for them a checker, question didnt ask tho...
#I added the checking for 0 too just in case, i hope i wont lose marks for that...

def reducer(number):
    if (number % 2 == 0):
        return int(number / 2)
    else:
        return (number * 3) + 1


def menu():
    print("Welcome!")
    while True:
        try:
            number = int(input("Enter number:"))
            break

        except ValueError:
            print("hmmm,... please whole numbers only")

    if number>0:
        while number != 1:
            number = reducer(number)
            print(number)
    elif number<0:
        print("It only works with positive numbers.")
    else:
        print("Your number is 0")

menu()
