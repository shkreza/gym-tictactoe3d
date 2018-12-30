#! /usr/bin/env python3

import gym
import gym_tictactoe

def play_game(actions, step_fn=input):
  env = gym.make('tictactoe-v0')
  env.reset()

  for action in actions:
    print(env.step(action))
    env.render()
    if step_fn:
      step_fn()


actions = ['x021', 'o111', 'x221', 'o222', 'x121']
play_game(actions)
print('Done')


actions = ['x021', 'o111', 'x221', 'o222', 'x121']
play_game(actions)
print('Done')