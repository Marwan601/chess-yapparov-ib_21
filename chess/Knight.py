from chess.Color import WHITE
from chess.Figure import Figure
from chess import Board

class Knight(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wN'
        return 'bN'

    def can_move(
            self,
            board: Board,
            row_start: int,
            col_start: int,
            row_end: int,
            col_end: int) -> bool:
        col_diff = abs(col_end - col_start)
        row_diff = abs(row_end - row_start)
        return col_diff == 2 and row_diff == 1 or col_diff == 1 and row_diff == 2

    def can_attack(
        self,
            board: Board,
            row_start: int,
            col_start: int,
            row_end: int,
            col_end: int) -> bool:
        is_white = self.color == WHITE
        if col_end != col_start-1 and col_end != col_start+1:
            return False
        if is_white and row_end != row_start + 1:
            return False
        if not is_white and row_end != row_start - 1:
            return False
        return True

