#!/usr/bin/python3

import board
import neopixel

pixels=neopixel.NeoPixel(board.D18, 256)

for i in range(256):
  pixels[i]=(0,0,0)