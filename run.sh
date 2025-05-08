#!/bin/bash
export PYTHONPATH=.
uvicorn app.main:app --reload