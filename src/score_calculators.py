
class ScoreCalculator:
    
    score = 0
    
    def __init__(self):
        self.reset_score()
        
    def reset_score(self):
        self.score = {'correct position':0, 'wrong position':0}
        
    def input_score(self):
        self.score['correct position'] = int(input('How many on the correct position? '))
        if not self.is_score_correct():
            self.score['wrong position'] = int(input('How many on the wrong position? '))
        
    def determine_score(self, guess, code):          
        pairwise = zip(guess, code)            
        self.score['correct position'] = sum(1 for p in pairwise if p[0] == p[1])
        self.score['wrong position'] =  len(set(guess).intersection(set(code))) - \
                                        self.score['correct position']
        return self.score
    
    def right_guess(self):
        return self.score['correct position'] == 4
    
    def process_score(self, combinations_left, guess):
        max_index = len(combinations_left)-1
        for i, combination in enumerate(reversed(combinations_left)):
            if self.score != self.determine_score(combination, guess):
                del combinations_left[max_index-i]

    
class DifferenceScoreCalculator(ScoreCalculator):
    def reset_score(self):
        self.score = 99
    
    def input_score(self):
        self.score = int(input('What\'s my score? '))

    def determine_score(self, guess, code):
        return sum(abs(guess[i] - code[i]) for i in range(len(guess)))

    def right_guess(self):
        return self.score == 0
    
    
