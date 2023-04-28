import random

random.seed(1234)

class Game:
    def __init__(self):
        self.score = 0
    
    def play_round(self):
        # Simula um round do jogo
        roll = random.randint(1, 6)
        if roll == 1:
            self.score = 0
        else:
            self.score += roll
    
    def play_game(self):
        # Simula uma partida completa do jogo
        while self.score < 100:
            self.play_round()
    
    def __str__(self):
        return "Score: " + str(self.score)

# Simula vários jogos com a mesma semente
for i in range(5):
    game = Game()
    game.play_game()
    print("Jogo", i+1, "-", game)