import numpy as np
import gym
import random

# using the FrozenLake environment to test out Q learning algorithm
env = gym.make("FrozenLake-v0")


# return the amount of actions available
actions = env.action_space.n
# return the amount of states the agent can be in
states = env.observation_space.n

# initialize the Qmatrix with zeros
q_table = np.zeros((states,actions))
#print(q_table)

# number of episodes in total
episodes= 10000

# the max amount of moves the agent can make per episode
max_steps_episodes = 100

learning_rate = 0.1
discount_rate = 0.99

# setting the explore rates for the agent to randomly go through the enviroment to gain knowledge and start
# updating the Q matrix
explore_rate = 1
max_explore_rate = 10
min_explore_rate = 0.005
change_in_explore = 0.005

# create empty rewards array
rewards_all = []

for episode in range(episodes):
    state = env.reset()
    done = False
    rewards_curr = 0
    
    for step in range(max_steps_episodes):
        explore_threshold = random.uniform(0,1)
        if explore_threshold > explore_rate:
            action = np.argmax(q_table[state,:])
        else:
            action = env.action_space.sample()
            
        new_state, reward, done, info = env.step(action)
        #env.render()

        # Q learning formula implemented with code
        q_table[state, action] = q_table[state, action] * (1- learning_rate) + learning_rate * (reward+discount_rate * np.max(q_table[new_state, :]))
        
        state = new_state
        rewards_curr += reward
        
        if done == True:
            break
    explore_rate = min_explore_rate + (max_explore_rate - min_explore_rate) * np.exp(-change_in_explore*episode)
    
    rewards_all.append(rewards_curr)
    
rewards_avg = np.split(np.array(rewards_all),episodes/1000)
count=1000
# showcase the avg amount of successful episodes per 1000 episodes

for r in rewards_avg:
    # prints the percentage value of how many episodes were successful to the console
    print(count,":",str(sum(r/1000)*100))
    count += 1000
