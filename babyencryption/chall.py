import string
from secret import MSG


def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * ord(char) + 18) % 256) #number is first *multiplied* then *added* and a *modulo*
    print("Encrypted integer array: ")
    print(ct)
    return bytes(ct)

ct = encryption(MSG)
ct = ct.hex()
print("Encrypted Hex: " + ct)



def encryptSingleItem(item):
        return (123 * ord(item) + 18) % 256


allCharacters = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
decodedString = []

def bruteForce(intToCrack):
    for char in allCharacters:
        if (encryptSingleItem(char) == intToCrack): # we have the integer we want to crack therefore we must pass in
            decodedString.append(char)


def decodeHex(hex):
    decodedByteArray = bytearray.fromhex(hex)
    decodedCharArray = []
    intValues = [b for b in decodedByteArray] #this is correct
    print("Encrypted integer values (inside decode)")
    print(intValues)
    for intVal in intValues:
        bruteForce(intVal)

hex = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
decodeHex(hex)
print(''.join(decodedString))



