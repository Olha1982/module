import random
class Enemy:
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives
    @staticmethod
    def select_attack():
        return random.choice([1, 2, 3])

    def decrease_lives(self):
        pass
class Player:
    def __init__(self, name, lives, score, allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_attacks
    @staticmethod
    def fight(attack, defense):
        pass
    def decrease_lives(self):
        pass
    def attack(self, enemy_obj):
        pass
    def defence(self, enemy_obj):
        pass