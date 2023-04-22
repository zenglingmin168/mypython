import pygame
import time
import random

# 初始化pygame
pygame.init()

# 游戏屏幕大小
width = 2000
height = 600

# 创建游戏屏幕
screen = pygame.display.set_mode((width, height))

# 设置窗口标题
pygame.display.set_caption("Google Dino")

# 加载图像资源
dino_img = pygame.image.load("/Users/mac/mystudy/mypython/dino.png")
cactus_img = pygame.image.load("/Users/mac/mystudy/mypython/cactus.png")
bird_img = pygame.image.load("/Users/mac/mystudy/mypython/bird.png")
gameover_img = pygame.image.load("/Users/mac/mystudy/mypython/gameover.png")

# 定义颜色
black = (0, 0, 0)

# 游戏变量
dino_x = 2
dino_y = 5
dino_jump = False
dino_jump_height = 10
dino_jump_count = dino_jump_height
cactus_x = width
cactus_y = 5
cactus_speed = 2
bird_x = width
bird_y = random.randint(5, 10)
bird_speed = 5
score = 0
gameover = False

# 游戏循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino_jump = True

    # 更新游戏变量
    if dino_jump:
        dino_y -= int(dino_jump_count * abs(dino_jump_count) * 0.5)
        dino_jump_count -= 1
        if dino_jump_count <= -dino_jump_height:
            dino_jump = False
            dino_jump_count = dino_jump_height

    cactus_x -= cactus_speed
    if cactus_x < -50:
        cactus_x = width + random.randint(5, 20)
        score += 1

    bird_x -= bird_speed
    if bird_x < -50:
        bird_x = width + random.randint(5, 20)
        bird_y = random.randint(5, 10)

    # 碰撞检测
    if (dino_x + 44 > cactus_x and dino_x < cactus_x + 40
        and dino_y + 47 > cactus_y):
        gameover = True

    if (dino_x + 44 > bird_x and dino_x < bird_x + 30
        and dino_y < bird_y + 20):
        gameover = True

    # 绘制图形
    screen.fill(black)

    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(cactus_img, (cactus_x, cactus_y))
    screen.blit(bird_img, (bird_x, bird_y))

    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (width - 1000, 100))

    if gameover:
        screen.blit(gameover_img, (width / 2 - 5, height / 2 - 5))

    # 更新屏幕
    pygame.display.update()

    # 延时
    time.sleep(0.02)
