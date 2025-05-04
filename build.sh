#!/bin/bash
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r ./stretch_reminder_gui/requirements.txt
pyinstaller --onefile ./stretch_reminder_gui/widget.py
