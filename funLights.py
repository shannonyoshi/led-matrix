#!/usr/bin/python3

import board
import neopixel

pixels=neopixel.NeoPixel(board.D18, 256)

# all rows
rainbowDict={0:(255,105,180),
1: (255,0,0),
2: (255,142,0,),
3: (255,255,0),
4: (0,142,0),
5: (0,192,192),
6: (64,0,152),
7: (142,0,142)}

def divTuple(rgb, div):
  return(rgb[0]/div,rgb[1]/div,rgb[2]/div, )

for i in range(256):
     r=i%16
     col=(7-r if r <8 else r-8)
     pixels[i]=divTuple(rainbowDict[col], 8)

