#!/usr/bin/python3

import board
import neopixel
import math
import time
import copy

pixels=neopixel.NeoPixel(board.D18, 256, auto_write=False)
# key =row, value=col lights on
alien0={
0:[1,2,3], 
1:[3,4],
2:[1,2,3,4,5,7],
3:[0,2,3,5,6],
4:[0,2,3,4,5],
5:[2,3,4,5],
6:[0,2,3,4,5],
7:[0,2,3,5,6],
8:[1,2,3,4,5,7],
9:[3,4],
10:[1,2,3],
}
alien1={
  0:[3,4,5,6],
  1:[0,2,3,4],
  2:[1,2,3,4,5,7],
  3:[2,3,5,6],
  4:[2,3,4,5],
  5:[2,3,4,5],
  6:[2,3,4,5],
  7:[2,3,5,6],
  8:[1,2,3,4,5,7],
  9:[0,2,3,4],
  10:[3,4,5,6]
}
# which alien should be an alien dictionary, start is the row number, partRows is for making only part of alien
def makeAlien(whichAlien, start, partRows=0):
  alienWidth=len(whichAlien)
  # i is an individual light
  startI=(start)*8
  i=copy.deepcopy(startI)
  if partRows>0:
    endI=startI+partRows*8
  else:
    endI=startI+alienWidth*8
  while i<256 and i<endI:
      # lights numbers go up one column then down the next
      rem=i%16
      # col=0 to 8
      col=(7-rem if rem <8 else rem-8)
      # print("col:", col)
      # row=0 to 31
      row=math.floor(i/8-start)
      # print("row:", row)
      if partRows>0:
        row=row+alienWidth-partRows

      thisRow=whichAlien[row]
      if col in thisRow:
        pixels[i]=rainbow(col)
      else:
        pixels[i]=(0,0,0)
      i+=1


def blankRow(startRow):
  # only 32 rows total
  if startRow <32:
    # multiply row by 8 to get light number
    for i in range(startRow*8, (startRow*8)+8):
      pixels[i] = (0,0,0) 

def moveAliens():
  print("moveAliens")
  for i in range(12):

      if i%2==0:
        if i>1:
          makeAlien(alien1,0,i-1)
        if i>0:
          blankRow(i-1)
          makeAlien(alien0, i)
          blankRow(i+11)
          makeAlien(alien1,i+12)
          blankRow(i+23)
          makeAlien(alien0, i+24)
          pixels.show()
      else:
        if i>1:
          makeAlien(alien0,0,i-1)
        if i>0:
          blankRow(i-1)
          makeAlien(alien1, i)
          blankRow(i+11)
          makeAlien(alien0,i+12)
          blankRow(i+23)
          makeAlien(alien1, i+24)
          pixels.show()

      time.sleep(1)



# To Make a RAINBOW
rainbowDict={
  0:(255,105,180),
  1: (255,0,0),
  2: (255,142,0,),
  3: (255,255,0),
  4: (0,142,0),
  5: (0,192,192),
  6: (64,0,152),
  7: (142,0,142)}

# makes colors less bright by dividing value by div
def divTuple(rgb, div):
  return(rgb[0]/div,rgb[1]/div,rgb[2]/div, )

def rainbow(col):
  return divTuple(rainbowDict[col], 12)


# makeAlien(alien0,0,5)

moveAliens()

# moveAliens()
# print("Alien0")
# makeAlien(alien0, 0)
# print("Alien1")
# makeAlien(alien1, 12)
# makeAlien(alien1, 24)
# makeAlien(alien0,12)