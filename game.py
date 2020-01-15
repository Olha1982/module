import random
class Game:
   TYPES = ('wizard', 'warrior', 'robber')

   def __init__(self):
       #: WIN, LOSE, DRAW
       counts = 0, 0, 0
       num = 0

   def increase_count(self, n):
       counts[n] += 1

   def round_logic(self):
       if self.user_choice == self.ii_choice:
           print('Ничья')
           self.increase_count(2)
       elif (self.user_choice == 'wiz' and self.ii_choice == 'war')
               or (self.user_choice == war and self.ii_choice == 'wizz')
               or (self.user_choice == 'rob' and self.ii_choice == 'wiz'):
           print('Выигрыш')
           self.increase_count(0)
       else:
           print('Проигрыш')
           self.increase_count(1)

   def round(self):
       while True:
           self.user_choice = input('wizard(wiz), warrior (war), robber (rob)')
           if self.user_choice not in Game.TYPES:
               print('Введите wiz, war, rob')
           else:
               break

       self.ii_choice = random.choice(Game.TYPES)
       self.round_logic()

       self.num -= 1
       if self.num is 0:
           self.end()

   def end(self):
       print('Победы - {0}\nПроигрыши - {1}\nНичьи- {2}'.format(*self.counts)

   @staticmethod
   def start(class):
       while True:
           try:
               n = int(input('Введите количество игр n '))
               return Game(n)
           except ValueError:
               print('Это не число!')


if __name__ == '__main__':
    Game.start()


