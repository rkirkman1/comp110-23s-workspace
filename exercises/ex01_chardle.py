"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730401129"

word: str = input("Enter a five character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
else:
    print("Searching for " + character + " in " + word)

number: int = 0

if (character == word[0]):
    print(character + " found at index 0")
    number += 1
if (character == word[1]):
    print(character + " found at index 1")
    number += 1
if (character == word[2]):
    print(character + " found at index 2")
    number += 1
if (character == word[3]):
    print(character + " found at index 3")
    number += 1
if (character == word[4]):
    print(character + " found at index 4")
    number += 1

number_1 = str(number)

if number_1 == "0":
    print("No instances of " + character + " found in " + word)
else:
    if number_1 == "1":
        print("1 instance of " + character + " found in " + word)
    else:
        print(number_1 + " instances of " + character + " found in " + word)