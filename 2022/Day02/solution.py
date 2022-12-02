#!/usr/bin/env python3

convert = {
    "A": "Rock",
    "X": "Rock",
    "B": "Paper",
    "Y": "Paper",
    "C": "Scissors",
    "Z": "Scissors",
}

win_states = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

win_against = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}
lose_to = {y: x for x, y in win_against.items()}


def determine_winner(a, b):
    # A wins
    if win_against[a] == b:
        return 1
    # A loses
    elif lose_to[a] == b:
        return -1
    # They tie
    else:
        return 0


with open("input.txt") as f:
    plays = f.read().splitlines()

# Part 1
their_score = our_score = 0
for play in plays:
    their_move, our_move = map(convert.get, play.split())

    win_state = determine_winner(their_move, our_move)
    if win_state == 1:
        # Opponent win
        their_score += 6
    elif win_state == -1:
        # We win
        our_score += 6
    else:
        # Tie
        their_score += 3
        our_score += 3

    their_score += (
        1 if their_move == "Rock"
        else 2 if their_move == "Paper"
        else 3
    )
    our_score += (
        1 if our_move == "Rock"
        else 2 if our_move == "Paper"
        else 3
    )

print(their_score, our_score)


# Part 2
our_score = their_score = 0
for play in plays:
    their_move, win_state = play.split()

    their_move = convert[their_move]
    win_state = win_states[win_state]

    if win_state == "Lose":
        # We lose
        our_move = win_against[their_move]
        their_score += 6
    elif win_state == "Draw":
        # We draw
        our_move = their_move
        their_score += 3
        our_score += 3
    else:
        # We win
        our_move = lose_to[their_move]
        our_score += 6

    their_score += (
        1 if their_move == "Rock"
        else 2 if their_move == "Paper"
        else 3
    )
    our_score += (
        1 if our_move == "Rock"
        else 2 if our_move == "Paper"
        else 3
    )

print(their_score, our_score)
