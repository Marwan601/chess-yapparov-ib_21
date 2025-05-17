from chess.Color import WHITE
from chess.Figure import Figure
from chess import Board

class Queen(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wQ'
        return 'bQ'

    def can_move(self,
                 board: Board,
                 row_start: int,
                 col_start: int,
                 row_end: int,
                 col_end: int
                 ) -> bool:
        row_diff = abs(row_end - row_start)
        col_diff = abs(col_end - col_start)
        if col_diff == row_diff:
            row = row_start
            col = col_start
            row_step = 1 if row_start < row_end else -1
            col_step = 1 if col_start < col_end else -1
            for i in range(col_diff - 1):
                row += row_step
                col += col_step
                other_player = board.get_item(row, col)
                if other_player:
                    return False
            return True
        elif row_diff and not col_diff:
            row_step = 1 if row_end > row_start else -1
            for row in range(row_start + row_step, row_end, row_diff):
                figure = board.get_item(row, col_start)
                if figure:
                    return False
            return True
        elif not row_diff and col_diff:
            col_step = 1 if col_end > col_start else -1
            for col in range(col_start + col_step, col_end, col_diff):
                figure = board.get_item(row_start, col)
                if figure:
                    return False
            return True
        return False