#!/bin/bash

/home/caroltc/pythonWorks/pyscheduler/stop.sh
nohup python3 /home/caroltc/pythonWorks/pyscheduler/main.py > /home/caroltc/pythonWorks/pyscheduler/app.log 2>&1 &
