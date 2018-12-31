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
  ['1000', '1111', '1222'], # Diagonal
  ['1020', '1111', '1202'], # Diagonal
  ['1002', '1111', '1220'], # Diagonal
  ['1022', '1111', '1200'], # Diagonal
  ['1000', '1011', '1022'], # Diagonal one face
  ['1020', '1011', '1002'], # Diagonal one face
  ['1100', '1111', '1122'], # Diagonal one face
  ['1102', '1111', '1120'], # Diagonal one face
  ['1200', '1211', '1222'], # Diagonal one face
  ['1220', '1211', '1202'], # Diagonal one face
  
  ['1000', '1100', '1200'],
  ['1001', '1101', '1201'],
  ['1002', '1102', '1202'],
  ['1010', '1110', '1210'],
  ['1011', '1111', '1211'],
  ['1012', '1112', '1212'],
  ['1020', '1120', '1220'],
  ['1021', '1121', '1221'],
  ['1022', '1122', '1222'],

  ['1000', '1001', '1002'],
  ['1010', '1011', '1012'],
  ['1110', '1111', '1112'],
  ['1020', '1021', '1022'],
  ['1120', '1121', '1122'],
  ['1220', '1221', '1222'],
  
  ['1000', '1010', '1020'],
  ['1001', '1011', '1021'],
  ['1002', '1012', '1022'],
  ['1100', '1110', '1120'],
  ['1101', '1111', '1121'],
  ['1102', '1112', '1122'],
  ['1200', '1210', '1220'],
  ['1201', '1211', '1221'],
  ['1202', '1212', '1222'],
]

game_actions_enforce_rounds = [
  ['1021', '2111', '1221', '2222', '1121']
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
