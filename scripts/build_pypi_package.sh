#! /bin/bash

python3 setup.py bdist_wheel

# Get most recent wheel
recent_whl=$(ls -t dist/gym_tictactoe-0.*-py3-none-any.whl | head -n 1)

# Install most recent wheel
pip3 install ${recent_whl}