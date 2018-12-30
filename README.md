# TiC Tac Toe Game in OpenAI Gym
The 3D version of Tic Tac Toe

## Install
To install run:
```console
# In your virtual environment
pip install gym-tictactoe
```

## Use
To use:
```python
import gym
import gym_tictactoe

def play_game(actions, step_fn=input):
  env = gym.make('tictactoe-v0')
  env.reset()

  # Play actions in action profile
  for action in actions:
    print(env.step(action))
    env.render()
    if step_fn:
      step_fn()

actions = ['x021', 'o111', 'x221', 'o222', 'x121']
play_game(actions)
print('Done')

```