import random
#this will be the code to randomly choose a monster
#ChosenMonster = ForestMonsters[random.randint(0,len(ForestMonsters)-1)]
class Monster:
  def __init__(self,Name):
    self.Name = Name
    self.MaxHealth = 0
    self.CurrentHealth = 0
    self.MaxStamina = 0
    self.CurrentStamina = 0
  def SetLevel(self,Level):
    self.Level = Level
    self.MaxHealth = 100 + self.Level*25
    self.CurrentHealth = self.MaxHealth
    self.MaxStamina = 100 + self.Level*25
    self.CurrentStamina = self.MaxStamina
  def AffectHealth(self,Change):
    self.CurrentHealth += Change
    if self.CurrentHealth < 0:
      self.CurrentHealth = 0
#ForestMonsters
Goblin = Monster('Goblin')
Ogre = Monster('Ogre')
Treant = Monster('Treant')
Druid = Monster('Druid')
WildBoar = Monster('Wild Boar')
Wolf = Monster('Wolf')
DireWolf = Monster('Dire Wolf')
GrizzlyBear = Monster('Grizzly Bear')
Python = Monster('Python')
#list To Randomly Choose From
ForestMonsters = [Goblin,Ogre,Treant,Druid,WildBoar,Wolf,DireWolf,GrizzlyBear,Python]
#DesertMonsters
Scorpion = Monster('Scorpion')
SandShark = Monster('SandShark')
Vulture = Monster('Vulture')
SentientSandstorm = Monster('Sentient Sandstorm')
SandSnake = Monster('SandSnake')
Coyote = Monster('Coyote')
Tarantula = Monster('Tarantula')
Hyena = Monster('Hyena')
Armadillo = Monster('Armadillo')
#list To Randomly Choose From
DesertMonsters = [Scorpion,SandShark,Vulture,SentientSandstorm,SandSnake,Coyote,Tarantula,Hyena,Armadillo]