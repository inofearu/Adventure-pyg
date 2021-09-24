import pygame
def functions():
  AvailableFunctions = ['Update.ClearScreen()','Update.Gold(player_gold)','Update.HealthStamina(current_player_health,max_player_health,current_player_stamina,max_player_stamina)','Update.ScreenText(strength,perception,endurance,charisma,luck,agility,intelligence,\'-Enter Name-\',stat_points)']
  return AvailableFunctions
Coin_PNG = pygame.image.load('Images/Coin.png')
Heart_PNG = pygame.image.load('Images/Heart.png')
Stamina_PNG = pygame.image.load('Images/Stamina.png')
Fonts = ["comicsansms","dejavusansmono","freesans","dejavusans","freeserif","freemono"]
screen = pygame.display.set_mode((610, 325))
BackgroundColor = (79, 105, 198)
Black = ( 0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = ( 255, 0, 0)
Blue = (0,96,255)
def Bar(color, Fill,X,Y,Height,Width,BorderSize,MaxVariable,Variable,H_V):
  if Variable > MaxVariable:
    MaxVariable = Variable
  if H_V in ['H','h']:
   bar_percentage = Variable / MaxVariable
   pygame.draw.rect(screen, color, pygame.Rect(X,Y,Width,Height))
   pygame.draw.rect(screen, Fill, pygame.Rect(X+(BorderSize/2),Y+(MaxVariable*(1-bar_percentage))+(BorderSize/2),Width-BorderSize,(Height-BorderSize)*bar_percentage) )
  if H_V in ['V','v']:
   bar_percentage = Variable / MaxVariable
   pygame.draw.rect(screen, color, pygame.Rect(X,Y,Width,Height))
   pygame.draw.rect(screen, Fill, pygame.Rect(X+(BorderSize/2),Y+(BorderSize/2),(Width-BorderSize)*bar_percentage,Height-BorderSize))
  pygame.display.flip()
def DrawBorder(color, Fill,X,Y,Height,Width,BorderSize, Location):
  global width
  global height
  if Location in ['L4']:
    X = (screen.get_width() // 4) - X
    Y = (screen.get_height() // 9) - Y
    pygame.draw.rect(screen, color, pygame.Rect(X,Y,Height,Width))
    pygame.draw.rect(screen, Fill, pygame.Rect(X+(BorderSize/2),Y+(BorderSize/2),Height-BorderSize,Width-BorderSize))
    pygame.display.flip()
  else:
    pygame.draw.rect(screen, color, pygame.Rect(X,Y,Height,Width))
    pygame.draw.rect(screen, Fill, pygame.Rect(X+(BorderSize/2),Y+(BorderSize/2),Height-BorderSize,Width-BorderSize))
    pygame.display.flip()
def DrawRectangle(color,X,Y,Height,Width,Location):
  global width
  global height
  if Location in ['L4']:
    X = (screen.get_width() // 4) - X
    Y = (screen.get_height() // 9) - Y
    print(X,Y)
    pygame.draw.rect(screen, color, pygame.Rect(X,Y,Height,Width))
    pygame.display.flip()
  else:
    pygame.draw.rect(screen, color, pygame.Rect(X,Y,Height,Width))
    pygame.display.flip()
def Text(Text,Color,Font,Size,Location,wm,hm,Underline):
  font = pygame.font.SysFont(Fonts[Font], Size)
  if Underline == True:
    fontUnderline= font
    fontUnderline.set_underline(True)
    textUnderline = fontUnderline.render(Text, True, (Color))
    if Location == 'TopCentre':
      Location = 320 + wm - textUnderline.get_width() // 2, 50 + hm - textUnderline.get_height() // 1
    elif Location == 'L4':
      Location = 320 + wm - textUnderline.get_width() // .4, 100 +  hm - textUnderline.get_height() // 1
    elif Location == 'R4':
      Location = 320 + wm - textUnderline.get_width() // 9, 100 + hm - textUnderline.get_height() // 1
    screen.blit(textUnderline,(Location))
  else:
    text = font.render(Text, True, (Color))
    if Location == 'TopCentre':
      Location = 320 + wm - text.get_width() // 2, 50 + hm - text.get_height() // 1
    elif Location == 'L4':
      Location = 320 + wm - text.get_width() // .4, 100 + hm - text.get_height() // 1
    elif Location == 'R4':
      Location = 320 + wm - text.get_width() // 9, 100 + hm - text.get_height() // 1
    screen.blit(text,(Location))
def Gold(PlayerGold):
  DrawBorder((BackgroundColor),(BackgroundColor), 460,22,70+(6*(len(str(PlayerGold)))),30,2,'R')
  screen.blit(Coin_PNG, ((340 - screen.get_width())+730,( 320 - screen.get_height())+25))
  Text(str(PlayerGold),Black,4,16,(495.5,31),-100,75,False)
  pygame.display.flip()
def ClearScreen():
  screen.fill(BackgroundColor)
def ScreenText(Strength,Perception,Endurance,Charisma,Luck,Agility,Intelligence,Name,Stat_Points):
  Text('Player Menu',Black,5,36,'TopCentre',0,0,True)
  DrawBorder((0,0,0),(79,105,198), 35,78,170,195,2,'L')
  DrawBorder((0,0,0),(79,105,198), 35,59,170,20,2,'L')
  Text('Name: '+Name,Black,4,12,(40,65),0,0,False)
  Text('Stat Points:' + str(Stat_Points),Black,4,16,(40.5,83),0,0,False)
  Text('Strength:' + str(Strength),Black,4,16,(40.5,103),0,0,False)
  Text('Perception:' + str(Perception),Black,4,16,(40.5,128),74,25,False)
  Text('Endurance:' + str(Endurance),Black,4,16,(40.5,153),23,50,False)
  Text('Charisma:' + str(Charisma),Black,4,16,(40.5,178),-4,100,False)
  Text('Intelligence:' + str(Intelligence),Black,4,16,(40.5,203),96,150,False)
  Text('Agility:' + str(Agility),Black,4,16,(40.5,228),-28,125,False)
  Text('Luck:' + str(Luck),Black,4,16,(40.5,253),-102,75,False)
  pygame.display.flip()
def HealthStamina(Health,Max_Health,Stamina,Max_Stamina):
  DrawBorder(BackgroundColor,(BackgroundColor), 210,215,250,85,2,'L')
  Bar((Black),(Red), 220,244.25,29,208,4,Max_Health, Health,'v')
  Bar((Black),(Blue), 215,274.25,20,218,4,Max_Stamina, Stamina,'v')
  Text(str(Health)+'  /  '+str(Max_Health),(58,58,58),4,16,'TopCentre',0,217,False)
  Text(str(Stamina)+'   /   '+str(Max_Stamina),(58,58,58),4,14,'TopCentre',0,241,False)
  Text('Health And Stamina',Black,1,20,'TopCentre',3,190,True)
  screen.blit(Heart_PNG, ((340 - screen.get_width())+695,( 320 - screen.get_height())+248))
  screen.blit(Stamina_PNG, ((340 - screen.get_width())+700,( 320 - screen.get_height())+271))
  pygame.display.flip()
def StrengthStat(Strength):
  DrawBorder((BackgroundColor),(BackgroundColor), 37,103,166,18.5,2,'L')
  Text('Strength:' + str(Strength),Black,4,16,(40.5,103),0,0,False)
  pygame.display.flip()
def PerceptionStat(Perception):
  DrawBorder((BackgroundColor),(BackgroundColor), 37,128,166,18.5,2,'L')
  Text('Perception:' + str(Perception),Black,4,16,(40.5,128),0,0,False)
  pygame.display.flip()
def EnduranceStat(Endurance):
  DrawBorder((BackgroundColor),(BackgroundColor), 37,153,166,18.5,2,'L')
  Text('Endurance:' + str(Endurance),Black,4,16,(40.5,153),23,50,False)
  pygame.display.flip()
def CharismaStat(Charisma):
  DrawBorder((BackgroundColor),(BackgroundColor), 37,178,166,18.5,2,'L')
  Text('Charisma:' + str(Charisma),Black,4,16,(40.5,178),-4,100,False)
  pygame.display.flip()
def IntelligenceStat(Intelligence):
  DrawBorder((BackgroundColor),(BackgroundColor), 37,203,166,18.5,2,'L')
  Text('Intelligence:' + str(Intelligence),Black,4,16,(40.5,203),96,150,False)
  pygame.display.flip()
def AgilityStat(Agility):
  DrawBorder((BackgroundColor),(BackgroundColor), 37,228,166,18.5,2,'L')
  Text('Agility:' + str(Agility),Black,4,16,(40.5,228),-28,125,False)
  pygame.display.flip()
def LuckStat(Luck):
  DrawBorder((BackgroundColor),(BackgroundColor), 37,253,166,18.5,2,'L')
  Text('Luck:' + str(Luck),Black,4,16,(40.5,253),-102,75,False)
  pygame.display.flip()
def NameText(Name):
  DrawBorder((BackgroundColor),(BackgroundColor), 37,60,166,18.5,2,'L')
  Text('Name: '+Name,Black,4,12,(40,65),0,0,False)
  pygame.display.flip()
def StatPoints(Stat_Points):
  DrawBorder((BackgroundColor),(BackgroundColor), 37,83,166,18.5,2,'L')
  Text('Stat Points:' + str(Stat_Points),Black,4,16,(40.5,83),0,0,False)
  pygame.display.flip()