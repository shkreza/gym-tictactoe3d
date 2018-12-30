from gym.envs.registration import register

register(
  id='tictactoe-v0',
  entry_point='gym_tictactoe.envs:TicTacToeEnv',
)
register(
  id='tictactoe-test-v0',
  entry_point='gym_tictactoe.envs:TicTacToeEnv',
  kwargs={'enforce_rounds': False}
)
