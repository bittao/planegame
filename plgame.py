
import pygame
from pygame.locals import *

class PlGame(object):


    __instance = None
    __isFirst = True

    def __init__(self):
        if PlGame.__isFirst:
            # 串口宽高
            self.__wight = 480
            self.__height = 750
            # command按键是否按下
            self.__commandkey = None
            # 窗口初始化
            pygame.init()
            # 获得窗口实例
            self.__screen = pygame.display.set_mode((self.__wight, self.__height), 0, 32)
            # 设置窗口名
            pygame.display.set_caption("PlaneGame")
            # 背景图片
            self.__blackgroundImage = pygame.image.load("feiji/background.png")
            self.__itemList = []
            PlGame.__isFirst = False

    def __new__(cls, *args, **kwargs):
        if not PlGame.__instance:
            PlGame.__instance = object.__new__(cls)
        return PlGame.__instance

    @staticmethod
    def getPlGame():
        return PlGame()

    def draw(self):
        self.__screen.blit(self.__blackgroundImage, (0, 0))
        for item in self.__itemList:
            item.draw()
        pygame.display.update()

    def addItem(self, item):
        self.__itemList.append(item)

    def getScreen(self):
        return self.__screen

    def keyHandle(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LMETA:
                self.__commandkey = K_LMETA
            elif event.key == K_q and self.__commandkey == K_LMETA:
                exit()
        elif event.type == KEYUP:
            if event.key == K_LMETA:
                self.__commandkey = None

        for item in self.__itemList:
            item.keyProcess(event)

    def run(self):
        for item in self.__itemList:
            item.run()

    def getHeight(self):
        return self.__height

    def getWight(self):
        return self.__wight
