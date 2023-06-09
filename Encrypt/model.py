"""
Make a model for encrypting and decrypting messages with a key (for unicode table of values.
"""


def operation(message, key):
    if choose_operation == "encrypt":
        for char in message:
            print(chr(ord(char) + key), end="")
    elif choose_operation == "decrypt":
        for char in message:
            print(chr(ord(char) - key), end="")
    else:
        print("Nije dobar unos operacije. \nIzaberite encrypt ili decrypt.")


input_message = input("Uneti poruku: ")
input_key = int(input("Uneti broj između 1 i 5: "))


while 0 < input_key < 6:
    choose_operation = input("Uneti operaciju: ")
    operation(input_message, input_key)
    break
else:
    print("Pogrešan unos")
