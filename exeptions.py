class GameOver(Exception):

    @staticmethod
    def save_result(name, score):
        f = open('scores.txt', 'a')
        f.write(f"Name: {name}, Score: {score} \n")
        f.close()


class EnemyDown(Exception):
    pass
