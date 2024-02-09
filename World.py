class World:
    def __init__(self) -> None:
        self.world_map = [
                {
                    "region" : "desert",
                    "monsters" : ["goblins, snakes"],
                    "resources" : ["wood, ore, metal"]
                },
                {
                    "region" : "hyperion",
                    "monsters": ["none"],
                    "resources" : ["ore"],
                },
                {
                    "region" : "desert",
                    "monsters": "none",
                    "resources" : "none"
                },
                {
                    "region" : "portland community college",
                    "monsters": "none",
                    "resources" : "none"
                }
            ]

        self.curr_pos = 0 #starts the player at the first index of the map
        
    def where_am_i(self):
        print("+---------------------------------------------------+")
        print(f"Current location: {self.world_map[self.curr_pos]['region']}")
        print("+---------------------------------------------------+")


    def check_monsters(self):
        
        monsters_list = self.world_map[self.curr_pos]["monsters"]

        print("+---------------------------------------------------+")
        print("Monsters in the current region:")
        
        for monster in monsters_list:
            if monster == "none":
                print("There's nothing to fight here")
                break
            else:
                print(monster)
        
        print("+---------------------------------------------------+")
        
    def travel(self):
        print("Would you like to travel east or west?")
        choice = input("Enter east/west: ")

        if choice == "east" and self.curr_pos < len(self.world_map):
            self.curr_pos += 1
        elif choice ==  "west" and self.curr_pos > 0:
            self.curr_pos -= 1
        else:
            print("+--------------------------------+")
            print("You are at the edge of the world!")
            print("+--------------------------------+")

