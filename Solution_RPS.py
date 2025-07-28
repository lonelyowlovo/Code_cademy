from collections import defaultdict
import random

# Inicialização global
transition_counts = defaultdict(lambda: defaultdict(int))
prev_moves = []

def player(prev_opponent_play):
    global prev_moves, transition_counts

    # Atualiza histórico de jogadas
    if prev_opponent_play:
        prev_moves.append(prev_opponent_play)

    # Se tiver pelo menos 3 jogadas, aprende com a transição
    if len(prev_moves) >= 3:
        a, b, c = prev_moves[-3], prev_moves[-2], prev_moves[-1]
        transition_counts[(a, b)][c] += 1

    # Se tiver pelo menos 2 jogadas, tenta prever o próximo movimento
    if len(prev_moves) >= 2:
        a, b = prev_moves[-2], prev_moves[-1]
        next_move_counts = transition_counts[(a, b)]

        if next_move_counts:
            predicted_opponent_move = max(next_move_counts, key=next_move_counts.get)
        else:
            predicted_opponent_move = random.choice(["R", "P", "S"])
    else:
        predicted_opponent_move = random.choice(["R", "P", "S"])

    # Escolhe o counter do movimento previsto
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_opponent_move]
