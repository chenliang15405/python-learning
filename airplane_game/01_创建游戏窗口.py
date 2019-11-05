from images.plane_sprites import *


# 游戏初始化
pygame.init()

# 创建游戏主窗口
screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("../images/background.png")
# 第二个参数表示背景图片的位置和左上角（0,0）z坐标的距离
screen.blit(bg, (0, 0))

# 绘制飞机
hero = pygame.image.load("../images/me1.png")
screen.blit(hero, (200, 500))

 # 更新显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("../images/enemy1.png")
enemy1 = GameSprite("../images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy)

# 游戏循环
while True:

    # 可以指定循环中代码执行的频率（帧率）
    clock.tick(60)

    # 捕获事件, 游戏窗口中的触发事件
    # 事件监听
    for event in pygame.event.get():

        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            # 直接退出系统
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机y的位置
    if hero_rect.y + hero_rect.height < 0:
        hero_rect.y = 700

    #  调用blit方法绘制图像
    # 先绘制背景，就会遮挡住上一次的飞机，再绘制新位置的飞机
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用方法
    enemy_group.update() # 让组中的所有精灵更新位置
    enemy_group.draw(screen) # 在此screen上绘制所有的精灵

    pygame.display.update()

    pass

pygame.quit()

