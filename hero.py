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
    def damage(self, new_damage: list) -> None:
        self._damage += new_damage

    def heal()