
import pygame



class Base(object):


    def __init__(self, planeGame, x, y, imagePath):
        self.__planeGame = planeGame
        self.__x = x
        self.__y = y
        self.__image = pygame.image.load(imagePath)

    def draw(self):
        self.__planeGame.getScreen().blit(self.__image, (self.__x, self.__y))


    def keyProcess(self, event):
        pass

    def run(self):
        pass

    def getPoint(self):
        return self.__x,self.__y

    def setPoint(self, x, y):
        self.__x,self.__y = x,y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def x_move(self, pos):
        self.__x += pos

    def y_move(self, pos):
        self.__y += pos

    def getPlGame(self):
        return self.__planeGame


# import pygame
#
#
#
# class Base(object):
#
#
#     def __init__(self, planeGame, x, y, imagePath):
#         self.planeGame = planeGame
#         self.x = x
#         self.y = y
#         self.image = pygame.image.load(imagePath)
#
#     def draw(self):
#         self.planeGame.getScreen().blit(self.image, (self.x, self.y))
#
#
#     def keyProcess(self, event):
#         pass
#
#     def run(self):
#         pass
#
#     def getPoint(self):
#         return self.x,self.y
#
#     def setPoint(self, x, y):
#         self.x,self.y = x,y
#
#
#
