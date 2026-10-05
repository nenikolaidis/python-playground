import random

from ex1_sudoku import EXAMPLE_BOARD, is_valid, solve_sudoku
from ex2_stockstrategy import Stock, buy_signal, sell_signal, create_stocks


def is_solved(board):
    groups = [row for row in board]
    groups += [[board[r][c] for r in range(9)] for c in range(9)]
    groups += [[board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]
               for br in (0, 3, 6) for bc in (0, 3, 6)]
    return all(sorted(group) == list(range(1, 10)) for group in groups)


def test_solves_example_board():
    board = [row[:] for row in EXAMPLE_BOARD]
    assert solve_sudoku(board)
    assert is_solved(board)
    for r in range(9):
        for c in range(9):
            if EXAMPLE_BOARD[r][c]:
                assert board[r][c] == EXAMPLE_BOARD[r][c]


def test_is_valid():
    assert not is_valid(EXAMPLE_BOARD, 0, 2, 5)
    assert not is_valid(EXAMPLE_BOARD, 2, 0, 8)
    assert not is_valid(EXAMPLE_BOARD, 1, 1, 9)
    assert is_valid(EXAMPLE_BOARD, 0, 2, 4)


def test_unsolvable_board():
    board = [row[:] for row in EXAMPLE_BOARD]
    board[0][3] = 5
    assert not solve_sudoku(board)


def make_stock(previous_price, price):
    stock = Stock("TEST", "TST", previous_price)
    stock.price = price
    return stock


def test_buy_signal_at_25_percent_rise():
    assert buy_signal(make_stock(100, 125))
    assert not buy_signal(make_stock(100, 124))


def test_sell_signal_at_10_percent_drop():
    assert sell_signal(make_stock(100, 90))
    assert not sell_signal(make_stock(100, 91))


def test_create_stocks_are_unique():
    random.seed(0)
    stocks = create_stocks(10)
    assert len({s.name for s in stocks}) == 10
    assert len({s.symbol for s in stocks}) == 10
    assert all(10 <= s.price <= 500 for s in stocks)
