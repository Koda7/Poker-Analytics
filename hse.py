import itertools
from deuces import Card, Evaluator, Deck
# from hse.hse_2 import hse_2
# from hse.hse_1 import hse_1

evaluator = Evaluator()

def hse_1(board, hand):
    wins = 0
    losses = 0
    ties = 0

    deck = Deck()

    for card in board + hand: 
        deck.cards.remove(card)

    hero_score = evaluator.evaluate(board, hand)
    hero_class = evaluator.get_rank_class(hero_score)

    # for all possible starting hands the opponent could have
    for i in range(len(deck.cards)):
        for j in range(i + 1, len(deck.cards)):

            villain_hand = [deck.cards[i], deck.cards[j]]
            villain_score = evaluator.evaluate(board, villain_hand)
        
            if hero_score < villain_score:
                wins += 1
            elif hero_score > villain_score:
                losses += 1
            else:
                ties += 1

    print("Hero best hand:")
    Card.print_pretty_cards(evaluator.get_best_hand(board, hand))
    print("Rank: ", hero_score)
    print("Class: ", evaluator.class_to_string(hero_class))

    print("Wins: ", wins)
    print("Losses: ", losses)
    print("Ties: ", ties)

    hse = (wins + ties / 2) / (wins + losses + ties)
    print("HSE: ", hse)
    return hse

def hse_2(board, hand):
    wins = 0
    losses = 0
    ties = 0

    deck = Deck()

    for card in board + hand: 
        deck.cards.remove(card)
    
    hero_score = evaluator.evaluate(board, hand)
    hero_class = evaluator.get_rank_class(hero_score)

    # for all possible starting hands the opponent could have
    for oppcards_1 in itertools.combinations(deck.cards, 2):

        oppcards1 = list(oppcards_1)

        # Remove the cards from the deck.
        for card in oppcards1:
            deck.cards.remove(card)

        villain_score1 = evaluator.evaluate(board, oppcards1)

        # all possible hands of second opponent
        for oppcards_2 in itertools.combinations(deck.cards, 2):

            oppcards2 = list(oppcards_2)

            villain_score2 = evaluator.evaluate(board, oppcards2)

            if hero_score < min(villain_score1, villain_score2):
                wins += 1
            elif hero_score == min(villain_score1, villain_score2):
                ties += 1
            else:
                losses += 1

        # adding the cards back
        for card in oppcards1:
            deck.cards.append(card)

    print("Hero best hand:")
    Card.print_pretty_cards(evaluator.get_best_hand(board, hand))
    print("Rank: ", hero_score)
    print("Class: ", evaluator.class_to_string(hero_class))

    print("Wins: ", wins)
    print("Losses: ", losses)
    print("Ties: ", ties)

    hse = (wins + ties / 2) / (wins + losses + ties)
    print("HSE_2: ", hse)
    return hse

if __name__ == "__main__":
    hand = [Card.new('2s'), Card.new('3c')]

    board = [Card.new('Th'), Card.new('8h'), Card.new('6h')]

    h_1 = hse_1(board, hand)
    print("------")
    h_2 = hse_2(board, hand)
    print("------")
    print("Adjusted HSE for 2 players:", pow(h_1, 2))
    print("HSE_2:", h_2)