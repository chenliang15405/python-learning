import pygame

from airplane_game.plane_main import SCREEN_RECT

"""
如果继承的父类不是object类，那么在__init__方法中，一定要super() 一下父类的__init__方法，
因为需要先初始化父类的__init__方法（定义的属性等）

"""


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def update(self):
        """重写父类方法"""

        # 调用父类方法
        super().__init__()

        # 判断是否移出屏幕，如果移出屏幕，则将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        pass


