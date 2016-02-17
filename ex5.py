print "Type a word or sentence."

word = raw_input("--> ")

# word = "Cunningham"
robbers_word = ""

for element in word:

    if element == "a" or element == "e" or element == "i" or element == "o" or element == "u":
        robbers_word += element
    elif element == " ":
        robbers_word += element
    else:
        robbers_word += element + "o" + element

print "Here's your input in rovarspraket:", robbers_word        

