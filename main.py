
import pygame
from pygame.locals import *
import time
import plgame
import plane

def main():

    # 获得此游戏总控制类
    planeGame = plgame.PlGame.getPlGame()

    # 创建英雄飞机实例
    heroPlane = plane.HeroPlane(planeGame)

    # 把英雄飞机实例加入游戏控制类中
    planeGame.addItem(heroPlane)

    enemyPlane = plane.EnemyPlane(planeGame)

    planeGame.addItem(enemyPlane)


    while True:

        # 按键处理
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 游戏总控制类事件处理
            planeGame.keyHandle(event)

        planeGame.run()

        planeGame.draw()

        time.sleep(1/1000)


if __name__ == '__main__':
    main()
