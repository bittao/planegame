
from base import *


class Bullet(Base):
    pass


class HeroBullet(Bullet):


    def __init__(self, plGame, x, y):
        self.__height = 22
        self.__wight = 22
        self.__step = -20
        super(Bullet, self).__init__(plGame, x-self.__wight/2, y-self.__height/2, './feiji/bullet.png')

    def move(self):
        self.y_move(self.__step)

    def judge(self):
        if self.getY() < 0 - self.__height:
            return True
        else:
            return False


class EnemyBullet(Bullet):


    def __init__(self, plGame, x, y):
        self.__height = 21
        self.__wight = 9
        self.__step = 10
        super(EnemyBullet, self).__init__(plGame, x-self.__wight/2, y-self.__height/2, \
                                          './feiji/bullet1.png')

    def move(self):
        self.y_move(self.__step)

    def judge(self):
        if self.getY() > self.getPlGame().getHeight():
            return True
        else:
            return False

