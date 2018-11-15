import sys
import pandas as pd
from models.DDPG import DDPG
from task import Task
import numpy as np
import matplotlib.pyplot as plt

num_episodes = 10000
target_pos = np.array([0., 0., 100.])
task = Task(target_pos=target_pos)
agent = DDPG(task) 
worst_score = 1000000
best_score = -1000000.
reward_log = "reward.txt"

reward_labels = ['episode', 'reward']
reward_results = {x : [] for x in reward_labels}

labels = ['episode', 'reward', 'x', 'y', 'z']
results = {x : [] for x in labels}

for i_episode in range(1, num_episodes+1):
    agent.reset_episode_vars() # start a new episode
    score = 0
    while True:
        action = agent.act(agent.last_state) 
        next_state, reward, done = task.step(action)
        agent.step(action, reward, next_state, done)
        score += reward
        if done:
            results['episode'].append(i_episode)
            results['reward'].append(reward)
            results['x'].append(task.sim.pose[0])
            results['y'].append(task.sim.pose[1])
            results['z'].append(task.sim.pose[2])
            print("Episode = {}, reward = {:7.10f}, x = {}, y = {},  z = {}".format(
                i_episode, 
                score, 
                task.sim.pose[0],
                task.sim.pose[1],
                task.sim.pose[2]))  # [debug]
            break

#plt.plot(results['time'], results['reward'], label='reward')
#plt.legend()
#plt.ylim()
#plt.show()

#plt.plot(results['time'], results['x'], label='x')
#plt.plot(results['time'], results['y'], label='y')
#plt.plot(results['time'], results['z'], label='z')
plt.plot(results['episode'], results['reward'], label='reward')
plt.legend()
plt.ylim()
plt.show()