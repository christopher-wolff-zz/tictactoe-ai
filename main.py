# Game
class Game:

    '''
    Player 1 (X) is the user
    Player 2 (O) is the computer
    '''

    winningCombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [2, 4, 7]]

    def __init__(self, board = [str(i) for i in range(9)], turn = 1, currentPlayer = 1):
        self.board = board
        self.turn = turn
        self.currentPlayer = currentPlayer

    def run(self):
        while not self.gameOver():
            # Print turn number
            if self.turn is not 1:
                print('------------')
            print('Turn {}:'.format(self.turn))
            # Main logic
            self.drawBoard()
            self.getMove()
            self.makeMove()
            self.switchPlayer()
            self.turn = self.turn + 1

    def getMove(self):
        if self.currentPlayer == 1:
            move = input('User move: ')
            # TODO: Check move validity
            self.currentMove = int(move)
        else:
            move = 4
            print('Comp move: {}'.format(move))
            self.currentMove = move

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

    def gameOver(self):
        if self.value() == 1:
            print('------------')
            self.drawBoard()
            print('User wins.')
            return True
        elif self.value() == -1:
            print('------------')
            self.drawBoard()
            print('Computer wins.')
            return True
        elif self.turn > 9:
            print('------------')
            self.drawBoard()
            print("It's a draw.")
            return True
        else:
            return False

    # value returns 1 if the user wins, -1 if the computer wins, and 0 otherwise
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
