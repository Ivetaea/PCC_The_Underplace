def WeaponMenu(menuSelect, itemNames, itemDurability, itemDamage,itemID):
  best = 0
  while menuSelect.upper() != "MAIN":
    menuSelect = input("Available Weapons: [Axe], [Sword], [Staff], [Knife], \
    [BEST] for the highest quality item, or \n[MAIN] to go back to main menu.\n")
    
    if menuSelect.upper() == "AXE": #Item ID = 0
      print("\nItem name:",itemNames[0], "\nDamage:",itemDamage[0],\
            "\nDurability:",itemDurability[0],"\n\
                Two-handed weapon.\n")
      continue
      
    if menuSelect.upper() == "SWORD": #Item ID = 1
      print("\nItem name:",itemNames[1], "\nDamage:",itemDamage[1],\
            "\nDurability:",itemDurability[1],"\n\
            One-handed weapon.\n")
      continue
      
    if menuSelect.upper() == "STAFF": #Item ID = 2
      print("\nItem name:",itemNames[2], "\nDamage:",itemDamage[2],\
            "\nDurability:",itemDurability[2],"\n\
            Two-handed weapon. Also increases mana by 20.\n")
      continue
      
    if menuSelect.upper() == "KNIFE": #Item ID = 3
      print("\nItem name:",itemNames[3], "\nDamage:",itemDamage[3],\
            "\nDurability:",itemDurability[3],"\n\
            One-handed weapon. Deals more damage while you are undetected.\n")
      continue

    if menuSelect.upper() == "BEST":
      i = 0
      while i < 4:
        if best < itemDamage[i]:
          best = itemDamage[i]
          bestID = itemID[i]
        i += 1
      print("\nSelecting item with the highest effectiveness:\n\
            Item name:",itemNames[bestID],\
            "\nLook up this item in the appropriate menu to see more details.\n")
      continue
        
      
    #return to main
    if menuSelect.upper() == "MAIN":
      break
    #invalid input message
    else:
      print("That was not a valid menu option!\n")

