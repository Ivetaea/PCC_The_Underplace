import Utility
from Player import Player
from Weapons import Weapons
quit = False

#initialize player
#see Player.py def__init__
player = Player()

#not sure if shop should be its own thing with
#the weapons class as part of it..
#but for not we'll just do this

shop = Weapons() 

while quit != True:
    choice = Utility.menuSelect()
    if choice == "1":
        shop.weaponSelect(player)
    if choice == "2":
        player.seeStats()
    if choice == '3':
        player.seeInventory()
    if choice == "9":
        quit = True
    

print("goodbye!")