from deuces import Card, Evaluator, Deck
from preflop import preflop_monte_carlo
from hse import hse_1
from hp import HandPotential_1, HandPotential_2
from percentage_rank import percentage_rank
from odds import mc_odds_calculator

deck = Deck()
evaluator = Evaluator()
num_opps = 1

# hero_hand = deck.draw(2)
hero_hand = [Card.new('7c'), Card.new('Jd')]
# villain_hand = deck.draw(2)
villain_hand = [Card.new('5h'), Card.new('6s')]


print("Hero's hand:")
Card.print_pretty_cards(hero_hand)

print("Villain's hand:")
Card.print_pretty_cards(villain_hand)
print("--------------------")
print("------Preflop------")
print("---Hero---")
preflop_monte_carlo(hero_hand, 2)
print("---Villain---")
preflop_monte_carlo(villain_hand, 2)
print("--------------------")
print("------Odds------")
mc_odds_calculator(hero_hand, villain_hand)
print("--------------------")


# remove hands from deck
for card in hero_hand + villain_hand:
    deck.cards.remove(card)

# board = deck.draw(3)

board = [Card.new('3c'), Card.new('Kc'), Card.new('5s')]
for card in board:
    deck.cards.remove(card)

# remove the cards from the heros hand, villains hand and the board from the deck


print("Board:")
Card.print_pretty_cards(board)
print("Hero's hand rank: ", percentage_rank(board, hero_hand))
print("Villain's hand rank: ", percentage_rank(board, villain_hand))

print("--------------------")

print("------HSE1------")
print("---Hero---")
h_1 = hse_1(board, hero_hand)
print("---Villain---")
h_2 = hse_1(board, villain_hand)

print("--------------------")

print("--------------------")

print("------HP!------")
print("---Hero---")
HandPotential_1(board, hero_hand)
print("---Villain---")
HandPotential_1(board, villain_hand)

print("--------------------")

print("------HandPotential2------")
print("---Hero---")
pp_1, np_1 = HandPotential_2(board, hero_hand)
print("---Villain---")
pp_2, np_2 = HandPotential_2(board, villain_hand)
print("--------------------")

print("------EHS------")
print("---Hero---")
ehs_1 = h_1 + (1 - h_1) * pp_1
print("EHS: ", ehs_1)
print("---Villain---")
ehs_2 = h_2 + (1 - h_2) * pp_2
print("EHS: ", ehs_2)
print("--------------------")

turn = deck.draw(1)
board = board + [turn]

print("Board:")
Card.print_pretty_cards(board)
print("Hero's hand rank: ", percentage_rank(board, hero_hand))
print("Villain's hand rank: ", percentage_rank(board, villain_hand))

print("--------------------")

print("------HSE1------")
print("---Hero---")
hse_1(board, hero_hand)
print("---Villain---")
hse_1(board, villain_hand)
print("--------------------")

print("------HandPotential1------")
print("---Hero---")
HandPotential_1(board, hero_hand)
print("---Villain---")
HandPotential_1(board, villain_hand)
print("--------------------")

river = deck.draw(1)
board = board + [river]

print("Board:")
Card.print_pretty_cards(board)

print("Hero's hand rank: ", percentage_rank(board, hero_hand))
print("Villain's hand rank: ", percentage_rank(board, villain_hand))

print("--------------------")

print("------HSE1------")
print("---Hero---")
hse_1(board, hero_hand)
print("---Villain---")
hse_1(board, villain_hand)
print("--------------------")

hero_rank = evaluator.evaluate(board, hero_hand)
villain_rank = evaluator.evaluate(board, villain_hand)

hero_rank_class = evaluator.get_rank_class(hero_rank)
villain_rank_class = evaluator.get_rank_class(villain_rank)

print("Hero's rank: ", evaluator.class_to_string(hero_rank_class))
print("Villain's rank: ", evaluator.class_to_string(villain_rank_class))

best_hero_hand = evaluator.get_best_hand(board, hero_hand)
best_villain_hand = evaluator.get_best_hand(board, villain_hand)

print("Hero's best hand:")
Card.print_pretty_cards(best_hero_hand)
print("Villain's best hand:")
Card.print_pretty_cards(best_villain_hand)

if hero_rank < villain_rank:
    print("Hero wins!")
elif hero_rank > villain_rank:
    print("Villain wins!")