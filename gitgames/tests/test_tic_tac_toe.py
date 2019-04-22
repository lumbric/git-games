from pytest import raises

from ..board import TicTacToeBoard


def test_default_init():
    board = TicTacToeBoard()
    assert len(board.fields) == 3
    assert all('.' == field
               for row in board.fields
               for field in row)


def test_read_file():
    board = TicTacToeBoard.from_file()
    assert len(board.fields) == 3
    assert board == TicTacToeBoard()


def test_invalid_players():
    fields = [
        ['a', 'b', 'c'],
        ['a', 'b', 'c'],
        ['a', 'b', 'c'],
    ]
    with raises(ValueError, match='invalid character'):
        TicTacToeBoard(fields)


def test_invalid_board_size():
    with raises(ValueError, match='invalid board size'):
        TicTacToeBoard([[1], [2]])
