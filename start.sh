#!/bin/bash

# Define the commands to run in the panes
start_frontend="cd frontend; nvm use 19; npm run dev"
start_backend="source .env/bin/activate; cd backend; ./manage.py runserver"

# Check if already in a tmux session
if [ -n "$TMUX" ]; then
    # Split the current window vertically
    tmux split-window -v

    # Run the 'first' command in the upper pane
    tmux select-pane -t 1
    tmux send-keys "$start_frontend" C-m

    # Run the 'bottom' command in the lower pane
    tmux select-pane -t 2
    tmux send-keys "$start_backend" C-m
else
    # Create a new tmux session and perform the same split and command execution as before
    tmux new-session -d -s mysession

    tmux split-window -v
    tmux select-pane -t 1
    tmux send-keys "$start_frontend" C-m

    tmux select-pane -t 2
    tmux send-keys "$start_backend" C-m
    tmux attach-session -t mysession
fi

