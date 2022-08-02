import socket

#ip and port
host = "127.0.0.1"
port = 1337

#socket setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

# variables
leakedCipher = None

#client server communication
askForUsername = s.recv(4096).decode().strip()
print(askForUsername)

username = "cdmin"
s.send(username.encode())

askForPassword = s.recv(4096).decode().strip()
print(askForPassword)

password = "g0ld3n_b0y"
s.send(password.encode())

receiveWelcomeMessage = s.recv(4096).decode().strip()
print(receiveWelcomeMessage)

receiveNextMessage = s.recv(4096).decode().strip()
print(receiveNextMessage)

if (receiveNextMessage.startswith("Leaked")):
    leakedCipher = receiveNextMessage.split(' ')[2]

askForEnterCipherText = s.recv(4096).decode().strip()
print(askForEnterCipherText)

# first need to convert to bytes
leakedCipherBytes = bytes.fromhex(leakedCipher)

print("Leaked Cipher Bytes: " + str(leakedCipherBytes))

# then convert to byte array
leakedCipherBytes = bytearray(leakedCipherBytes)

# xor the cipher byte you want to change with the ord of the actual character and the ord of the character you want to replace
flippedCipherChar = chr(leakedCipherBytes[0] ^ ord("c") ^ ord("a"))

# remove the first byte
del(leakedCipherBytes[0])

print("After del: " + str(leakedCipherBytes))

# turn the flipped char into a byte
flippedCipherByte = flippedCipherChar.encode()

print("Encoded flipped cipher byte: " + str(flippedCipherByte))

# turn the flipped cipher byte into a byte array to easily manipulate it
flippedCipherByte = bytearray(flippedCipherByte)

# add to the flipped cipher byte array to have the whole ciphertext in the byte array
flippedCipherByte.extend(leakedCipherBytes)

# convert back to bytes
finalCipherBytes = bytes(flippedCipherByte)

print("Final cipher bytes: " + str(finalCipherBytes))

# turn it back into hex
flippedCipherHex = flippedCipherByte.hex()

print("Final hex: " + str(flippedCipherHex))

# send it off
s.send(flippedCipherHex.encode())
result = s.recv(4096).decode().strip()

# woohoo flag is gotten
print(result)





