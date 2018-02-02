import random

def create_combinations(difficulty_level):
    digits = [1,2,3,4,5,6,7,8,9,0][:difficulty_level+3]
    return [(w, x, y, z)        \
        for w in digits         \
        for x in digits         \
        for y in digits         \
        for z in digits         \
        if  w not in (x,y,z)    \
        and x not in (y,z)      \
        and y != z ]

def determine_score_alternative(combination, code):
    score = {'correct position':0, 'wrong position':0}
    pairwise = zip(combination, code)
    score['correct position'] = sum(i for i, p in enumerate(pairwise) if p[0] == [1])
    score['wrong position'] = len(set(combination).intersection(set(code))) - \
                              score['correct position']
    return score

def determine_score(combination, code):
    score = {'correct position':0, 'wrong position':0}
    for i in range(len(combination)):
        if combination[i] == code[i]:
            score['correct position'] += 1
        elif combination[i] in code:
            score['wrong position'] += 1
    return score

def determine_score_difference(combination, code):
    return sum(abs(combination[i] - code[i]) for i in range(len(combination)))
    
def process_score(combinations_left, tried_combination, score):
    max_index = len(combinations_left)-1
    for i, combination in enumerate(reversed(combinations_left)):
        if score != determine_score(combination, tried_combination):
            del combinations_left[max_index-i]
            
def process_score_alternative(combinations_left, tried_combination, score):
    max_index = len(combinations_left)-1
    for i, combination in enumerate(reversed(combinations_left)):
        if score != determine_score(combination, tried_combination):
            del combinations_left[max_index-i]

def do_computer_move(combinations_left, difficulty_level):
    
    # Input error handling
    if len(combinations_left) == 0:
        print("You probably made an error in specifying the score for one of my guesses!")
        print("Let's start over..")
        combinations_left.extend(create_combinations(difficulty_level))

    guess = random.choice(combinations_left)
    print('My guess:', guess)

    score['correct position'] = int(input('How many on the correct position? '))
    
    if score['correct position'] != 4:
        score['wrong position'] = int(input('How many on the wrong position? '))
        process_score(combinations_left, guess, score)
    
    return score

# Main program

print("\n---- Digitmind ----\n")

difficulty_level = int(input("Give the difficulty level [1..7]: "))

# Human codebreaker
combinations = create_combinations(difficulty_level)
code = random.choice(combinations)

print("\nOk, I’ve chosen a code, try to guess it!\n")

score = {'correct position':0, 'wrong position':0}
while score['correct position'] != 4:
    guess = [int(c) for c in input("Your next guess: ") ]
    score = determine_score(code, guess)
    print(score)

print("\nCorrect! Well done!")

# Computer codebreaker
combinations = create_combinations(difficulty_level)
score = {'correct position':0, 'wrong position':0}
while score['correct position'] != 4:
    score = do_computer_move(combinations, difficulty_level)
        
print('YES!')





