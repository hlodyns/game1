import sys
import os
import random
import time
import math

#BİSMİLLAHİRRAHMANİRRAHİM
class Game:
    def print_slow(self, str, delay = 0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")

    def reset_console(self):
        print("\n")
        os.system('cls||clear')

    def fprint(self, str, delay = 0):
        print("\n" + str)
        time.sleep(delay)

    def sprint (self, str, delay = 0):
        print(str)
        time.sleep(delay)

game_functions = Game()

class player:
    def __init__(self, location, health, armor, att_point, items):
        self.health = health
        self.items = items
        self.location = location
        self.armor = armor
        self.att_point = att_point #Henüz kullanılmıyor.
        
hero = player("", 100, 1, 1, [])

class NPC:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
    def attack(self):
        game_functions.fprint(f"A {self.name} emerges from the shadows. And attacks you!")
        game_functions.fprint("'Hissssss! Stay away form me!!'")
        attack_value = random.randint(15,25)
        hp_reduce = attack_value - (attack_value % (5 * hero.armor))
        hero.health -= hp_reduce 
        game_functions.fprint(f"\nYou lost {hp_reduce} hp. Health:{hero.health}")

    def move(self):
        available_locations = ["entry", "cavern", "hallway", "pit"]
        self.location = random.choice(available_locations)

    
goblin = NPC("goblin", "hallway")

class World:
    
    def use_medkit(self):
        if "medkit" in hero.items:
            hero.items.remove("medkit")
            game_functions.fprint("You used your medkit.")
            
            if hero.health == 100:
                game_functions.fprint("You are at max health. You wasted your medkit for nothing.", 2)
            elif hero.health >= 90:
                hero.health == 100
            else:
                hero.health += 10
            print(f"\nHealth:{hero.health}")
        else:
            game_functions.fprint("You don't have a medkit.")

    def check_medkit(self):
        medkit_find = random.randint(0,100)
        if medkit_find <= 100:
            hero.items.append("medkit")
            game_functions.fprint("You found a medkit.", 2)
            game_functions.fprint("Enter 'm' to use it.", 2)

    def check_bat_attack(self):
        bat_attack = random.choice([True, False])
        bat_attack = True
        if bat_attack == True:
            game_functions.fprint("You were attacked by a swarm of bats!", 2)
            attack_value = random.randint(10,30)
            hp_reduce = attack_value - (attack_value % (5 * hero.armor)) 
            hero.health -= hp_reduce 
            game_functions.fprint(f"\nHealth: {hero.health}", 2)
        
    def handle_goblin(self):
        goblin.move()
        if hero.location == goblin.location:
            goblin.attack()    

    def show_stats(self):
        print(f"\nHP: {hero.health}")
        print(f"\nArmor: {hero.armor}")
        print(f"\nAtt. Points: {hero.att_point}")

    def menu(self):
        print("1-) Start Game!")
        print("2-) Help")
        print("3-) Exit")
        choice = input("\n> ")
        if choice == "1":
            self.entry()
        elif choice == "2":
            print("Type 'stats' to see your characters stats.")
            self.menu()
        elif choice == "3":
            sys.exit()
        else:
            print("Please type 1 to start the game or type 2 to exit the game.")
            
    def entry(self):
        hero.location = "entry"
        print(f"\nHealth:{hero.health}")
        game_functions.fprint("You are in a dark cave! The entry has been sealed by fallen rocks. There is no way out.", 2)
        
        print("Ahead, you can see a cavern. Will you continue?")
        print("Enter 'yes' or 'no'.")
        while True:
            action = input("\n> ")
            if action == "yes":
                self.cavern()
            elif action == "no":
                game_functions.fprint("A bat flies over your head and you hear noises in the distance.")  
            elif action == "stats":
                self.show_stats()
            else:
                game_functions.fprint("You sit in total darkness, wondering if there is a way out.")

    def cavern(self):
        hero.location = "cavern"
        print(f"\nHealth:{hero.health}")
        game_functions.fprint("You stumble into a dimly lit cavern.", 2)
        
        self.check_bat_attack()
        
        self.check_medkit()
        
        self.handle_goblin()
        
        print("You cannot go right or left. But the cave continues ahead. Will you go on ?")
        print("Enter 'yes' or 'no'.")
        while True:
            action = input("\n> ")
            if action == "yes":
                self.hallway()
            elif action == "no":
                game_functions.fprint("You sit down and eat some food you brought with you.")        
            elif action == "m":
                self.use_medkit()  
            elif action == "stats":
                self.show_stats()
            else:
                game_functions.fprint("You shiver from the cold.")    

    def hallway(self):
        hero.location = "hallway"
        print(f"\nHealth:{hero.health}")
        game_functions.fprint("You are in a wide hallway. It continues on and on and on.", 2)
        
        self.check_medkit()
        
        self.handle_goblin()
        
        print("There is no turning back. Will you go on?")
        print("Enter 'yes' or 'no'.")
        while True:
            action = input("\n> ")
            if action == "yes":
                self.pit()
            elif action == "no":
                game_functions.fprint("You try to call for help but no one is there.")        
            elif action == "m":
                self.use_medkit()    
            elif action == "stats":
                self.show_stats()
            else:
                game_functions.fprint("You wonder what time it is.")

    def pit(self):
        hero.location = "pit"
        print(f"\nHealth:{hero.health}")
        game_functions.fprint("You fall head first into a pit of ash and dust.", 2)
        game_functions.sprint("Luckily, you only landed on your back.", 2)
        
        self.check_medkit()
        
        self.handle_goblin()
        
        print("You can try to climb out. Will you try ?")
        print("Enter 'yes' or 'no'.")
        while True:
            action = input("\n> ")
            if action == "yes":
                game_functions.fprint("You tried to climb out, but you slide of the rocky walls and fall back down.", 2)
                print("GAME OVER!")
                sys.exit()
            elif action == "no":
                game_functions.fprint("You sit in utter darknes")        
            elif action == "m":
                self.use_medkit()   
            elif action == "stats":
                self.show_stats()
            else:
                game_functions.fprint("You feel hopeless.")

new_world = World()

new_world.menu()



