import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from gym_tictactoe.envs.tictactoe_env import TicTacToeEnv

class TicTacToePltEnv(TicTacToeEnv):
  _MARKERS = ['', 'x', 'o']
  _COLORS = ['', 'g', 'b']
  _MARKER_SIZE = 100
  _PLOT_RANGE = [0, 1, 2]
  _GRID = [[[(i,j,k) for i in range(3)] for j in range(3)] for k in range(3)]
  _GRID = np.array(_GRID).flatten()

  _FONT_SIZE = 7
  _Z_GRID = np.array(_GRID).flatten()[2::3]
  _Y_GRID = np.array(_GRID).flatten()[1::3]
  _X_GRID = np.array(_GRID).flatten()[0::3]

  def __init__(self, show_axes=True, **kwargs):
    super().__init__(**kwargs)

    self._show_axes = show_axes
    self._close_previous_figure_before_render = True
    self._fig = None
    self._ax = None
  
  def _render_player(self, ax, np_obs, player):
    marker = TicTacToePltEnv._MARKERS[player]
    
    xs = []
    ys = []
    zs = []
    for ijk, v in np.ndenumerate(np_obs==player):
      if v:
        xs.append(ijk[0])
        ys.append(ijk[1])
        zs.append(ijk[2])
    
    ax.scatter(xs,
                ys,
                zs,
                c=TicTacToePltEnv._COLORS[player],
                marker=TicTacToePltEnv._MARKERS[player],
                s=TicTacToePltEnv._MARKER_SIZE)
    
    ax.scatter(TicTacToePltEnv._X_GRID, TicTacToePltEnv._Y_GRID, TicTacToePltEnv._Z_GRID, c='b', marker='+', s=1)
    for xyz in zip(TicTacToePltEnv._X_GRID, TicTacToePltEnv._Y_GRID, TicTacToePltEnv._Z_GRID):
      ax.text(xyz[0], xyz[1], xyz[2], '  {}{}{}'.format(xyz[0], xyz[1], xyz[2]), size=TicTacToePltEnv._FONT_SIZE)


  def _prepare_fig(self):
    # Reclaim previous memory
    if self._close_previous_figure_before_render:
      plt.close()
      self._fig = None
    
    if not self._fig:
      self._fig = plt.figure()
      self._ax = self._fig.add_subplot(111, projection='3d')
    self._ax.view_init(azim=125, elev=20)
    if not self._show_axes:
      self._ax.set_axis_off()

    self._ax.set_xlim(min(TicTacToePltEnv._PLOT_RANGE), max(TicTacToePltEnv._PLOT_RANGE))
    self._ax.set_xticks(TicTacToePltEnv._PLOT_RANGE)

    self._ax.set_ylim(min(TicTacToePltEnv._PLOT_RANGE), max(TicTacToePltEnv._PLOT_RANGE))
    self._ax.set_yticks(TicTacToePltEnv._PLOT_RANGE)

    self._ax.set_zlim(min(TicTacToePltEnv._PLOT_RANGE), max(TicTacToePltEnv._PLOT_RANGE))
    self._ax.set_zticks(TicTacToePltEnv._PLOT_RANGE)
    for t in self._ax.zaxis.get_major_ticks(): t.label.set_fontsize(10)
    
    return self._ax
  
  def _display_fig(self):
    plt.show(block=False)
    
  def render(self):
    ax = self._prepare_fig()
    np_obs = np.array(self._world)

    # Draw X's
    self._render_player(ax, np_obs, 1)

    # Draw O's
    self._render_player(ax, np_obs, 2)

    # Display
    self._display_fig()