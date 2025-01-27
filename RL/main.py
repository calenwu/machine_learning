import time
import gym
import numpy as np
from agent import Agent
import matplotlib.pyplot as plt


def plot_learning_curve(x, scores, figure_file):
	running_avg = np.zeros(len(scores))
	for i in range(len(running_avg)):
		running_avg[i] = np.mean(scores[max(0, i-100):(i+1)])
	plt.plot(x, running_avg)
	plt.title('Running average of previous 100 scores')
	plt.savefig(figure_file)


if __name__ == '__main__':
	env = gym.make('CartPole-v0')
	N = 20
	batch_size = 16
	n_epochs = 4
	alpha = 0.0003
	agent = Agent(n_actions=env.action_space.n, input_dims=env.observation_space.shape, alpha=alpha, gamma=0.99,
				  n_epochs=n_epochs, batch_size=batch_size)
	n_games = 1000
	agent.load_models()
	figure_file = 'plots/cartpole.png'
	best_score = env.reward_range[0]
	score_history = []

	learn_iters = 0
	avg_score = 0
	n_steps = 0

	# for i in range(n_games):
	# 	done = False
	# 	observation = env.reset()
	# 	score = 0
	# 	while not done:
	# 		action, prob, val = agent.choose_action(observation)
	# 		observation_, reward, done, info = env.step(action)
	# 		n_steps += 1
	# 		score += reward
	# 		agent.remember(observation, action, prob, val, reward, done)
	# 		if n_steps % N == 0:
	# 			agent.learn()
	# 			learn_iters += 1
	# 		observation = observation_
	# 	score_history.append(score)
	# 	avg_score = np.mean(score_history[-100:])
	# 	if avg_score > best_score:
	# 		best_score = avg_score
	# 		agent.save_models()
	# 	print('episode', i, 'score %.1f' % score, 'avg score %.1f' % avg_score,
	# 		  'time_steps', n_steps, 'learning_steps', learn_iters)
	# x = [i + 1 for i in range(len(score_history))]
	# plot_learning_curve(x, score_history, figure_file)


	observation = env.reset()
	done = False
	while not done:
		action, prob, val = agent.choose_action(observation)
		observation_, reward, done, info = env.step(action)
		env.render()
		time.sleep(0.01)
		observation = observation_