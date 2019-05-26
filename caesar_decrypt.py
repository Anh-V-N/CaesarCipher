# This script is to brute force message encrypted using caesar cipher
print('Caesar Cipher Decryptor')
print('='*25, '\n')

cipher_text = input("Encrypted message to crack: ").upper()

print('Possible plaintext messages: ')
for i in range(1, 26):
    plaintext = []
    for char in cipher_text:
        if char.isalpha():
            plaintext_value = ord(char) + i
            if plaintext_value > 90:
                plaintext_value -= 26
            plaintext += [chr(plaintext_value)]
        else:
            plaintext += [char]
    plaintext = ''.join(char for char in plaintext)
    print(plaintext)
