from hero import Hero
from monster import Monster

def choose_action() -> int:
    player_action = ""
    while player_action not in ["1", "2", "3", "4"]:
        player_action = input("It's your turn\nplease enter:\n1. to attack\n2. to level up\n3. to heal\n4. to defend\n")
    return int(player_action)

def create_new_monster(hero_obj: Hero, monster_num: int) -> Monster:
        """
        a function that creates a new monster with new name and returns the new objects
        """
        monster_name = f"monster{monster_num}"
        monster_obj = Monster(monster_name, hero_obj.level)
        return monster_obj

def main():
    hero_name = input("Please enter your hero's name:\n")
    hero_obj = Hero(hero_name)
    monster_num = 1
    monster_obj = create_new_monster(hero_obj, monster_num)
    defend_activated = False
    while True:
        player_action = choose_action()
        hero_obj.coins += 1
        if player_action == 1:
            hero_obj.attack(monster_obj)
            print(f"Action was successful!\nMonster's hp now is: {monster_obj.hp}")
            if monster_obj.hp == 0:
                monster_num +=1
                monster_obj = create_new_monster(hero_obj, monster_num)
                print(f"You killed the monster!\nYou are facing {monster_obj.monster_name}")
        elif player_action == 2:
            if hero_obj.level_up():
                print(f"Action was successful!\nNew level: {hero_obj.level}\nNew damage: {hero_obj.damage}\n\
New hp: {hero_obj.hp}\nAmount of coins: {hero_obj.coins}")
            else:
                print("You don't have enough coins for this action")
        elif player_action == 3:
            hero_obj.heal()
            print(f"Action is successful!\nNew hp: {hero_obj.hp}")
        else:
            defend_activated = True
            print("action was successful")
        print("Now the monster is making his turn!")
        monster_obj.attack(hero_obj, defend_activated)
        defend_activated = False
        if hero_obj.hp == 0:
            break
    print("The hero died! game is over!")


if __name__ == "__main__":
    main()