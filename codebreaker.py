""" CodeBreaker game logic is defined here """
import random


class CodeBreaker:
    """ Main class for the codebreaker game """

    def __init__(self) -> None:
        """ Constructor: Initialize the true number with a random 4 digits number """
        self.true_number = ''
        self.generate_number()

    def generate_number(self):
        """ Generate a random 4 digits number """
        while len(self.true_number) < 4:
            number = str(random.randint(0, 9))
            if number not in self.true_number:
                self.true_number += number

    def guess(self, user_input=None):
        """ Main logic of the game """
        if self.true_number == '':
            # If the true number is not defined
            return 'Number is not defined.\n'
        if user_input is None:
            # If the user input is not defined
            return 'Error, please enter a number.\n'
        if len(user_input) != 4:
            # If the user input is not 4 digits
            return 'Error, please enter a 4-digit number.\n'
        if user_input == self.true_number:
            # If the user input is the true number
            print(self.true_number)
            return True

        answer_array = "" # Array to store the answer
        user_array = list(user_input) # Convert the user input to a list
        appeared_digits = [] # Array to store the digits that have already appeared
        for digit in user_array:
            # Check if the digits are different
            if digit in appeared_digits:
                # Check if the digit has already appeared
                return "All digits must be different.\n"
            appeared_digits.append(digit)

        for i, digit in enumerate(user_array):
            # Check if the digits are in the true number
            if self.true_number[i] == digit:
                # If the digit is in the correct position
                answer_array += 'X'
            elif digit in self.true_number:
                # If the digit is in the wrong position
                answer_array += '_'
            else:
                # If the digit is not in the true number
                answer_array += '•'

        return answer_array
    