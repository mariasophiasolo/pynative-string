# remove the first n characters from the string

def remove_chars (name, n, from_end=False):
    print ("First name:", name)

# remove the characters from the end or beginning of string
    if from_end:
        x = name[:-n]
    else:
        x = name[n:]
# return
        return

# ask user to input string and the number of characters to remove
user_input = input("Enter your name: ")
n = int(input("Enter how many letters you want to remove from your name: "))

# ask user whether to remove charcaters from the end or beginning
from_end_input = input("Do you want it to remove from end or beginning? (y/n:) ").lower()
from_end = from_end_input == 'y'

# call the function with the user input
result = remove_chars (user_input, n, from_end)

# display the result
print ("This will be your nickname: ", result)

