
def input_integer(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f'Please enter a number between {min_value} and {max_value}.')
        except ValueError:
            print('Please enter a valid number.')

class ScoreCalculator:
        
    def __init__(self):
        self.score = {'correct position':0, 'wrong position':0}
        
    def reset_score(self):
        self.score = {'correct position':0, 'wrong position':0}
        
    def input_score(self):
        self.score['correct position'] = \
            input_integer('How many in the correct position? ', 0, 4)
        if not self.right_guess():
            self.score['wrong position'] = \
                input_integer('How many in the wrong position? ', 0, 4)
        
    def determine_score(self, guess, code) -> dict:          
        pairwise = zip(guess, code)
        score = {'correct position':0, 'wrong position':0}            
        score['correct position'] = sum(1 for p in pairwise if p[0] == p[1])
        score['wrong position'] =  len(set(guess).intersection(set(code))) - score['correct position']
        return score
    
    def right_guess(self) -> bool:
        return self.score['correct position'] == 4
    
    def process_score(self, combinations_left, guess):
        max_index = len(combinations_left)-1
        for i, combination in enumerate(reversed(combinations_left)):
            if self.score != self.determine_score(combination, guess):
                del combinations_left[max_index-i]


class DifferenceScoreCalculator(ScoreCalculator):

    def __init__(self):
        self.score = None
    
    def reset_score(self):
        self.score = None
    
    def input_score(self):
        self.score = int(input('What\'s my score? '))
        if self.score is None:
            print('Please enter a valid score.')
            self.input_score()

    def determine_score(self, guess, code) -> int:
        return sum(abs(guess[i] - code[i]) for i in range(len(guess)))

    def right_guess(self) -> bool:
        return self.score == 0
    
    
