import pygame
import time
from pygame.locals import *


def main():
    # 创建窗口
    screen = pygame.display.set_mode((480, 700), 0, 32)

    # 加载背景图
    bg = pygame.image.load('./bg.png')

    # 加载飞机图片
    airplane = pygame.image.load('./airplane.png')

    # 添加到主窗口上
    screen.blit(bg, (0, 0))
    screen.blit(airplane, (200, 550))

    # 刷新页面
    pygame.display.update()

    for event in pygame.event.get():
        pass

    # 让飞机动

    time.sleep(500)


if __name__ == '__main__':
    main()
