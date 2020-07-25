import os #import os, a tool for finding files and not letting python write support prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide" #hide support prompt
import pygame,sys,random,threading #import pygame and sys, a tool for exiting, and random, a tool for random choices, and threading, a tool for setting non-blocking timers
pygame.init() #initiate pygame
screen=pygame.display.set_mode((700,700)) #setup display
pygame.display.set_caption("Tetris") #set caption
tetrislogo=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/tetris/pictures/tetrislogo.png") #load tetris logo
play=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/tetris/pictures/play.png") #load play button
screen.fill((50,50,50)) #fill screen
screen.blit(tetrislogo,(350-tetrislogo.get_width()/2,100-tetrislogo.get_height()/2)) #draw the tetris logo
screen.blit(play,((350-play.get_width()/2,600-play.get_height()/2))) #draw the play button
keep_going=True #set keep going to True

def load(names):
  for name in names:
    name_=f"C:/Users/Rainbow/Documents/GitHub/tetris/pictures/{name}.png"
    exec(f"global {name}")
    exec(f"{name}=pygame.image.load('{name_}')",globals())
def randomblock():
  x=random.choice("O left right tleft tright I tI L lL fL rL oL loL foL roL t rt ft lt".split())
  a=eval(x)
  a.set_colorkey((255,255,255))
  return a,x
class matrix:
  def __init__(self,string=(("0"*10+"\n")*20)[:-1]):
    self.matrix=[[int(y) for y in x] for x in string.split("\n")]
    self.x=len(self.matrix[0])
    self.y=len(self.matrix)
  def getat(self,xpos,ypos):
    try:
      if not xpos==0 and not ypos==0:
        return self.matrix[ypos][xpos]
      else:
        return matrix("")
    except:
      return matrix("")
  def collide(self,other,diff):
    for ypos1 in range(20-other.y):
      for xpos1 in range(10-other.x):
        xpos2=xpos1-diff[0]
        ypos2=ypos1-diff[1]
        if self.getat(xpos1,ypos1)==other.getat(xpos2,ypos2):
          return True
    return False
  def clear(self):
    self.matrix=[[0]*len(self.matrix[0])]*len(self.matrix)
def draw(blocks):
  a=blocks[0][0]
  b=blocks[1][0]
  c=blocks[2][0]
  d=blocks[3][0]
  nextsurface.blit(a,(50-a.get_width()/2,50-a.get_height()/2))
  nextsurface.blit(b,(50-b.get_width()/2,150-b.get_height()/2))
  nextsurface.blit(c,(50-c.get_width()/2,250-c.get_height()/2))
  nextsurface.blit(d,(50-d.get_width()/2,350-d.get_height()/2))
def getmatrix(block):
  block=block[1]
  def cond(block,listt):
    for x in listt:
      if block==x[0]:
        return matrix(x[1])
  return cond(block,(("O","11\n11"),("left","10\n11\n01"),("right","01\n11\n10"),("tleft","011\n110"),("tright","110\n011"),("I","1\n1\n1\n1"),("tI","1111"),("L","10\n10\n11"),("rL","111\n100"),("fL","11\n01\n01"),("lL","001\n111"),("oL","01\n01\n11"),("roL","100\n111"),("foL","11\n10\n10"),("loL","111\n001"),("t","111\n010"),("rt","01\n11\n01"),("ft","010\n111"),("lt","10\n11\n10")))
listofblocks=[]
for root,_,files in os.walk("C:/Users/Rainbow/Documents/GitHub/tetris/pictures"):
  for file in files:
    if file not in ["play.png","tetrislogo.png"]:
      listofblocks+=[file[:-4]]
load(listofblocks)
while keep_going: #while you are keep going
  for event in pygame.event.get(): #for every event
    if event.type==pygame.QUIT: #if the type is quit
      pygame.quit() #quit
      sys.exit()
    if event.type==pygame.MOUSEBUTTONDOWN: #if you click
      pos=pygame.mouse.get_pos() #set pos to be the position of the mouse
      if pos[0]>=350-play.get_width()/2 and pos[0]<=350+play.get_width()/2 and pos[1]>=600-play.get_height()/2 and pos[1]<=600+play.get_height()/2: #if you click on the button
        keep_going=False #stop going
  pygame.display.flip() #update screen
screen.fill((50,50,50))
pygame.display.flip()
keep_going=True
screenmatrix=matrix()
blocks=[randomblock(),randomblock(),randomblock(),randomblock()]
currentblock=randomblock()
nextsurface=pygame.Surface((100,400))
matrixscreen=pygame.Surface((100,200))
alreadymatrix=pygame.Surface((100,200))
while keep_going:
  screen.fill((50,50,50))
  nextsurface.fill((100,100,100))
  matrixscreen.fill((255,255,255))
  alreadymatrix.fill((255,255,255))
  currentblock=blocks.pop(0)
  blocks+=[randomblock()]
  draw(blocks)
  screen.blit(nextsurface,(550,50))
  screen.blit(matrixscreen,(300,250))
  blockmatrix=getmatrix(currentblock)
  xpos=random.randint(0,currentblock[0].get_width()/10-1)*10
  ypos=0
  yes=True
  while yes:
    matrixscreen.fill((255,255,255))
    matrixscreen.blit(currentblock[0],(xpos,round(ypos/10)*10))
    screen.blit(matrixscreen,(300,250))
    ypos+=0.15
    pygame.display.flip()
    yes=False
    for x in [305,315,325,335,345,355,365,375,385,395]:
      for y in [255,265,275,285,295,305,315,325,335,345,355,365,375,385,395,405,415,425,435,445]:
        if not screen.get_at((x,y))==(255,255,255,255):
          yes=True
    for event in pygame.event.get():
      pass
  keep_going=False
