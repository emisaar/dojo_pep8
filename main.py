""" Main file to run Codebreaker game """
from codebreaker import CodeBreaker

TOTAL_ATTEMPS = 10
codebreaker = CodeBreaker()
ATTEMPT = 0

print("Let's play Codebreaker!\n")

while ATTEMPT != TOTAL_ATTEMPS:
    print("\nAttempt {} of {}".format(ATTEMPT + 1, TOTAL_ATTEMPS))
    NUMBER = str(input('Your guess: '))
    resolve = codebreaker.guess(NUMBER)
    if resolve is True:
        print("You win!")
        break
    if ATTEMPT == TOTAL_ATTEMPS:
        print("You lose!")
    else:
        print(resolve)
    ATTEMPT += 1
