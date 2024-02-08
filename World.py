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
                    "monsters": "monsters",
                    "resources" : "resources"
                },
                {
                    "region" : "dust II",
                    "monsters": "monsters",
                    "resources" : "resources"
                },
                {
                    "region" : "portland community college",
                    "monsters": "monsters",
                    "resources" : "resources"
                }
            ]

        self.curr_pos = 0 #starts the player at the first index of the map
        
    def where_am_i(self):
        print("+---------------------------------------------------+")
        print(f"Current location: {self.world_map[self.curr_pos]["region"]}")
        print("+---------------------------------------------------+")


    def check_monsters(self):
        
        monsters_list = self.world_map[self.curr_pos]["monsters"]

        print("+---------------------------------------------------+")
        print("Monsters in the current region:")
        
        for monster in monsters_list:
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

