# Asking the user which message is needed to be decrypted
print('Type a message to descrypt')

# Ask the user to type the message
message = input()

# Follows the first message example
# Pbatenghyngvbaf, lbh unir fhpprrqrq va qrpelcgvat gur fgevat.

# Transform the message in a list
message_list = list(message)

# Import the package string, which contains ascii lists     
import string

# Defining a string containing all the lowercase and uppercase letters
alphabet = string.ascii_letters

# Creating a list of char starting from the string alphabet, therefore containing
# all the letters, both lowercase and uppercase ones
list_alphabet = list(alphabet)

# Creating a list of the values to associate to the letters in the alphabet list
list_values = list(range(len(list_alphabet)))

# Creating a dictionary in which the keys are the letter (list_alphabet), and the
# values are number from 0 to 51 (the length is 52)
dict_alphabet = dict(zip(list_alphabet,list_values))

# The variable that will contain the decrypted message
decrypted_message = [0]*len(message_list)
# [] means that it is a void element


# (string, s)
# string: the message to be decrypted
# s: the shift needed for the decryption   
def f_decryption(m, s):    
    i = 0
    for char in m:
        if(char.islower()):
            # Saving the position of char in the dictionary
            position = dict_alphabet[char]
            if((position-s)<0):
                decrypted_message[i]=list_alphabet[26+(position-s)]
                i = i+1
            elif((position-s)>-1):
                decrypted_message[i]=list_alphabet[position-s]
                i = i+1
        elif(char.isupper()):
            # Saving the position of char in the dictionary
            position = dict_alphabet[char]
            if((position-s)<26):
                decrypted_message[i]=list_alphabet[52-(position-26-1)]
                i = i+1
            elif((position-s)>25):
                decrypted_message[i]=list_alphabet[position-s]
                i = i+1
        else:
            # In case of punctuaction and spaces, save them in decrypted_message
            decrypted_message[i]=char
            i = i+1
    print(''.join(decrypted_message))
    return

for shift in range(0,25):
    decrypted_message = [0]*len(message_list)
    decrypted_message = f_decryption(message, shift)
