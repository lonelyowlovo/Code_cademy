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



#import tensorflow_probability as tfp
#import tensorflow as tf
#import numpy as np
#
#tfd = tfp.distributions
#
## Mapping between moves and numbers
#move_to_index = {'R': 0, 'P': 1, 'S': 2}
#index_to_move = ['R', 'P', 'S']
#beats = {'R': 'P', 'P': 'S', 'S': 'R'}
#
## Initialize with uniform transition matrix
#transition_counts = np.ones((3, 3))  # Start with 1s for Laplace smoothing
#
#def player(prev_play, opponent_history=[]):
#    # Add new play to history
#    if prev_play:
#        opponent_history.append(prev_play)
#
#    # If not enough data, just return a random safe choice
#    if len(opponent_history) < 2:
#        return 'R'
#
#    # Update transition counts based on last 2 moves
#    last = move_to_index[opponent_history[-2]]
#    current = move_to_index[opponent_history[-1]]
#    transition_counts[last][current] += 1
#
#    # Create transition probabilities from counts
#    transition_probs = transition_counts / transition_counts.sum(axis=1, keepdims=True)
#
#    # Estimate initial state probabilities from observed frequencies
#    init_counts = np.array([
#        opponent_history.count('R'),
#        opponent_history.count('P'),
#        opponent_history.count('S')
#    ], dtype=np.float32)
#
#    initial_probs = init_counts / init_counts.sum()
#
#    # Observation distribution is dummy (not used for prediction)
#    observation_distribution = tfd.Categorical(probs=[[1/3, 1/3, 1/3]] * 3)  # dummy but required
#
#    # Create Hidden Markov Model
#    hmm = tfd.HiddenMarkovModel(
#        initial_distribution=tfd.Categorical(probs=initial_probs),
#        transition_distribution=tfd.Categorical(probs=transition_probs),
#        observation_distribution=observation_distribution,
#        num_steps=1
#    )
#
#    # Predict the expected next move as a number between 0 and 2
#    predicted_numeric = round(hmm.mean().numpy()[0])  # Mean returns float, round to get index
#    predicted_move = index_to_move[predicted_numeric]
#
#    # Return the move that beats the predicted move
#    guess=beats[predicted_move]
#    return guess
#