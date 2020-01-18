from models import Player
from models import Enemy
import exeptions


def play():
    print('Enter your name: ')
    name = str(input())
    print("Please enter 'start' to start the game")
    command_start = str(input())
    Player(command_start)
    player = Player(name)
    level = 1
    enemy = Enemy(level)
    while player.lives > 0:
        player.attack(enemy)
        if enemy.level == 0:
            level += 1
            enemy = Enemy(level)
            player.score += 5
        player.defence(enemy)
        print(player.score)


if __name__ == '__main__':
    try:
        play()
    except exeptions.GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye')



