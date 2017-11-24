'''Main module.

Creates a tic-tac-toe game against the computer.
Minimax algorithm optimizes decisions.
'''

__author__ = 'Christopher Wolff'
__license__ = 'MIT'
__version__ = '1.0'
__date__ = '6/3/2017'

import random


# Game
class Game:

    '''
    Player 1 (X) is the user
    Player 2 (O) is the computer
    '''

    winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                      [0, 3, 6], [1, 4, 7], [2, 5, 8],
                      [0, 4, 8], [2, 4, 6]]

    def __init__(self, board=[0, 1, 2, 3, 4, 5, 6, 7, 8], current_player=1):
        self.board = board
        self.current_player = current_player

    def run(self):
        # Main loop
        while not self.game_over():
            print('Turn {}:'.format(self.turn()))

            self.draw_board()
            self.get_move()
            self.make_move()
            self.switch_player()

            print('------------')
        # End of game
        self.draw_board()
        if self.value() == 1:
            print('User wins.')
        elif self.value() == -1:
            print('Computer wins.')
        else:
            print("It's a draw.")

    def get_move(self):
        # User
        if self.current_player == 1:
            move = int(input('User move: '))
            while True:
                if move in self.valid_moves():
                    self.current_move = move
                    break
                else:
                    move = input('Invalid move. Enter a number between 0 and 8: ')
        # Computer
        else:
            self.minimax()
            print('Comp move: {}'.format(self.current_move))

    def make_move(self):
        if self.current_player == 1:
            self.board[self.current_move] = 'X'
        else:
            self.board[self.current_move] = 'O'

    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def turn(self):
        return len([i for i in self.board if i == 'X' or i == 'O']) + 1

    def game_over(self):
        if self.value() == 1 or self.value() == -1 or self.turn() > 9:
            return True
        else:
            return False

    def valid_moves(self):
        return [i for i in self.board if i != 'X' and i != 'O']

    def minimax(self, depth=0):
        if self.game_over():
            return self.value()

        move_values = {}
        for move in self.valid_moves():
            # Create new Game instance
            possible_game = Game(self.board[:], self.current_player)
            # Execute move
            possible_game.current_move = move
            possible_game.make_move()
            possible_game.switch_player()
            # Push value to dictionary
            move_values[move] = possible_game.minimax(depth+1)

        if self.current_player == 1:
            # Player 1 wants to maximize
            max_value = max(move_values.values())
            return max_value
        else:
            # Player 2 wants to minimize
            min_value = min(move_values.values())
            # Set current move for the computer
            if depth == 0:
                best_moves = [m for m in move_values.keys() if move_values[m] == min_value]
                best_move = random.choice(best_moves)
                self.current_move = best_move

            return min_value

    def value(self):
        '''Returns 1 if the user wins, -1 if the computer wins, and 0 otherwise.'''
        for combo in self.winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == 'X':
                return 1
            elif self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == 'O':
                return -1
        return 0

    def draw_board(self):
        print('{} {} {}'.format(self.board[0], self.board[1], self.board[2]))
        print('{} {} {}'.format(self.board[3], self.board[4], self.board[5]))
        print('{} {} {}'.format(self.board[6], self.board[7], self.board[8]))


# Run
if __name__ == '__main__':
    game = Game()
    game.run()
