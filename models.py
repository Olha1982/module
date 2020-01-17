import random
from exeptions import EnemyDown
from exeptions import GameOver


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return random.choice([1, 2, 3])

    def decrease_lives(self):
        self.level -= 1
        if self.level == 0:
            raise EnemyDown()
        return self.level


class Player:
    def __init__(self, name, lives=4, score=0):
        self.name = name
        self.lives = lives
        self.score = score

    @staticmethod
    def fight(attack, defense):
        res = None
        if attack == defense:
            res = 0
        elif attack == 2 and defense == 1:
            res = 1
        elif attack == 1 and defense == 3:
            res = 1
        elif attack == 3 and defense == 2:
            res = 1
        elif attack == 1 and defense == 2:
            res = -1
        elif attack == 2 and defense == 3:
            res = -1
        elif attack == 3 and defense == 1:
            res = -1
        return res

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver()
        return self.lives


    def choice_hero(self):
        print(str("Choose your HERO: 1 - MAG, 2 - WARRIOR, 3 - ROGUE"))
        choice_hero = int(input())
        return choice_hero

    def attack(self, enemy_obj):
        enemy_attack = enemy_obj.select_attack()
        player_attack = self.choice_hero()
        result = self.fight(player_attack, enemy_attack)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.score += 1
        elif result == -1:
            print("You missed!")
        else:
            print('')

    @staticmethod
    def defence(self, enemy_obj):
        enemy_attack = enemy_obj.select_attack()
        player_attack = self.choice_hero()
        result = self.fight(enemy_attack, player_attack)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        elif result == -1:
            print("Your enemy missed!")
        else:
            print("")

