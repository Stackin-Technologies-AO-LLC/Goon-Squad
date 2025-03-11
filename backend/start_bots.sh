#!/bin/bash

# Activate environment
source venv/bin/activate  # Use `venv\Scripts\activate` on Windows

# Start bots based on input
if [ "$1" == "2" ]; then
    python bot1.py &
    python bot2.py &
elif [ "$1" == "3" ]; then
    python bot1.py &
    python bot2.py &
    python bot3.py &
elif [ "$1" == "5" ]; then
    python bot1.py &
    python bot2.py &
    python bot3.py &
    python bot4.py &
    python bot5.py &
else
    echo "Usage: ./start_bots.sh [2|3|5]"
fi

