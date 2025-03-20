#Programmer: Timothy Pickering
#Date Written: 3/19/2025
#Title: Reverse camelCase

def word_separator(sentence):
    new_sentence = sentence[0]  #Start with the first character

    #Iterate over the rest of the characters
    for char in sentence[1:]:
        if char.isupper():
            new_sentence += " " + char.lower()  #Add space before uppercase and convert to lowercase
        else:
            new_sentence += char  #Add the character as is

    return new_sentence.strip()

#Get user input
sentence = input("Enter a camelCase sentence: ")

#Process and display the result
print(word_separator(sentence))
