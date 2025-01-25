import random

from score_calculators import *

def create_combinations(difficulty_level : int) -> list:
    digits = list(range(difficulty_level + 3))
    return [(w,x,y,z)           \
        for w in digits         \
        for x in digits         \
        for y in digits         \
        for z in digits         \
        if  w not in (x,y,z)    \
        and x not in (y,z)      \
        and y != z ]

def do_computer_move(score_calculator : ScoreCalculator, combinations_left : list, difficulty_level : int):
    
    # Input error handling
    if len(combinations_left) == 0:
        print("You probably made an error in specifying the score for one of my guesses!")
        print("Let's start over..")
        combinations_left.extend(create_combinations(difficulty_level))

    guess = random.choice(combinations_left)
    print('My guess:', guess)
    
    score_calculator.input_score()
    score_calculator.process_score(combinations_left, guess)

def set_score_calculator() -> ScoreCalculator:
    # Instantiate score calculator
    if input("Specify the scoring type [p=position, d=difference]: ") == 'p':
        return ScoreCalculator()
    else:
        return DifferenceScoreCalculator()
    
def set_difficulty_level() -> int:
    return input_integer("Give the difficulty level [1..7]: ", 1, 7)

def input_guess(difficulty_level : int) -> list:
    # Convert digits to strings for comparison
    digit_chars = [str(i) for i in range(10)[:difficulty_level+3]]
    while True:
        input_string = input("Your next guess: ")
        if len(input_string) == 4 \
                and all(c in digit_chars for c in input_string) \
                and len(set(input_string)) == 4:
            return [int(c) for c in input_string]
        print(f"Please enter a valid guess containing 4 different digits from {digit_chars}.")

# Main program

print("\n---- Digitmind ----\n")

# Init game
score_calculator = set_score_calculator()
difficulty_level = set_difficulty_level()

# Human codebreaker
combinations = create_combinations(difficulty_level)
code = random.choice(combinations)

print("\nOk, I've chosen a code, try to guess it!\n")

while not score_calculator.right_guess():
    guess = input_guess(difficulty_level)
    score_calculator.score = score_calculator.determine_score(guess, code)
    print('Your score:', score_calculator.score)

print("\nCorrect! Well done!")

# Computer codebreaker

input("\nOk, now it's my turn. Choose a code and I'll try to break it! (press key to continue)\n")

combinations = create_combinations(difficulty_level)
score_calculator.reset_score()
while not score_calculator.right_guess():
    do_computer_move(score_calculator, combinations, difficulty_level)
        
print('YES!')