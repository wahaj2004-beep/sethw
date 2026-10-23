secretset = {1,3,5, 6, 7}
my_guess = set()

print("Guess the secret numbers!")

while my_guess != secretset:
    guess = int(input("Enter a number: "))

    if guess in secretset:
        my_guess.add(guess)
        print("Correct")
    else:
        print("wrong")

print("You won")