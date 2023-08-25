import os,random

def chooseLastName():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    text_file_path = os.path.join(script_dir, 'name.txt')

    with open(text_file_path, 'r') as file:
        names_list = file.read().splitlines()

    randomName = random.choice(names_list)

    return randomName

def chooseFirstName():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    text_file_path = os.path.join(script_dir, 'firstName.txt')

    with open(text_file_path, 'r') as file:
        names_list = file.read().splitlines()

    randomFirstName = random.choice(names_list)
    return randomFirstName

def getNewAlias():

    newName = chooseFirstName() + " " + chooseLastName()
    return newName

print(getNewAlias())