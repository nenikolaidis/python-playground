def transform_card(card):
    if card == "T":
        return 10
    elif card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    else:
        return int(card)
    
def play_war_game(player1_cards, player2_cards):
    game_history = set()  # To track the game state and detect cycles

    player1_cards = [transform_card(card) for card in player1_cards]
    player2_cards = [transform_card(card) for card in player2_cards]
    
    while player1_cards and player2_cards:
        # Convert the lists to tuples to store in the game history
        game_state = (tuple(player1_cards), tuple(player2_cards))
        
        # Check if the current game state is repeating
        if game_state in game_history:
            return "draw"

        game_history.add(game_state)

        card1 = player1_cards.pop(0)
        card2 = player2_cards.pop(0)

        if card1 == card2:
            player1_cards.append(card1)
            player2_cards.append(card2)
        elif card1 > card2:
            player1_cards.extend([card2])
        else:
            player2_cards.extend([card1])

    if not player1_cards:
        return "player 2"
    elif not player2_cards:
        return "player 1"
    else:
        return "draw"

n = int(input())

for i in range(n):
    player1_cards = input().split()
    
    player2_cards = input().split()

    result = play_war_game(player1_cards, player2_cards)
    print(result)