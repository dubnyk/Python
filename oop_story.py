import sys

class Hero():
  health = 100
  attack_damage = 20
  healing_increase = 50
  
  def drink_potion(self):
    self.health += self.healing_increase
    print("Ahhh, healing potion. I feel mighty again!")
    print(">> Hero's health: %s\n" % self.health)
    
  def attack_monster(self, name):
    print("Take that you fiend!")
    name.health -= self.attack_damage
    print(">> Monster's health: %s\n" % name.health)
    if name.health < 30:
      print("Begone you hellish brute!")
      print(">> The monster has run away\n")
      sys.exit()
  
class Monster():
  health = 100
  attack_damage = 30
  
  def roar(self):
    print("RooooaarrRRRR!")
    
  def attack_hero(self, name):
    print("Raaaaarrrrrrr!!")
    name.health -= self.attack_damage
    print(">> Hero's health: %s\n" % name.health)
    if name.health <= 0:
      print("Raaar RaaarrrRR RRARRR!")
      print(">> The hero is no more\n")
      sys.exit()
    
warrior = Hero()
beast = Monster()

# Start of our story...
print("A monster leaps from its cave and strikes our hero!\n")
beast.attack_hero(warrior)
warrior.attack_monster(beast)
beast.attack_hero(warrior)
warrior.drink_potion()
beast.roar()
warrior.attack_monster(beast)
warrior.attack_monster(beast)
beast.attack_hero(warrior)
warrior.attack_monster(beast)
