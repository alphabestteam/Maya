ADD_LIFE_PERCENTAGE = 1.6
LEVEL_UP_PERCENTAGE = 1.4
TIMES_LEVEL_UP = 2
from monster import Monster

class Hero:
    def __init__(self, hero_name: str) -> None:
        self._hero_name = hero_name
        self._hp = 10
        self._damage = 2
        self._level = 1
        self._coins = 0

    @property
    def hero_name(self) -> str:
        return self._hero_name

    @property
    def hp(self) -> int:
        return self._hp
    
    @property
    def damage(self) -> int:
        return self._damage
    
    @property
    def level(self) -> int:
        return self._level
    
    @property
    def coins(self) -> int:
        return self._coins
    
    @hp.setter
    def hp(self, new_hp: int) -> None:
        self._hp += new_hp

    @damage.setter
    def damage(self, new_damage: int) -> None:
        self._damage += new_damage

    @level.setter
    def level(self, new_level: int) -> None:
        self._level += new_level

    @damage.setter
    def coins(self, new_coins: int) -> None:
        self._coins += new_coins

    def heal(self) -> None:
        """
        a function that adds 60% to the hp
        """
        self.hp *= ADD_LIFE_PERCENTAGE

    def level_up(self) -> None:
        """
        a function that upgrades the hero's level and damage and life if
        she has enough coins for it
        """
        if self.coins * TIMES_LEVEL_UP <= self.hp + 1:
            self.level += 1
            self.damage *= LEVEL_UP_PERCENTAGE
            self.hp *= LEVEL_UP_PERCENTAGE

    def attack(self, monster_obj: Monster) -> None:
        """
        a function that reduces the monster's lives based on the damage 
        """
        monster_hp = monster_obj.reduce_health(self)
        if monster_hp == 0:
            self.coins += self.level

    def defend(self, monster_damage: int):
        """
        a function that reduces the damage of the monster by 80 percent
        """
        return monster_damage / 0.8
    
    def reduce_health(self, monster_obj: Monster) -> None:
        """
        a function that reduces the monster's lives based on the damage
        """
        monster_damage = monster_obj.damage
        # if....
        monster_damage = self.defend(monster_obj.damage) #IF DEFEND WAS ACTIVATED THE TURN BEFORE
        
        if monster_damage <= self.hp:
            self.hp -= monster_damage
        else:
            self.hp = 0

    def increase_coins(self, coins_amount: int) -> None:
        """
        a function that adds a given amount of coins to the hero's coins
        """
        self.coins += coins_amount
    