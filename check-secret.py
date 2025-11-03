secret = "Haris@123"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess!=secret and not(out_of_guess):
    if guess_count<guess_limit:
        guess = input('Incorrect Secret! Please try again\n')
        guess_count+=1
    else:
        out_of_guess = True
if out_of_guess:
    print("You are out of guesses! YOU LOSE")
else:
    print('Congratulations! YOU WON..')