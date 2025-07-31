#!/bin/zsh
# Setup Python virtual environment and run audio processing script

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python audio_processor.py
