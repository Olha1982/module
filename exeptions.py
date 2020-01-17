class GameOver(Exception):
    my_file = open('scores.txt', 'w')

    my_file.close()


class EnemyDown(Exception):
    pass
