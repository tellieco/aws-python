def decryptMessageFull(message, shift):
    double_alphabet = getDoubleAlphabet(alphabeth)
    decryptedMessage = ""
    for letter in message:
        if letter == " ":
            print("space", letter)
            decryptedMessage += " "
        elif letter.isalpha() == False:
            print("special", letter)
            decryptedMessage += letter
        elif letter.isupper():
            print("upper", letter)
index = double_alphabet.find(letter.lower())
shifted_index = index - int(shift)
decryptedMessage += double_alphabet[shifted_index].upper()
else:
    print("letter", letter)
index = double_alphabet.find(letter)
shifted_index = index - int(shift)
decryptedMessage += double_alphabet[shifted_index]
return decryptedMessage