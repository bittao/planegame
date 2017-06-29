
import random
from base import *
from pygame.locals import *
import weapon


class Plane(Base):


    def __init__(self, plGame, x, y, imagePath):
        super(Plane, self).__init__(plGame, x, y, imagePath)
        self.__bulletList = []

    def draw(self):
        super(Plane, self).draw()
        for bullet in self.__bulletList:
            bullet.draw()

    def run(self):
        self.move()
        dellist = []
        for bullet in self.__bulletList:
            bullet.move()
            if bullet.judge():
                dellist.append(bullet)

        for bullet in dellist:
            self.__bulletList.remove(bullet)


    def addBullet(self, bullet):
        self.__bulletList.append(bullet)

class EnemyPlane(Plane):


    def __init__(self, plGame):
        super(EnemyPlane, self).__init__(plGame, 0, 0, './feiji/enemy-2.gif')
        self.__step = 10
        self.__height = 89
        self.__wight = 69
        self.__way = 'right'

    def move(self):
        if 0 >= self.getX():
            self.__way = 'right'
        elif self.getPlGame().getWight() <= self.getX() + self.__wight:
            self.__way = 'left'

        if self.__way == 'right':
            self.x_move(self.__step)
        elif self.__way == 'left':
            self.x_move(0-self.__step)

        if random.randint(1,100) <= 10:
            self.addBullet(weapon.EnemyBullet(self.getPlGame(), self.getX()+self.__wight/2, \
                                              self.getY()+self.__height+10))


class HeroPlane(Plane):

    def __init__(self, plGame):
        self.__height = 124
        self.__wight = 100
        super(HeroPlane, self).__init__(plGame, plGame.getWight()/2 - self.__wight/2, \
                                        plGame.getHeight() - self.__height - 20, \
                                        './feiji/hero.gif')
        self.__step = 10
        self.__keylist = [None]
        self.__space = None

    def move(self):
        if self.__keylist[0] == K_DOWN and \
                self.getY() + self.__step < self.getPlGame().getHeight() - self.__height/2:
            self.y_move(self.__step)
        elif self.__keylist[0] == K_UP and \
                self.getY() - self.__step > 0 - self.__height/2:
            self.y_move(0-self.__step)
        elif self.__keylist[0] == K_LEFT and \
                self.getX() - self.__step > 0 - self.__wight/2:
            self.x_move(0-self.__step)
        elif self.__keylist[0] == K_RIGHT and \
                self.getX() + self.__step < self.getPlGame().getWight() - self.__wight/2:
            self.x_move(self.__step)

        if self.__space == K_SPACE:
            # 产生子弹
            self.addBullet(weapon.HeroBullet(self.getPlGame(), self.getX()+self.__wight/2, \
                                             self.getY()-10))

    def keyProcess(self, event):
        if event.type == KEYDOWN:
            # 上下左右按键按下加入按键列表
            if event.key == K_a or event.key == K_LEFT:
                self.__keylist.insert(0, K_LEFT)
            elif event.key == K_d or event.key == K_RIGHT:
                self.__keylist.insert(0, K_RIGHT)
            elif event.key == K_w or event.key == K_UP:
                self.__keylist.insert(0, K_UP)
            elif event.key == K_s or event.key == K_DOWN:
                self.__keylist.insert(0, K_DOWN)
            elif event.key == K_SPACE:
                # # 产生子弹
                # self.addBullet(weapon.HeroBullet(self.getPlGame(), self.getX()+self.__wight/2, self.getY()-10))
                self.__space = K_SPACE
        elif event.type == KEYUP:
            # 上下左右按键弹起从列表中移除
            if event.key == K_a or event.key == K_LEFT:
                self.__keylist.remove(K_LEFT)
            elif event.key == K_d or event.key == K_RIGHT:
                self.__keylist.remove(K_RIGHT)
            elif event.key == K_w or event.key == K_UP:
                self.__keylist.remove(K_UP)
            elif event.key == K_s or event.key == K_DOWN:
                self.__keylist.remove(K_DOWN)
            elif event.key == K_SPACE:
                self.__space = None



# from base import *
# from pygame.locals import *
#
#
# class Plane(Base):
#
#
#     def __init__(self, plGame, x, y, imagePath):
#         super(Plane, self).__init__(plGame, x, y, imagePath)
#         self.bulletList = []
#
#     def draw(self):
#         super(Plane, self).draw()
#         for bullet in self.bulletList:
#             bullet.draw()
#
#
# class HeroPlane(Plane):
#
#     def __init__(self, plGame):
#         super(HeroPlane, self).__init__(plGame, 150, 480, './feiji/hero.gif')
#         self.step = 10
#         self.keylist = [None]
#
#     def move(self):
#         x,y = self.getPoint()
#         if self.keylist[0] == K_DOWN:
#             y += self.step
#         elif self.keylist[0] == K_UP:
#             y -= self.step
#         elif self.keylist[0] == K_LEFT:
#             x -= self.step
#         elif self.keylist[0] == K_RIGHT:
#             x += self.step
#
#         if x < -50:
#             x += self.step
#         elif x > 480 - 50:
#             x -= self.step
#         elif y < -62:
#             y += self.step
#         elif y > 800 - 62:
#             y -= self.step
#         self.setPoint(x, y)
#
#     def run(self):
#         self.move()
#
#     def keyProcess(self, event):
#         if event.type == KEYDOWN:
#             # 上下左右按键按下加入按键列表
#             if event.key == K_a or event.key == K_LEFT:
#                 self.keylist.insert(0, K_LEFT)
#             elif event.key == K_d or event.key == K_RIGHT:
#                 self.keylist.insert(0, K_RIGHT)
#             elif event.key == K_w or event.key == K_UP:
#                 self.keylist.insert(0, K_UP)
#             elif event.key == K_s or event.key == K_DOWN:
#                 self.keylist.insert(0, K_DOWN)
#             elif event.key == K_SPACE:
#                 # 产生子弹
#                 print('space')
#         elif event.type == KEYUP:
#             # 上下左右按键弹起从列表中移除
#             if event.key == K_a or event.key == K_LEFT:
#                 self.keylist.remove(K_LEFT)
#             elif event.key == K_d or event.key == K_RIGHT:
#                 self.keylist.remove(K_RIGHT)
#             elif event.key == K_w or event.key == K_UP:
#                 self.keylist.remove(K_UP)
#             elif event.key == K_s or event.key == K_DOWN:
#                 self.keylist.remove(K_DOWN)
#

