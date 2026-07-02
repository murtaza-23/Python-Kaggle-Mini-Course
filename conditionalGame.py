print("\tGUESS THE NUMBER\t\n")

number = 9
print("\nGuess the number between 1-10")
print("\nYou have 3 tries. Best of Luck")

tries = 3


while tries > 0:
    guess = input("\nGuess: ")
    if int(guess) == number:
        print("\nCongratulations! You won")
        break
    else:
        tries -= 1
        print(f'Tries left: {tries}')

else:
    print("\nSorry! You Lost")



