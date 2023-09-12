import random
RATIO_LIFE_DAMAGE = 2
class Monster:
    def __init__(self, monster_name: str, current_hero_level: int) -> None:
        self._monster_name = monster_name
        self._level = self.get_possible_level(current_hero_level)
        self._hp = RATIO_LIFE_DAMAGE * self.level
        self._damage = RATIO_LIFE_DAMAGE * self.level

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
    def monster_name(self) -> str:
        return self._monster_name
    
    @hp.setter
    def hp(self, new_hp: int) -> None:
        self._hp = new_hp

    @damage.setter
    def damage(self, new_damage: int) -> None:
        self._damage = new_damage

    @level.setter
    def level(self, new_level: int) -> None:
        self._level = new_level

    def get_possible_level(self, current_hero_level: int) -> int:
        """
        a function that checks the possible levels a monster can have and choose a random level
        based on instructions
        """
        if current_hero_level == 1:
            return random.choice([1, 2])
        else:
            return random.choice([current_hero_level - 1, current_hero_level, current_hero_level + 1])
        
    def attack(self, hero_obj: object, defend_activated: bool) -> None:
        """
        a function that reduces the hero's lives based on the damage 
        """
        hero_obj.reduce_health(self, defend_activated)

    def reduce_health(self, hero_obj: object) -> int:
        """
        a function that reduces the monster's lives based on the damage
        """
        if hero_obj.damage <= self.hp:
            self.hp -= hero_obj.damage
        else:
            self.hp = 0
        return self.hp