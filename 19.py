# 19. Prefix "Is" String Modifier

# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
while True:
    def prefix(text):
        if len(text) >= 2 and text[:2] == "Is" and "is":
            return text
        else:
            return "Is" + text
        

    text = input("Enter something : ")
    print(prefix(text))