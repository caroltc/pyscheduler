#!/bin/bash

kill -9 $(ps -ef | grep 'pyscheduler/main.py' | grep python3 | awk '{print $2}')
