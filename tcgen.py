from deuces import Card, Evaluator, Deck
from hse.mc_preflop import preflop_monte_carlo
from hse.hse_1 import hse_1
from hse.hand_potential_1 import HandPotential_1
from hse.hand_potential_2 import HandPotential_2
from percentage_rank import percentage_rank
from hse.odds import mc_odds_calculator
import pandas as pd

deck = Deck()
evaluator = Evaluator()
num_opps = 1

c1 = 'Tc'
c2 = '8s'

c3 = '6s'
c4 = '6d'

# hero_hand = deck.draw(2)
hero_hand = [Card.new(c1), Card.new(c2)]
# villain_hand = deck.draw(2)
villain_hand = [Card.new(c3), Card.new(c4)]


print("Hero's hand:")
Card.print_pretty_cards(hero_hand)

print("Villain's hand:")
Card.print_pretty_cards(villain_hand)
print("--------------------")
print("------Preflop------")
print("---Hero---")
mcp_1  = preflop_monte_carlo(hero_hand, 2)
print("---Villain---")
mcp_2 = preflop_monte_carlo(villain_hand, 2)
print("--------------------")
print("------Odds------")
o_1, o_2 = mc_odds_calculator(hero_hand, villain_hand)
print("--------------------")


# remove hands from deck
for card in hero_hand + villain_hand:
    deck.cards.remove(card)

# board = deck.draw(3)

board = [Card.new('Th'), Card.new('8h'), Card.new('6h')]
for card in board:
    deck.cards.remove(card)

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


# initialize df
df = pd.DataFrame(columns=['Hand', 'Odds', 'MC Preflop', 'HSE', 'HP1', 'HP2', 'EHS'])


# print column names
print(df.columns)
Card.print_pretty_cards(hero_hand)
print(round(o_1,3), "&", round(mcp_1, 3), "&", round(h_1, 3), "&", round(pp_1, 3), "&", round(np_1, 3), "&", round(ehs_1, 3), "& g")
Card.print_pretty_cards(villain_hand)
print(round(o_2,3), "&", round(mcp_2, 3), "&", round(h_2, 3), "&", round(pp_2, 3), "&", round(np_2, 3), "&", round(ehs_2, 3), "& g")