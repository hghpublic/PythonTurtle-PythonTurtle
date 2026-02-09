#!/usr/bin/env python3
# https://docs.python.org/3/library/turtle.html
from turtle import *

color("red")
fillcolor("yellow")

begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
