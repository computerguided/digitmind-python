import random


def create_combinations():
    digits = list(range(0,10))
    return [(w, x, y, z)        \
        for w in digits         \
        for x in digits         \
        for y in digits         \
        for z in digits         \
        if  w not in (x,y,z)    \
        and x not in (y,z)      \
        and y != z ]

def determine_score(combination, code):
    pairwise = zip(combination, code)
    num_correct_position = len([idx for idx, pair in enumerate(pairwise) \
                                if pair[0] == pair[1]])

    num_wrong_position = len(set(combination).intersection(set(code)))-num_correct_position
    score = {'correct position':num_correct_position, 'wrong position':num_wrong_position}
    return score
    
def process_score(combinations_left, tried_combination, score):
    max_index = len(combinations_left)-1
    for i, combination in enumerate(reversed(combinations_left)):
        if score != determine_score(combination, tried_combination):
            del combinations_left[max_index-i]

def do_computer_move(combinations_left):
    guess = random.choice(combinations_left)
    
    print('My guess:', guess)

    score['correct position'] = int(input('How many on the correct position? '))
    
    if score['correct position'] != 4:
        score['wrong position'] = int(input('How many on the wrong position? '))
        process_score(combinations, guess, score)
    
    return score
    

combinations = create_combinations()

code  = [5, 4, 8, 1]

score = {'correct position':0, 'wrong position':0}

while score['correct position'] != 4:
    score = do_computer_move(combinations)
        
print('YES!')





