from deuces import Card, Evaluator, Deck
import itertools

evaluator = Evaluator()

def preflop_monte_carlo(hand, num_opps, iterations=100000):
    for num_players in range(1, num_opps):
        wins = 0
        ties = 0
        losses = 0

        for i in range(iterations):

            deck = Deck()
            for card in hand:
                deck.cards.remove(card)

            board = deck.draw(5)

            hero_score = evaluator.evaluate(board, hand)

            villain_hands = []
            villain_scores = []
            for i in range(num_players):
                villain_hand = deck.draw(2)
                villain_hands.append(villain_hand)
                villain_scores.append(evaluator.evaluate(board, villain_hand))
            
            if hero_score < min(villain_scores):
                wins += 1
            elif hero_score == min(villain_scores):
                ties += 1
            else:
                losses += 1

        mc_IR = (wins + ties / 2) / (wins + losses + ties)
        print("Number of Opponents: ", num_players)
        print("Wins: ", wins)
        print("Losses: ", losses)
        print("Ties: ", ties)
        print("Monte Carlo IR: ", mc_IR)

        return mc_IR


# wont run - approx 2 billion cases 
def preflop_ir(hand):
    wins = 0
    ties = 0
    losses = 0

    deck = Deck()
    for card in hand:
        deck.cards.remove(card)

    for oppcards in itertools.combinations(deck.cards, 2):

        oppcards = list(oppcards)

        # Remove the cards from the deck.
        for card in oppcards:
            deck.cards.remove(card)

        for board in itertools.combinations(deck.cards, 5):
            
            board = list(board)

            hero_score = evaluator.evaluate(board, hand)
            villain_score = evaluator.evaluate(board, oppcards)

            if hero_score < villain_score:
                wins += 1
            elif hero_score == villain_score:
                ties += 1
            else:
                losses += 1

        # Restore the cards to the deck.
        for card in oppcards:
            deck.cards.append(card)

    mc_IR = (wins + ties / 2) / (wins + losses + ties)
    print("Wins: ", wins)
    print("Losses: ", losses)
    print("Ties: ", ties)
    print("IR: ", mc_IR)


if __name__ == '__main__':
    hand = [Card.new('Ah'), Card.new('3c')]
    preflop_monte_carlo(hand, 2)
    # preflop_ir(hand)
