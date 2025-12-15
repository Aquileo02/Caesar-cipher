# import logo from art module
from art import logo

print(logo)
# list containing letter
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# function that takes user text, shift number, and encode or decode choice


def caesar(original_text, shift_amount, encode_or_decode):
    # an empty string to be filled with the de/encoded word
    output_text = ""

    # if user chooses to decode then flip the number sign to go in reverse in the list index
    if encode_or_decode == "decode":
        shift_amount *= -1
    # if letter in user text no in the alphabet add to end of string
    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            # if letter in list then shift the index down or up, if the index
            # goes out of range start at the start or end of list
            # add that letter to output text
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# bool if user wants to decode or encode another word
should_continue = True

# while loop takes choice, text, and shift amount input and calls caesar cipher
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt. :\n").lower()
    if direction != "encode" and direction != "decode":
        print("Invalid entry, please choose 'encode' or 'decode'.")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

        # if user chooses to not encode or decode again end the program
        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
        if restart == 'no':
            should_continue = False
            print("Good-bye")
