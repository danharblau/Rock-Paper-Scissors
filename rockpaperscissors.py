import random

moves = ['rock', 'paper', 'scissors']


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class CyclePlayer(Player):
    def move(self):
        my_move = None
        their_move = None
        self.learn_move = (self, my_move, their_move)
        if self.my_move is None:
            return random.choice(moves)
        if self.my_move == "rock":
            return self.my_move
        elif self.my_move == "scissors":
            return self.my_move
        else:
            return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, or scissors?").lower()
            if move in moves:
                return move
            print("Invalid input! Try again!")


class ReflectPlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game():
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
            print("Player 1 wins")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player 2 wins")
        else:
            print("Tie!")
        print("The score is:")
        print(f"Player 1: {self.p1_score}")
        print(f"Player 2: {self.p2_score}")
    
    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move

    def play_game(self):
        print("Begin")
        self.rounds = 5
        for round in range(self.rounds):
            print(f"Round {round}:")
            self.play_round()
        print(f"Final score: Player 1: {self.p1_score}\
              Player 2: {self.p2_score}")
        print("Game over!")

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move

if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
