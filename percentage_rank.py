from deuces import Evaluator, Card

evaluator = Evaluator()

def percentage_rank(board, hand):
    rank = evaluator.evaluate(board, hand)
    percentage = 1.0 - evaluator.get_five_card_rank_percentage(rank)
    return percentage

if __name__ == "__main__":
    board = [Card.new('4h'), Card.new('3c'), Card.new('2h')]
    hand = [Card.new('7d'), Card.new('5c')]

    hand2 = [Card.new('7d'), Card.new('5d')]
    board2 = [Card.new('4d'), Card.new('3d'), Card.new('2d')]

    print(percentage_rank(board2, hand2))