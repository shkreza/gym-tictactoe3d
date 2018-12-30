import gym
from gym import error, spaces, utils
from gym.utils import seeding

class TicTacToeEnvKeys:
  KW_ENFORCE_ROUNDS = 'enforce_rounds'

class TicTacToeEnv(gym.Env):
  """
  TicTacToe environment:
    - World: 3 x 3 x 3 matrix
    - Players: 'x' and 'o'
    - Actions: [player] | [block] | [column] | row
  """
  metadata = {'render.modes': ['bcr','compact','full']}
  _EMPTY = '-'
  _X = 'x'
  _O = 'o'
  _PLAYERS = [_X, _O]
  _PLAYERS_COUNT = len(_PLAYERS)
  _DIM_SIZE = 3
  _WORLDSIZE = _DIM_SIZE ** 3
  _MAX_ROUND = 3 * 3 * 3

  def __init__(self, **kwargs):
    self._round = 0
    self._world = [[[self._get_empty(b, c, r) for r in range(TicTacToeEnv._DIM_SIZE)] for c in range(TicTacToeEnv._DIM_SIZE)] for b in range(TicTacToeEnv._DIM_SIZE)]
    self._done = True
    self.enforce_rounds = True
    if kwargs:
      self.enforce_rounds = kwargs[TicTacToeEnvKeys.KW_ENFORCE_ROUNDS] if TicTacToeEnvKeys.KW_ENFORCE_ROUNDS in kwargs else False
  
  def _get_empty(self, b, c, r):
    return TicTacToeEnv._EMPTY

  def step(self, action):
    if len(action) != 4:
      raise ValueError('Bad action')

    player, b, c, r = action[0], int(action[1]), int(action[2]), int(action[3])
    if self._done:
      raise ValueError('Game has ended')
    
    if self.enforce_rounds and player != TicTacToeEnv._PLAYERS[self._round % TicTacToeEnv._PLAYERS_COUNT]:
      raise ValueError('This is not {}\'s turn'.format(player))

    if self._world[b][c][r] != TicTacToeEnv._EMPTY:
      raise ValueError('Cell is used')
    
    self._world[b][c][r] = player
    self._round += 1

    self._done = self._check()

    return None, 1 if self._done else 0, self._done, {'round': self._round, 'next_player': 'NONE' if self._done else TicTacToeEnv._PLAYERS[self._round%TicTacToeEnv._PLAYERS_COUNT]}

  def reset(self):
    self._round = 0
    self._world = [[[self._get_empty(b, c, r) for r in range(TicTacToeEnv._DIM_SIZE)] for c in range(TicTacToeEnv._DIM_SIZE)] for b in range(TicTacToeEnv._DIM_SIZE)]
    self._done = False

  def render(self, mode='compact', close=False):
    for r in range(3):
      for b in range(3):
        for c in range(3):
            print(self._world[b][c][r], end=' ')
        print('   ', end='')
      print()

  def _check_indices(self, index1, index2, index3):
    a = self._world[index1[0]][index1[1]][index1[2]]
    if a not in TicTacToeEnv._PLAYERS:
      return False

    b = self._world[index2[0]][index2[1]][index2[2]]
    if a != b:
      return False

    c = self._world[index3[0]][index3[1]][index3[2]]
    if b != c:
      return False
    
    return True

  def _check(self):
    # Naiive implementation (for now)

    # For each block
    for b in range(3):
      # Check each column
      for c in range(3):
        if self._check_indices((b, c, 0), (b, c, 1), (b, c, 2)):
          return True

      # Check each row
      for r in range(3):
        if self._check_indices((b, 0, r), (b, 1, r), (b, 2, r)):
          return True

      if self._check_indices((b, 0, 0), (b, 1, 1), (b, 2, 2)):
        return True

      if self._check_indices((b, 0, 2), (b, 1, 1), (b, 2, 0)):
        return True

    # For each row
    for r in range(3):
      # Check each column
      for c in range(3):
        if self._check_indices((0, c, r), (1, c, r), (2, c, r)):
          return True

      # Check each block
      for b in range(3):
        if self._check_indices((b, 0, r), (b, 1, r), (b, 2, r)):
          return True

      if self._check_indices((0, 0, r), (1, 1, r), (2, 2, r)):
        return True

      if self._check_indices((2, 0, r), (1, 1, r), (0, 2, r)):
        return True

    # For each column
    for c in range(3):
      # Check each block
      for b in range(3):
        if self._check_indices((b, c, 0), (b, c, 1), (b, c, 2)):
          return True

      # Check each row
      for r in range(3):
        if self._check_indices((0, c, r), (1, c, r), (2, c, r)):
          return True

      if self._check_indices((0, c, 0), (1, c, 1), (2, c, 2)):
        return True

      if self._check_indices((0, c, 2), (1, c, 1), (2, c, 0)):
        return True
    
    # Diagonal 1
    if self._check_indices((0, 0, 0), (1, 1, 1), (2, 2, 2)):
        return True

    # Diagonal 2
    if self._check_indices((0, 2, 0), (1, 1, 1), (2, 0, 2)):
        return True

    # Diagonal 3
    if self._check_indices((0, 0, 2), (1, 1, 1), (2, 2, 0)):
        return True

    # Diagonal 4
    if self._check_indices((0, 2, 2), (1, 1, 1), (2, 0, 0)):
        return True