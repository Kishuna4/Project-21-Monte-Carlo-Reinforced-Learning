import numpy as np
import matplotlib.pyplot as plt
import gym
from IPython.display import lear_output
from time import sleep
import random
import itertools
import collections

env = gym.make('FrozenLake-v0')
epsilon = 0.9
nb_episodes = 100000
max_steps = 100
alpha = .85
gamma = .95

Q = np.zeros((env.observation_space.n, env.action_space.n))

def choose_action(state):
    action = 0
    values = Q[state, :]
    max_values = max(values)
    actions = [a for a in range(len(values))]
    greedy_actions = [a for a in range(len(values)) if values[a] == max_value]
    if (random.random() < epsilon):
                      return random.choice(actions)
    else:
        return random.choice(greedy_actions)

def update(state, state2, reward, action, action2):
    predict = Q[state, action]
    target = reward + gamme * Q[state2, action2]
    Q[state, action] = Q[action, state] + alpha * (target - predict)

def test_policy(policy, env):
    wins = 0
    r = 100

    perf = run_game(env, policy, r)
    if perf > 1:
        wins += 1
    return wins / r

reward = 0

def run_game(env, Q, nb_episodes):
    total_score = 0
    for episode in range(nb_episodes):
        t = 0
        s = env.reset()
        A1 = choose_action(S)
        score = 0
        while t < max_steps:
            

            s2, reward, done, info =env.step(A1)
            A2 = choose_action(s2)

            update(s, s2, reward, A1, A2)

            s = s2
            A1 = A2

            t += 1
            score += reward


            if done:
                if (score > 1):
                    print("Perf: ", score)
                break
    print ("Performace : ", total_Score/nb_episodes/100)
    return total_score

run_game(env, Q, nb_episodes)

print(test_policy(Q, env))

