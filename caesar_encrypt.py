# This script is to encrypt message using caesar cipher

print('Caesar Cipher Encryptor')
print('='*25, '\n')
plain_text = input("Message to encrypt: ").upper()
while True:
    cipher = input("Number of shifted characters: ")
    try:
        cipher = int(cipher)
        if cipher in range(1, 26):
            break
        else:
            print("Please enter a digit from 1 to 25")
            continue
    except Exception:
        print("Please enter a digit from 1 to 25")
        continue

cipher_text = []
for char in plain_text:
    if char.isalpha():
        cipher_value = ord(char) + cipher
        if cipher_value > 90:
            cipher_value -= 26
        cipher_text += [chr(cipher_value)]

    else:
        cipher_text += [char]

cipher_text = ''.join(char for char in cipher_text)
print('Encrypted message: ', cipher_text)
