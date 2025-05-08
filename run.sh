#!/bin/bash

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python3 mocked_data.py

export PYTHONPATH=.
uvicorn app.main:app --reload