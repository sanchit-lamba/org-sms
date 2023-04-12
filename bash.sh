#!/bin/bash
emacs -load test.el -kill
python3 twilio-api.py
