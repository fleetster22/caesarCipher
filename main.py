# Day 8 of 100 Days of Code - The Complete Python Pro Bootcamp for 2021
import time
import math
from art import logo

# def greet(name):
#     print(f"Rise and shine, {name}!")
#     time.sleep(2)
#     print("Seize the motherfucking day!")
#     time.sleep(2)
#     print("Be Epic!")
#
#
# greet("Nubs")

# def greet_with(name, location):
#     print(f"Whaddup bitches. My name is {name} and I am from {location}")
#

# greet_with("Anaka", "Colorado")
# greet_with(location="Denver", name="Nubs")


# Paint Area Calculator
# def paint_calc(height, width, cover):
#     # to round up use math.ceil
#     area = height * width
#     number_of_cans = math.ceil(area / cover)
#     print(f"You will need {number_of_cans} cans of paint for this room")
#
# room_h = int(input("Height of wall: "))
# room_w = int(input("Width of wall: "))
# coverage = 5
#
# paint_calc(height=room_h, width=room_w, cover=coverage)


# Prime Number Checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")
#
#
# n = int(input("Check this number:\n"))
#
# prime_checker(number=n)


# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)


# def encrypt(plain_text, shift_amt):
#     cipher_msg = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amt
#         cipher_msg += alphabet[new_position]
#     print(f"Here's your encrypted message: {cipher_msg}")
#
#
# def decrypt(cipher_msg, shift_amt):
#     plain_text = ""
#     for letter in cipher_msg:
#         position = alphabet.index(letter)
#         new_position = position - shift_amt
#         plain_text += alphabet[new_position]
#     print(f"Here's your decrypted message: {plain_text}")
#
#
# if direction == "encode":
#     encrypt(plain_text=msg, shift_amt=shift)
# else:
#     decrypt(cipher_msg=msg, shift_amt=shift)

# OPTIMIZED Above Code

def caesar(start_text, shift_amt, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amt *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amt
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's your {cipher_direction}d message: {end_text}")


go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    msg = input("Type your message:\n").lower()
    shift = int(input("Enter the shift number:\n"))
    shift = shift % 26 + 1
    caesar(start_text=msg, shift_amt=shift, cipher_direction=direction)

    result = input("Type 'yes' if you would lke to go again. Otherwise type 'no'\n")
    if result == "no":
        go_again = False
        print("OK. Goodbye.")
