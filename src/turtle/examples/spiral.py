#!/usr/bin/env python3
# https://docs.python.org/3/library/turtle.html
from turtle import *

for steps in range(100):
    for c in ("blue", "red", "green"):
        color(c)
        forward(steps)
        right(30)
