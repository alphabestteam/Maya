ADD_LIFE_PERCENTAGE = 1.6
LEVEL_UP_PERCENTAGE = 1.4
TIMES_LEVEL_UP = 2

class Hero:
    def __init__(self, hero_name: str) -> None:
        self._hero_name = hero_name
        self._hp = 10
        self._damage = 2
        self._level = 1
        self._coins = 0

    @property
    def hp(self):
        return self._hp
    
    @property
    def damage(self):
        return self._damage
    
    @property
    def level(self):
        return self._level
    
    @property
    def coins(self):
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

    def heal(self):
        """
        a function that adds 60% to the hp
        """
        self.hp *= ADD_LIFE_PERCENTAGE

    def level_up(self):
        """
        a function that upgrades the hero's level and damage and life if
        she has enough coins for it
        """
        if self.coins * TIMES_LEVEL_UP <= self.hp + 1:
            self.level += 1
            self.damage *= LEVEL_UP_PERCENTAGE
            self.hp *= LEVEL_UP_PERCENTAGE

    def attack(self, monster_obj: Monster):


    def defend():

    def reduce_health():

    def increase_coins():

    