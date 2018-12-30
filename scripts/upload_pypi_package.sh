#!/bin/bash

# Get most recent wheel
recent_whl=$(ls -t dist/gym_tictactoe-0.*-py3-none-any.whl | head -n 1)

# Upload most recent wheel
python -m twine upload ${recent_whl}