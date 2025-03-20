#Programmer: Timothy Pickering
#Date Written: 3/19/2025
#Title: Name Initials Generator

def initials_generator(personsName):
    personsInitials = ""

    #Split the input into a list of names
    nameParts = personsName.split()

    #Extract the first letter of each name and format with a period
    for name in nameParts:
        personsInitials += name[0].upper() + ". "

    return personsInitials.strip()  #Remove trailing space

#Get user input
personsName = input("Enter the user's first, middle, and last name: ")

#Generate and print initials
initials = initials_generator(personsName)
print(initials)
