import pygame
import random

pygame.init()

# 視窗設定
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("貪吃蛇")

# 顏色
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 貪吃蛇設定
block_size = 20
snake_pos = [[100, 100]]  # 初始位置
snake_dir = "RIGHT"
snake_speed = 5  # 每秒移動格數

# 食物設定
food_pos = [random.randrange(0, WIDTH//block_size)*block_size,
            random.randrange(0, HEIGHT//block_size)*block_size]

# 遊戲控制
FPS = 30
clock = pygame.time.Clock()
running = True
frame_counter = 0  # 記錄幀數

while running:
    clock.tick(FPS)
    frame_counter += 1

    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dir != "RIGHT":
                snake_dir = "LEFT"
            if event.key == pygame.K_RIGHT and snake_dir != "LEFT":
                snake_dir = "RIGHT"
            if event.key == pygame.K_UP and snake_dir != "DOWN":
                snake_dir = "UP"
            if event.key == pygame.K_DOWN and snake_dir != "UP":
                snake_dir = "DOWN"

    # 控制蛇移動速度
    if frame_counter >= FPS // snake_speed:
        frame_counter = 0

        # 移動蛇身
        head_x, head_y = snake_pos[-1]
        if snake_dir == "LEFT":
            head_x -= block_size
        if snake_dir == "RIGHT":
            head_x += block_size
        if snake_dir == "UP":
            head_y -= block_size
        if snake_dir == "DOWN":
            head_y += block_size
        snake_pos.append([head_x, head_y])

        # 吃到食物
        if head_x == food_pos[0] and head_y == food_pos[1]:
            food_pos = [random.randrange(0, WIDTH//block_size)*block_size,
                        random.randrange(0, HEIGHT//block_size)*block_size]
        else:
            snake_pos.pop(0)

        # 撞到自己或牆壁 → 結束
        if [head_x, head_y] in snake_pos[:-1] or \
           head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            running = False

    # 畫面更新
    win.fill(BLACK)
    for block in snake_pos:
        pygame.draw.rect(win, GREEN, (block[0], block[1], block_size, block_size))
    pygame.draw.rect(win, RED, (food_pos[0], food_pos[1], block_size, block_size))
    pygame.display.update()

pygame.quit()