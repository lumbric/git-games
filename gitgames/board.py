import re
from pathlib import Path


class Board:
    FNAME = None  # to be defined in subclass
    TEMPLATE_FNAME = None  # to be defined in subclass

    def __init__(self, fields):
        self.fields = fields

    @classmethod
    def from_file(cls):
        with open(cls.FNAME, 'r') as f:
            board_str = f.read()
        return cls.from_str(board_str)

    @classmethod
    def from_str(cls, board_str):
        raise NotImplementedError("to be implemented in subclass")

    def __eq__(self, other):
        return self.fields == other.fields

    def is_empty(self):
        raise NotImplemented  # TODO


class TicTacToeBoard(Board):
    FNAME = Path(__file__).parent.parent / 'tic-tac-toe' / 'board'
    TEMPLATE_FNAME = 'board-tic-tac-toe'

    def __init__(self, fields=None):
        if fields is None:
            fields = [['.'] * 3 for _ in range(3)]

        if len(fields) != 3 or any(len(row) != 3 for row in fields):
            raise ValueError('invalid board size, must be 3 x 3')

        valid_chars = 'O', 'X', '.'
        if any(field.upper() not in valid_chars
               for rows in fields
               for field in rows):
            raise ValueError("invalid character on game board, "
                             f"allowed: {', '.join(valid_chars)}")

        super().__init__(fields)

    @classmethod
    def from_str(cls, board_str):
        fname = Path(__file__).parent / cls.TEMPLATE_FNAME
        with open(fname, 'r') as f:
            board_template = f.read()
        board_template = board_template.replace('|', '\\|').replace('.', '([OXox.])')

        match = re.search(board_template, board_str)
        fields_flat = match.groups()
        fields = [list(fields_flat[i:i+3]) for i in range(0, 9, 3)]

        board = cls(fields)
        return board


class InvalidMove(Exception):
    ...


class Move:
    def __init__(self, old_board, new_board):
        changed_fields = [(i, j) for i in range(3) for j in range(3)
                          if old_board.fields[i][j] != new_board.fields[i][j]]

        if len(changed_fields) == 0:
            raise InvalidMove
        elif len(changed_fields) > 1:
            ...

        row, col = changed_fields[0]

        if old_board[row][col] != '.':
            ...

        if new_board[row][col] not in PLAYERS:
            ...

        return new_board[row][col].lower()
