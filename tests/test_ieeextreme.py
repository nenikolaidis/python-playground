import pytest

from restaurant_cipher import most_frequent_lowercase_to_uppercase
from war_games import transform_card, play_war_game


@pytest.mark.parametrize("card, value", [
    ("2", 2), ("9", 9), ("T", 10), ("J", 11), ("Q", 12), ("K", 13), ("A", 14),
])
def test_transform_card(card, value):
    assert transform_card(card) == value


def test_war_player_with_higher_cards_wins():
    assert play_war_game(["A", "K"], ["2", "3"]) == "player 1"
    assert play_war_game(["2", "3"], ["A", "K"]) == "player 2"


def test_war_repeating_game_is_a_draw():
    assert play_war_game(["5"], ["5"]) == "draw"


def test_war_sample_input(monkeypatch, capsys):
    import war_games
    lines = iter(["1", "2 3 A", "K 4 5"])
    monkeypatch.setattr("builtins.input", lambda: next(lines))
    war_games.main()
    assert capsys.readouterr().out == "player 2\n"


@pytest.mark.parametrize("text, expected", [
    ("abc a", "A"),
    ("gggg ff", "G"),
    ("hello, world!", "E"),
])
def test_most_frequent_letter(text, expected):
    assert most_frequent_lowercase_to_uppercase(text) == expected


def test_no_letters_a_to_g():
    assert most_frequent_lowercase_to_uppercase("xyz") is None
