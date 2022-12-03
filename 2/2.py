# ROCK = A or X
# PAPER = B or Y
# SCISSORS = C or Z
from enum import Enum


class Opponent(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class MyHands(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class Points(Enum):
    X = 1  # ROCK
    Y = 2  # PAPER
    Z = 3  # SCISSORS


class Scores(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


tie_hands = [
    (Opponent.ROCK.value, MyHands.ROCK.value),
    (Opponent.SCISSORS.value, MyHands.SCISSORS.value),
    (Opponent.PAPER.value, MyHands.PAPER.value),
]
winning_hands = [
    (Opponent.PAPER.value, MyHands.SCISSORS.value),
    (Opponent.ROCK.value, MyHands.PAPER.value),
    (Opponent.SCISSORS.value, MyHands.ROCK.value),
]
losing_hands = [
    (Opponent.SCISSORS.value, MyHands.PAPER.value),
    (Opponent.PAPER.value, MyHands.ROCK.value),
    (Opponent.ROCK.value, MyHands.SCISSORS.value),
]


def get_my_hand(opponent, hand_set):
    return [y for (x, y) in hand_set if x == opponent][0]

def score_round(opponent: str, my_hand: str) -> int:
    """
    The winner of the whole tournament is the player with the highest score.
    Your total score is the sum of your scores for each round. The score for a single round
    is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round
    (0 if you lost, 3 if the round was a draw, and 6 if you won)."""
    if (opponent, my_hand) in tie_hands:
        return Scores.DRAW.value + Points[my_hand].value
    elif (opponent, my_hand) in winning_hands:
        return Scores.WIN.value + Points[my_hand].value
    return Scores.LOSS.value + Points[my_hand].value


# Test_input
print(score_round("A", "Y"))
print(score_round("B", "X"))
print(score_round("C", "Z"))

# Part 1
total = 0
with open("./input.txt") as file:
    for line in file:
        opponent, my_hand = line.rstrip().split()
        total += score_round(opponent, my_hand)

print(f"PART1 TOTAL={total}")

# Part 2
total = 0
with open("./input.txt") as file:
    for line in file:
        opponent, outcome = line.rstrip().split()
        my_hand = None
        # loss
        if outcome == "X":
            my_hand = get_my_hand(opponent, losing_hands)
        elif outcome == "Y":
            my_hand = get_my_hand(opponent, tie_hands)
        else:
            my_hand = get_my_hand(opponent, winning_hands)
        total += score_round(opponent, my_hand)

print(f"PART2 TOTAL={total}")
