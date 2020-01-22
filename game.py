from models import Player
from models import Enemy
import exeptions


def play():
    print('Enter your name: ')
    name = input()
    player = Player(name)
    level = 1
    enemy = Enemy(level)
    while player.lives > 0:
        try:
            player.attack(enemy)
            player.defence(enemy)
            print(player.score)
            print(player.lives)
        except exeptions.EnemyDown:
            level += 1
            player.score += 5
            enemy = Enemy(level)


if __name__ == '__main__':
    try:
        play()
    except exeptions.GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye')



