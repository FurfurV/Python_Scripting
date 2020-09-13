# Viktoria Cseke R00180598
# System scripting Assignment 2: Python scripting
# task1
# ----------------------------------------------------
# algorithm:
#  created 3 functions that accept list of string items.
# user enters words one by one until the list length is 5
#  1st function returns first item whose length is divisible by 3, check if modulo returns 0
#  2nd function returns last item with more than 4 characters, reverse list then check len()>4
#  3rd function replicates line by 3. then print one entry per line that has an odd length, check length %2 thats not 0
# added lines to functions just in case it cant find any met requirements
#
#  create the menu print function
# use of while loop
# if user enters 'f' or 'F', run 1st function
# if user enters 'l' or 'L' run 2nd function
# if user enters 'e' or 'E' then exit and print message
# if user enters a number run 3rd function, change input to int
# put userinput in try except to only allow the above options

def length_divisible(userList):
    for u in userList:
        if len(u)%3==0:
            print(u,"has a length that is divisible by 3.")
            break
    else:
        print("hmm, could not find any 😕")

def return_last(userList):
    for u in reversed(userList):
        if len(u)>4:
            print(u,"has a length that is longer than 4.")
            break
    else:
        print("hmm, could not find any 😕")

def replicate(userList):
    output=userList*3
    for o in output:
        if len(o) % 2 !=0:
            print(o)


def print_options():
        print("="*70)
        print("\tEnter f or F to find first item, whose is length divisible by 3")
        print("\tEnter l or L to find last item, whose length is more than 4")
        print("\tEnter any number to replicate list by 3")
        print("\tEnter e or E to exit")
        print("="*70)

def main():
    print("Welcome !")
    #input_string = input("Enter 5 string items separated by ',' a comma:")
    #userList= input_string.split(',')
    userList=[]
    while len(userList)<5:
        print("add values>>>")
        new=input()
        userList.append(new)
    print("user list is ", userList)

    while True:
        print_options()

        select = input(">>: ")
        try:
            if select == 'f' or select == 'F':
                length_divisible(userList)

            elif select == 'l' or select == 'L':
                return_last(userList)

            elif select == 'e' or select == 'E':
                print("Thank you, bye!")
                return False

            else:
                int(select)
                replicate(userList)
        except:
            print("wrong choice")

main()