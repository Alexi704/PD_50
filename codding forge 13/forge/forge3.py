class Player:

    def __init__(self):
        self.name = 0
        self.score = 0

    def set_score(self, value):
        self.score = value
        return self.score

    def get_score(self):
        return self.score
