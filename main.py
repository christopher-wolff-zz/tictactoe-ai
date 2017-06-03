import random

# Game
class Game:
    '''
    Player 1 (X) is the user
    Player 2 (O) is the computer
    '''

    winningCombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [2, 4, 6]]

    def __init__(self, board=range(9), currentPlayer=1):
        self.board = board
        self.currentPlayer = currentPlayer

    def run(self):
        # Main loop
        while not self.gameOver():
            if self.turn() != 1:
                print('------------')
            print('Turn {}:'.format(self.turn()))

            self.drawBoard()
            self.getMove()
            self.makeMove()
            self.switchPlayer()
        # End of game
        print('------------')
        self.drawBoard()
        if self.value() == 1:
            print('User wins.')
        elif self.value() == -1:
            print('Computer wins.')
        else:
            print("It's a draw.")

    def getMove(self):
        # User
        if self.currentPlayer == 1:
            move = input('User move: ')
            while True:
                if move in self.valid_moves():
                    self.currentMove = move
                    break
                else:
                    move = input('Invalid move. Enter a number between 0 and 8: ')
        # Computer
        else:
            self.minimax()
            print('Comp move: {}'.format(self.currentMove))

    def makeMove(self):
        if self.currentPlayer == 1:
            self.board[self.currentMove] = 'X'
        else:
            self.board[self.currentMove] = 'O'

    def switchPlayer(self):
        if self.currentPlayer == 1:
            self.currentPlayer = 2
        else:
            self.currentPlayer = 1

    def turn(self):
        return len([i for i in self.board if i == 'X' or i == 'O']) + 1

    def gameOver(self):
        if self.value() == 1 or self.value() == -1 or self.turn() > 9:
            return True
        else:
            return False

    def valid_moves(self):
        return [i for i in self.board if i != 'X' and i != 'O']

    def minimax(self, depth=0):
        if self.gameOver():
            return self.value()

        moveValues = {}
        for move in self.valid_moves():
            # Create new Game instance
            possible_game = Game(self.board[:], self.currentPlayer) # Slice the board to lose the reference
            # Execute move
            possible_game.currentMove = move
            possible_game.makeMove()
            possible_game.switchPlayer()
            # Push value to dictionary
            moveValues[move] = possible_game.minimax(depth+1)

        if self.currentPlayer == 1:
            # Player 1 wants to maximize
            max_value = max(moveValues.values())
            return max_value
        else:
            # Player 2 wants to minimize
            min_value = min(moveValues.values())
            # Set current move for the computer
            if depth == 0:
                best_moves = [m for m in moveValues.keys() if moveValues[m] == min_value]
                best_move = random.choice(best_moves)
                self.currentMove = best_move

            return min_value

    # Returns 1 if the user wins, -1 if the computer wins, and 0 otherwise
    def value(self):
        for combo in self.winningCombos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == 'X':
                return 1
            elif self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == 'O':
                return -1
        return 0

    def drawBoard(self):
        print('{} {} {}'.format(self.board[0], self.board[1], self.board[2]))
        print('{} {} {}'.format(self.board[3], self.board[4], self.board[5]))
        print('{} {} {}'.format(self.board[6], self.board[7], self.board[8]))


# Run
if __name__ == '__main__':
    game = Game()
    game.run()
