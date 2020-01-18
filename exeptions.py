class GameOver(Exception):
    pass

    @staticmethod
    def save_result(name, score):
        f = open('scores.txt', 'a')
        f.write(f"Name{score.name}, Score: {score.score} \n")
        f.close()


class EnemyDown(Exception):
    pass
