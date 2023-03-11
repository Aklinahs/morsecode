# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
                    'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
                    'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
                    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}


# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message.lstrip():
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += ' '

    return cipher


# Function to decrypt the string from morse to english
def decrypt(message):

    message += ' '
    decipher = ''
    citext = ''
    i = 0
    for letter in message.lstrip():
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

type = input("Enter 'D' for decrypt or 'E' for encrypt :")
if type.upper() == "E":
    message = input("Enter message to encrypt : ")
    print(encrypt(message))

elif type.upper() == "D":
    message = input("Enter message to decrypt : ")
    print(decrypt(message))

else:
    print("Invalid input, please try again")
