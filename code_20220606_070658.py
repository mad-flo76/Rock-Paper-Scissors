import random

moves = ['rock', 'paper', 'scissors']


def valid_input(prompt, op1, op2, op3):
    while True:
        response = input(prompt).lower()
        if response == op1:
            break
        elif response == op2:
            break
        elif response == op3:
            break
        else:
            print("I don't Understand.\n")
    return response


def player_type():
    players = [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    return random.choice(players)


def defeats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Opponent:
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Opponent):
    def move(self):
        response = valid_input("Please choose\n", "rock,", "paper", "scissors")
        return response


class RandomPlayer(Opponent):
        def move(self):
            return random.choice(moves)


class ReflectPlayer(Opponent):
        def move(self):
            if self.their_move is None:
                return random.choice(moves)
            elif self.their_move in moves:
                return self.their_move


class CyclePlayer(Opponent):
        def move(self):
            if self.my_move is None:
                return random.choice(moves)
            else:
                index = moves.index(self.my_move) + 1
                index = 0
                return moves[index]


class Game:
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2

        def play_round(self):
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"\nPlayer1:{move1} Player 2: {move2}")
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)
            while True:
                if move1 == move2:
                    print("**Tie!**\n")
                elif beats(move1, move2) is Ture:
                    print("**player 2 wins**\n")
                self.p2.count += 1
                return self.p1.count and self.p2.count

        def play_game(self):
            self.p1.count = 0
            self.p2.count = 0
            print("\nrock,paper, scissors,START\n")
            for round in range(3):
                print(f"Round {round + 1}:")
                self.play_round()
            print("Fatality!\n")
            print(f"Score:\n")
            f"Player 1: {self.p1.count}\n"
            f"Player 2:{self.p2.count}\n"

        def play_again(self):
            response = valid_input("Play again?""y" or "n", "m")
            if "y" in response:
                print("Okay")
                self.play_game()
            elif "n" in response:
                print("\n Good-Bye \n")
                exit()

if __name__ == '__main__':

        game = Game(HumanPlayer(), player_type())
        game.play_game()

        while True:
            game = Game(HumanPlayer(), player_type())
            game.play_again()
