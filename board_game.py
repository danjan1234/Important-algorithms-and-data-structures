from collections import deque

class Player:
    def __init__(self, name, board):
        self.name = name
        self._board = board

    def play(self, cell):
        self._board.update_board(cell, self.name)
        print("{} has played".format(self.name))

class Cell:
    def __init__(self, i, j):
        self.i, self.j = i, j

class Board:
    def __init__(self, size):
        self._arr = [['X' for _ in range(size)] for _ in range(size)]
        self._empty_slots = size ** 2

    def update_board(self, cell, identifier):
        self._arr[cell.i][cell.j] = identifier
        self._empty_slots -= 1

    def is_full(self):
        return self._empty_slots == 0

class BoardGame:
    def __init__(self, size=10):
        self._board = Board(size)
        self._p1 = Player('A', self._board)
        self._p2 = Player('B', self._board)
        self._q = deque()

    def initialize(self):
        print("{} vs {}".format(self._p1.name, self._p2.name))
        self._q.append(self._p1)
        self._q.append(self._p2)

    def play(self, cell):
        curr_player = self._q.popleft()
        curr_player.play(cell)
        if self._check_win():
            print("{} has won".format(curr_player.name))
            self._exit()
        elif self._board.is_full():
            print("Cannot play more moves. Game exit.")
            self._exit()
        self._q.append(curr_player)

    def _check_win(self):
        print("Check win ...")

    def _exit(self):
        print("Game exiting...")


if __name__ == '__main__':
    game = BoardGame(3)
    game.initialize()
    game.play(Cell(0, 0))
    game.play(Cell(0, 1))
    game.play(Cell(0, 2))
    game.play(Cell(1, 0))
    game.play(Cell(1, 1))
    game.play(Cell(1, 2))
    game.play(Cell(2, 0))
    game.play(Cell(2, 1))
    game.play(Cell(2, 2))
    
    game.play(Cell(2, 2))
    pass

