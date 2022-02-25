
import gym
import pygame
import numpy as np
import matplotlib.pyplot as plt
from gym import wrappers
import time
from tqdm import tnrange, tqdm_notebook
from IPython import display as Idisplay

################################################################################
def get_action(s, w):
    return 1 if s.dot(w) > 0 else 0
################################################################################
# this function plays only one episdoe
def play_one_episode(env, params, render_on=False):
    observation = env.reset() # we reset the environment to go to a start state
    done = False
    t = 0 # length of the episode
    #
    while not done and t < 10000:
        if render_on:
            env.render() # see a video of the episode as it's being played (makes run slow)
        t += 1
        action = get_action(observation, params)
        observation, reward, done, info = env.step(action)
        if done:
            break
    #
    return t
################################################################################
# this function calls the function "play_one_episode" for T times!
# i.e. this function runs T episode of the environment!
def play_multiple_episodes(env, T, params, render_on=False):
    episode_lengths = np.empty(T)
    #
    for i in range(T):
        episode_lengths[i] = play_one_episode(env, params, render_on)
    #
    avg_length = episode_lengths.mean()
    return avg_length # this function returns the average run time for running T episodes
################################################################################
# this function
# We are going to search through 100 random parameter vectors, each are ...
# ... randomly selected from a uniform distribution between minus 1 and 1 in ...
# ... the loop. We call the "play_multiple_episodes_function" with T equals 100 so ...
# ... that we test each parameter vector at 100 times, and we get back the ...
# ... average episode length for the current set of parameters and we ...
# ... append this to our list of episode lengths.
# If this average is better than our best so far we keep these parameters and we ...
# ... update the best average length at the ends. We return all the average episode lengths ...
# ... and the final programs in the main section.
#
# Why Random Search? Because we can use it as a baseline! Assume that a monkey ...
# ... randomly pushes the cart left and right, and see how well it performs. ...
# ... This can help us to establish a baseline.
#
num_random_searches = 30
def random_search(env):
    episode_lengths = []
    best_avg_time = 0
    optimal_params = None
    for t in tnrange(num_random_searches):
        curr_new_params = np.random.random(4)*2 - 1
        curr_avg_length = play_multiple_episodes(env, 100, curr_new_params)
        episode_lengths.append(curr_avg_length)
        #
        if curr_avg_length > best_avg_time:
            optimal_params = curr_new_params
            best_avg_time = curr_avg_length
            print("best length:", best_avg_time)
    return episode_lengths, optimal_params, best_avg_time
################################################################################
env = gym.make('CartPole-v0').env
episode_lengths, optimal_params, best_avg_time = random_search(env)
plt.plot(episode_lengths)
plt.xlabel('Random Wights')
plt.ylabel('Average Survival Time')
plt.savefig('CartPole_RandomSearch.png')
# plt.show()
print("optimal_params = {}".format(optimal_params))
# # play a final set of episodes
# print("***Final run with final weights***")
# play_multiple_episodes(env, 100, optimal_params, render_on=False)
################################################################################
# Let's see a random policy
# env = gym.make('CartPole-v0')
env.close()
env = gym.make('CartPole-v0').env
a_random_coeff = np.random.random(4)*2 - 1
env = wrappers.Monitor(env, 'videos/random_search/a_random_policy', force=True)
print("***Random weights***:", play_one_episode(env, a_random_coeff))
################################################################################
env.close()
env = gym.make('CartPole-v0').env
env = wrappers.Monitor(env, 'videos/random_search/optimal', force=True)
print("***Final run with final weights***:", play_one_episode(env, optimal_params))
################################################################################
H = 5+6

