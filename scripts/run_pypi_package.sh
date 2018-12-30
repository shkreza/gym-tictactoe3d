#! /usr/bin/env python3

import gym
import gym_tictactoe

def play_game(actions, step_fn=None, enforce_rounds=True):
  if enforce_rounds:
    env = gym.make('tictactoe-v0')
  else:
    env = gym.make('tictactoe-test-v0')
  env.reset()
  env.render()
  
  total_reward = 0
  for action in actions:
    _, reward, done, info = env.step(action)
    print(info)
    total_reward += reward
    env.render()
    if step_fn:
      step_fn()

  return total_reward, done

game_actions_ignore_rounds = [
  ['x000', 'x111', 'x222'], # Diagonal
  ['x020', 'x111', 'x202'], # Diagonal
  ['x002', 'x111', 'x220'], # Diagonal
  ['x022', 'x111', 'x200'], # Diagonal
  ['x000', 'x011', 'x022'], # Diagonal one face
  ['x020', 'x011', 'x002'], # Diagonal one face
  ['x100', 'x111', 'x122'], # Diagonal one face
  ['x102', 'x111', 'x120'], # Diagonal one face
  ['x200', 'x211', 'x222'], # Diagonal one face
  ['x220', 'x211', 'x202'], # Diagonal one face
  
  ['x000', 'x100', 'x200'],
  ['x001', 'x101', 'x201'],
  ['x002', 'x102', 'x202'],
  ['x010', 'x110', 'x210'],
  ['x011', 'x111', 'x211'],
  ['x012', 'x112', 'x212'],
  ['x020', 'x120', 'x220'],
  ['x021', 'x121', 'x221'],
  ['x022', 'x122', 'x222'],

  ['x000', 'x001', 'x002'],
  ['x010', 'x011', 'x012'],
  ['x110', 'x111', 'x112'],
  ['x020', 'x021', 'x022'],
  ['x120', 'x121', 'x122'],
  ['x220', 'x221', 'x222'],
  
  ['x000', 'x010', 'x020'],
  ['x001', 'x011', 'x021'],
  ['x002', 'x012', 'x022'],
  ['x100', 'x110', 'x120'],
  ['x101', 'x111', 'x121'],
  ['x102', 'x112', 'x122'],
  ['x200', 'x210', 'x220'],
  ['x201', 'x211', 'x221'],
  ['x202', 'x212', 'x222'],
]

game_actions_enforce_rounds = [
  ['x021', 'o111', 'x221', 'o222', 'x121']
]

dup_detector = set()

for actions in game_actions_ignore_rounds:
  print('*'*10, 'New game:', actions)
  new_action = str(sorted(actions))
  if new_action in dup_detector:
    raise ValueError('Duplicate action:', actions)
  dup_detector.add(new_action)
  total_reward, done = play_game(actions, enforce_rounds=False)
  assert done == True

print('Checked {} combinations'.format(len(dup_detector)))

for actions in game_actions_enforce_rounds:
  print('*'*10, 'New game')
  total_reward, done = play_game(actions)
  assert done == True
