#!/bin/bash

/usr/bin/unclutter -idle 0.1 &
/usr/bin/python3 ./main.py
pkill unclutter
