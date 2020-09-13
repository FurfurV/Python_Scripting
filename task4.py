# Viktoria Cseke R00180598
# System scripting Assignment 2: Python scripting
# task4
# ----------------------------------------------------
# i have made a diagram of the folder layout.
# wrote function to create a folder, it needs two inputs, directory path and directory name.
# wrote the next function that checks if task4 directory exists or not, if yes delete it.
#
# imported shutil because os.rmdir only removes an empty directory, and shutil removes the whole tree
# using os library as it has functions that i need, such as checking existing directory in path, get current dir,
# and join path name
#
# then run phase_one(), it recreates task4 folder and the subfolders in it.
# changes path to working path, then create folders again (pics, docs, movie)
#inside that create two sub folders (school, party) and 5 txt files
# i wrote a function that reads in a list and creates the text files with the names from the list
#
# move on to phase_two()
# pass path of docs to phase_two(), inside that walk through the directories and files,
# a for loop to alter the names of the files
# the first variable makes the name lowercase until the .txt
# the 2nd variable makes the last 3 chars uppercase
# then create a single string out of it and rename the files in the given path
# the folders stay the same name
#
# in zipfiles function i defined the path to backup
# then changed to directory backup before zipping the docs folder
# print contents changes directory to task for to print backup files
# then used a function from zipfile library to print contents from docs3.zip
# i added the prints just for verification purposes


import os
import shutil
import zipfile

def create_dir(current_dir,name):
    dir = os.path.join(current_dir, name)
    if not os.path.exists(dir):
        os.mkdir(dir)

def phase_one():
    print("----------------------phase one----------------------")

    current_dir = os.getcwd() #get current dir
    create_dir(current_dir,"task4")
    print("folder task4 created in: ",current_dir)

    task4_dir= os.path.join(current_dir, "task4") #extend the dir path to task4
    create_dir(task4_dir, "backup")
    create_dir(task4_dir, "working")

    print("folder backup and working created in: ", task4_dir)

    working_dir= os.path.join(task4_dir, "working")  #extend path to working
    create_dir(working_dir, "pics")
    create_dir(working_dir, "docs")
    create_dir(working_dir, "movie")

    print("folder pics and docs and movie created in: ", working_dir)

    docs_dir=os.path.join(working_dir, "docs")  #extend path to docs

    names=["CORONAVIRUS.txt","DANGEROUS.txt","KEEPSAFE.txt","STAYHOME.txt","HYGIENE.txt"]

    print("")
    for n in names:
        name = os.path.join(docs_dir,n)
        file=open(name, "w")
        print("\ttext file",n,"created in: ", docs_dir)
        file.close()

    create_dir(docs_dir, "school")
    create_dir(docs_dir, "party")

    print("\nfolder school and party created in: ", docs_dir, "\n")

    return docs_dir,task4_dir

def phase_two(docs_dir,task4_dir):
    # print("Current directory:\n",docs_dir)
    # docs_dir = os.path.join(docs_dir, "docs")  # extend path to docs
    print("----------------------phase two----------------------")

    for root, dirs, files in os.walk(docs_dir):
        for f in files:
            front=f[0:-3:1].lower()
            txt=f[-3:].upper()
            name=front+txt

            old=os.path.join(docs_dir,f)
            new=os.path.join(docs_dir,name)
            os.rename(old, new)
            print("file name changed from:",f,"to:",name)

    zip_files(docs_dir,task4_dir)
    print_contents(task4_dir)


def zip_files(from_path,task4_dir):
    to_path=os.path.join(task4_dir, "backup")
    os.chdir(to_path) #change to this directory

    for i in range(5):
        name="docs"+str(i+1)
        shutil.make_archive(name, 'zip',from_path)


def print_contents(task4_dir):
    os.chdir(task4_dir)
    # current_dir = os.getcwd()
    # task4_dir = os.path.join(current_dir, "task4")
    backup_dir = os.path.join(task4_dir, "backup")
    print("-----------------------------------------------------")
    print("contents of backup folder:")
    for root, dirs, files in os.walk(backup_dir):
        for f in files:
            print(f)

    os.chdir(backup_dir)
    print("\nContents of the zip file docs3: ")
    zip = zipfile.ZipFile('docs3.zip')
    print(str(zip.namelist()))
    zip.close()

def remove_dirs():
    current_dir = os.getcwd()
    dir = os.path.join(current_dir, "task4")
    if os.path.exists(dir):
        try:
            shutil.rmtree(dir)
        except:
            print('Error while deleting directory')

        print(dir + ' already existed, removed.\n')

def main():
    print("Welcome!")
    remove_dirs()

    docs_dir,task4_dir=phase_one()

    phase_two(docs_dir,task4_dir)

main()