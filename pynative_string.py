# check if n is less than the length of the string
# remove the first n characters from the string



def remove_chars(word, n, from_end=False):
    print('Original string:', word)


    if from_end:
        x = word[:-n]
    else:
        x = word[n:]
    return x

print("Removing characters from a string")


user_input = input("Enter a string: ")
n = int(input("Enter the number of characters to remove: "))
from_end_input = input("Remove from the end? (y/n): ").lower()
from_end = from_end_input == 'y'
result = remove_chars(user_input, n, from_end)

print("Result after removing characters:", result)
