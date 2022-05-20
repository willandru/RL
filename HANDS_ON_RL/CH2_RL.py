import gym 

env = gym.make("FrozenLake-v1")

env.render()

#SEE THE STATE SPACE
print('STATE SPACE:   ',env.observation_space)

#SEE THE ACTION SPACE
print('ACTION SPACE:   ',env.action_space)

#THE TRANSITION PROBABILITY
#env.P[state][action]
#output : [(transition probability, next state, reward, Is terminal state?)]
#TRANSITION PROBABILITY:    [(0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 0, 0.0, False)]
print('TRANSITION PROBABILITY:   ',env.P[14	][2])


#HOW TO SELECT ACTIONS IN THE ENVIRONMENT?

state= env.reset()
env.render()
env.step(1)
print(env.step(1))

(next_step, reward, done, info)= env.step(1)

#random action
random_action= env.action_space.sample()
next_state, reward, done, info= env.step(random_action)


#GENERATING AN EPISODE
print('Starts iteration')
env.reset()
num_timesteps= 20

for t in range(num_timesteps):
	random_action=env.action_space.sample()
	next_step, reward, done, info= env.step(random_action)
	env.render()
	if done:
		break

#generating a sequence of EPISODES

num_episodes= 10
num_timesteps=20

for i in range(num_episodes):

	state = env.reset()
	print('Time Step 0:')
	env.render()

	for t in range(num_timesteps):
		random_action= env.action_space.sample()
		new_state, reward, done, info= env.step(random_action)
		print('TimeStep {} : ', format(t+1) )

		env.render()
		if done:
			break 
