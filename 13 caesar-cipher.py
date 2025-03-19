def getDoubleAlphabet(x):
    doubleAlphabet = x + x
    return doubleAlphabet

print(getDoubleAlphabet("ABCDEF"))
print(getDoubleAlphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

x= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(getDoubleAlphabet(x))

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

print(getMessage())

#def getCipherKey():
 #   shiftAmount = input( "Please enter a key (whole number from 1-25): ")
  #  return shiftAmount

def getCipherKey():

    while True:
        try:
            shiftAmount = int(input("Please enter a key (whole number from 1-25): "))
            if 1 <= shiftAmount <= 25:
                return shiftAmount

            else:
                print("Error: Key must be a whole number between 1 and 25.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")
            
print(getCipherKey())

def encryptMessage(getMessage, getCipherKey, alphabet):
    encryptedMessage = ""
    #uppercaseMessage = ""
    uppercaseMessage = getMessage.upper()
    for x in uppercaseMessage:
        position = alphabet.find(x) #find index of current character in alphabet
        newPosition = position + int(getCipherKey) #new index = old index + key
        if x in alphabet:
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + x
    return encryptedMessage

print(encryptMessage("Hello+", 1, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
#print(encryptMessage(getMessage, getCipherKey, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))