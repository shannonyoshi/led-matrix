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

alien2={
  0:[1,3,4],
  1:[0,2,3,4,5],
  2:[3,5,6],
  3:[2,3,4,5,6,7],
  4:[2,3,4,5,6,7],
  5:[3,5,6],
  6:[0,2,3,4,5],
  7:[1,3,4]
}

alien3={
  0:[0,3,4],
  1:[1,3,4],
  2:[0,2,3,5,6],
  3:[1,3,4,5,6,7],
  4:[1,3,4,5,6,7],
  5:[0,2,3,5,6],
  6:[1,3,4],
  7:[0,3,4]
}

alien4={
 0:[0,3,4],
 1:[0,3,4,5,6],
 2:[1,3,4,5,6],
 3:[1,2,3,5,6],
 4:[2,3,5,6,7],
 5:[1,3,4,5,6,7],
 6:[1,3,4,5,6,7],
 7:[2,3,5,6,7],
 8:[1,2,3,5,6],
 9:[1,3,4,5,6],
 10:[0,3,4,5,6],
 11:[0,3,4],
}

alien5={
  0:[3,4,5],
  1:[1,3,4,5,6],
  2:[0,1,2,3,4,5,6],
  3:[0,2,3,5,6],
  4:[2,3,5,6,7],
  5:[1,3,4,5,6,7],
  6:[1,3,4,5,6,7],
  7:[2,3,5,6,7],
  8:[0,2,3,5,6],
  9:[0,1,2,3,4,5,6],
  10:[1,3,4,5,6],
  11:[3,4,5],
}

# which alien should be an alien dictionary, partRows is for making only part of alien
def makeAlien(whichAlien, startRow, partRows=0):
  alienWidth=len(whichAlien)
  if startRow<32:
    loopCount = alienWidth if partRows<=0 else partRows
    for i in range(loopCount):
      x=startRow+i
      rowLights=whichAlien[alienWidth-loopCount+i]
      for j in range(8):
        if j in rowLights:
          writePix([x, j], (1,1,1))
        else:
          writePix([x,j], (0,0,0))

# coords=[x=row,y=column], color=(r,g,b)
def writePix(coords, color):
    pixel = coords[0]*8
    if coords[0]%2==0:
      pixel+=coords[1]
    else:
      pixel+=7-coords[1]
    if pixel>=0 and pixel <256:
      pixels[pixel]=color

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
          
        makeAlien(alien3, i)
        blankRow(i+len(alien3))
        makeAlien(alien5,i+len(alien3)+1)
        blankRow(i+len(alien5)+len(alien3))
        makeAlien(alien1, i+len(alien5)+len(alien3)+2)
        pixels.show()
      else:
        if i>1:
          makeAlien(alien0,0,i-1)
        if i>0:
          blankRow(i-1)
        makeAlien(alien2, i)
        blankRow(i+len(alien2))
        makeAlien(alien4,i+len(alien2)+1)
        blankRow(i+len(alien4)+len(alien2))
        makeAlien(alien0, i+len(alien4)+len(alien2)+2)
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

# takes y coordinate
def rainbow(y):
  return divTuple(rainbowDict[y], 12)


moveAliens()
