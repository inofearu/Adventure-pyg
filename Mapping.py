import time
import pygame
import random
import Update
pygame.init()
MapX,MapY=0,0
j = 0
counter = 0
amountofsquaresperchunk = 4
#please put in the square root of the amount of squares you want
biomes = []
RarityForest = 100
for i in range(0,RarityForest):
  biomes.append('Forest')
RarityDesert = 50
for i in range(0,RarityDesert):
  biomes.append('Desert')
RaritySwamp = 25
for i in range(0,RaritySwamp):
  biomes.append('Swamp')
RarityOcean = 15
for i in range(0,RarityOcean):
  biomes.append('Ocean')
RarityCorrupt = 6
for i in range(0,RarityCorrupt):
  biomes.append('Corrupt')
  RarityTundra = 10
for i in range(0,RarityTundra):
  biomes.append("Tundra")    
m = 0
i = 0
class Chunk:
  def __init__(self,Square,Chunk,Column,Row,mapX,mapY):
    self.Row = Row
    self.Biome = ''
    self.Column = Column
    self.XStartPoint = Column*8
    self.YStartPoint = Row*8
    self.Chunk = ''
    self.SquareValue = Square
    self.IsCorner = False
    self.Biome = ''
    amountofchunks = ((mapX//8)*(mapX//8))//4
    global i
    for i in range(0,amountofchunks):
      global m
      m += 1
      e = i*8
      f = i*8+8
      if self.XStartPoint >= e and self.XStartPoint <= f:
       if self.YStartPoint >= e and self.YStartPoint <= f:
         self.Chunk = m
         i = 7
      i += 1
    if self.Chunk in ['']:
      self.Chunk = 'Error'
    i = 0
    m = 0
  def BiomeColors(self):
    if self.Biome in ['Forest']:
      self.Fill = (0,200,0)
      Update.DrawBorder((0,0,0),self.Fill, getattr(globals()[f"Chunk{j}"],'XStartPoint')*4+20,getattr(globals()[f"Chunk{j}"],'YStartPoint')*4+20,8*4,8*4,2,'R')
    if self.Biome in ['Desert']:
      self.Fill = (220,230,50)
      Update.DrawBorder((0,0,0),self.Fill, getattr(globals()[f"Chunk{j}"],'XStartPoint')*4+20,getattr(globals()[f"Chunk{j}"],'YStartPoint')*4+20,8*4,8*4,2,'R')
    if self.Biome in ['Swamp']:
      self.Fill = (0,100,0)
      Update.DrawBorder((0,0,0),self.Fill, getattr(globals()[f"Chunk{j}"],'XStartPoint')*4+20,getattr(globals()[f"Chunk{j}"],'YStartPoint')*4+20,8*4,8*4,2,'R')
    if self.Biome in ['Ocean']:
      self.Fill = (0,0,150)
      Update.DrawBorder((0,0,0),self.Fill, getattr(globals()[f"Chunk{j}"],'XStartPoint')*4+20,getattr(globals()[f"Chunk{j}"],'YStartPoint')*4+20,8*4,8*4,2,'R')
    if self.Biome in ['Corrupt']:
      self.Fill = (75,0,130)
      Update.DrawBorder((0,0,0),self.Fill, getattr(globals()[f"Chunk{j}"],'XStartPoint')*4+20,getattr(globals()[f"Chunk{j}"],'YStartPoint')*4+20,8*4,8*4,2,'R')
    if self.Biome in ['Tundra']:
      self.Fill = (165,242,243)
      Update.DrawBorder((0,0,0),self.Fill, getattr(globals()[f"Chunk{j}"],'XStartPoint')*4+20,getattr(globals()[f"Chunk{j}"],'YStartPoint')*4+20,8*4,8*4,2,'R') 
        
  def AssignBiome(self):
    BiomeNum = random.randint(0,len(biomes)-1)
    self.Biome = biomes[BiomeNum]
    self.BiomeColors()
class Square:
  def __init__(self,Square,Chunk,Column,Row,mapX,mapY):
    self.Row = Row
    self.Biome = ''
    self.Column = Column
    self.XStartPoint = Column*8
    self.YStartPoint = Row*8
    self.Chunk = ''
    self.SquareValue = Square
    self.IsCorner = False
    self.Biome = ''
def Biomes(MapX,MapY):
  global screen
  screen = pygame.display.set_mode((MapX*2+40, MapY*2+40))
  pygame.display.set_caption('Adventure Game')
  global background
  background = (255,255,255)
  screen.fill(background)
  pygame.display.flip()
  for i in range(0,MapY//(4*4)):
   for l in range(0,MapX//(4*4)):
     global j
     global counter
     j += 1
     globals()[f"Chunk{j}"] = Chunk(j,'Forest',l,i,MapX,MapY)
     '''
     print(f"Chunk{j}")
     print(getattr(globals()[f"Chunk{j}"],'XStartPoint'),getattr(globals()[f"Chunk{j}"],'YStartPoint'))
     '''
     CurrentChunkA = globals()[f"Chunk{j}"]
     CurrentChunkA.AssignBiome()
     Update.DrawBorder((0,0,0),(CurrentChunkA.Fill), getattr(globals()[f"Chunk{j}"],'XStartPoint')*4+20,getattr(globals()[f"Chunk{j}"],'YStartPoint')*4+20,8*4,8*4,6,'R')
     counter+=1
     time.sleep(.009)
def ChooseMapSize():
 MapSize = str(input('How big do you want the map to be?\n1.Large\n2.Normal\n3.Small\n> '))
 if MapSize in ['1','2','3']:
   global g
   global h
   if MapSize in ['1']:
     MapX,MapY = 8*16,8*16
     Biomes(MapX,MapY)
   elif MapSize in ['2']:
     MapX,MapY = 8*12,8*12
     Biomes(MapX,MapY)
   else:
     MapX,MapY = 8*8,8*8
     Biomes(MapX,MapY)
   g = MapX
   h = MapY
 else:
   print('\nPlease choose a value between 1 and 3\n')
   ChooseMapSize()
 j = 0
 screen.fill((255,255,255))
 '''
 for li in range(1,3):
    for il in range(1,3):
      j=0
      for i in range(0,g//(4*4)):
        for l in range(0,h//(4*4)):
          j += 1
          CurrentChunk = globals()[f"Chunk{j}"]
          m = round(16/amountofsquaresperchunk)
          Update.DrawBorder((0,0,0),(0,0,0),CurrentChunk.XStartPoint*4+16*li+4,CurrentChunk.YStartPoint*4+16*il+4,m*amountofsquaresperchunk,m*amountofsquaresperchunk,2,'R')
 '''
 for li in range(1,3):
    for il in range(1,3):
      j=0
      for i in range(0,g//(4*4)):
        for l in range(0,h//(4*4)):
          j += 1
          CurrentChunk = globals()[f"Chunk{j}"]
          m = round(16/amountofsquaresperchunk)
          Update.DrawBorder((0,0,0),(CurrentChunk.Fill),CurrentChunk.XStartPoint*4+16*li+4,CurrentChunk.YStartPoint*4+16*il+4,m*amountofsquaresperchunk,m*amountofsquaresperchunk,1.5,'R')
          time.sleep(0.00125)
 for li in range(1,3):
    for il in range(1,3):
      j=0
      for i in range(0,g//(4*4)):
        for l in range(0,h//(4*4)):
          j += 1
          CurrentChunk = globals()[f"Chunk{j}"]
          m = round(16/amountofsquaresperchunk)
          Update.DrawBorder((0,0,0),(CurrentChunk.Fill),CurrentChunk.XStartPoint*4+16*li+4,CurrentChunk.YStartPoint*4+16*il+4,m*amountofsquaresperchunk,m*amountofsquaresperchunk,1,'R')
          time.sleep(.005)
 for i in range(1,counter+1):
   CurrentChunk = globals()[f"Chunk{i}"]
   pygame.draw.line(screen,(0,0,0),(CurrentChunk.XStartPoint*4+20,CurrentChunk.YStartPoint*4+20),(CurrentChunk.XStartPoint*4+50,CurrentChunk.YStartPoint*4+20),1)
   pygame.draw.line(screen,(0,0,0),(CurrentChunk.XStartPoint*4+20,CurrentChunk.YStartPoint*4+50),(CurrentChunk.XStartPoint*4+50,CurrentChunk.YStartPoint*4+50),1)
   pygame.draw.line(screen,(0,0,0),(CurrentChunk.XStartPoint*4+20,CurrentChunk.YStartPoint*4+20),(CurrentChunk.XStartPoint*4+20,CurrentChunk.YStartPoint*4+50),1)
   pygame.draw.line(screen,(0,0,0),(CurrentChunk.XStartPoint*4+50,CurrentChunk.YStartPoint*4+20),(CurrentChunk.XStartPoint*4+50,CurrentChunk.YStartPoint*4+50),1)
   pygame.display.flip()
   time.sleep(0.025)
ChooseMapSize()

input()