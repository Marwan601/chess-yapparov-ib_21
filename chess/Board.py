from chess.Color import WHITE, BLACK
from chess.Knight import Knight
from chess.Pawn import Pawn
from chess.Rook import Rook
from chess.Bishop import Bishop
from chess.King import King
from chess.Queen import Queen

class Board:
    def __init__(self):
        self.__board = []
        for y in range(8):
            cols = []
            for x in range(8):
                cols.append(None)
            self.__board.append(cols)
        self.__player = WHITE
        for col in range(8):
            self.__board[1][col] = Pawn(WHITE)
            self.__board[6][col] = Pawn(BLACK)
        for col in [0, 7]:
            self.__board[0][col] = Rook(WHITE)
            self.__board[7][col] = Rook(BLACK)
        for col in [1, 6]:
            self.__board[0][col] = Knight(WHITE)
            self.__board[7][col] = Knight(BLACK)
        for col in [2, 5]:
            self.__board[0][col] = Bishop(WHITE)
            self.__board[7][col] = Bishop(BLACK)
        for col in [4]:
            self.__board[0][col] = King(WHITE)
            self.__board[7][col] = King(BLACK)
        for col in [3]:
            self.__board[0][col] = Queen(WHITE)
            self.__board[7][col] = Queen(BLACK)


    @property
    def player(self) -> int:
        return self.__player

    @property
    def board(self) -> list[list]:
        return self.__board

    @staticmethod
    def validate(row: int, col: int) -> bool:
        return 0 <= row <= 7 and 0 <= col <= 7

    def get_item(self, row: int, col: int):
        if self.validate(row, col):
            return self.__board[row][col]
        return None

    def move_item(self,
                  row_start: int,
                  col_start: int,
                  row_end: int,
                  col_end: int):
        self.__board[row_end][col_end] = self.__board[row_start][col_start]
        self.__board[row_start][col_start] = None

    def change_player(self):
        if self.player == WHITE:
            self.__player = BLACK
        else:
            self.__player = WHITE