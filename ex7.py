def string_reverse(string):
    reverse = ""
    length = len(string)
    length -= 1

    for letter in range(length, -1, -1):
        reverse += string[letter]

    print reverse
string_reverse("This is a sentence")        
