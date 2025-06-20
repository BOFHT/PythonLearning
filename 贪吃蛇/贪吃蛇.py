from os import system
import random
from click import pause
import pygame




snake_list=[[100,100]]
rect_snake_restlist=[]
rect_snake_head=[]
food_point=[20,20]
rect_food=[]
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("贪吃蛇小游戏")
font = pygame.font.SysFont('msyh.ttc', 36)  # 新增字体对象

score = 0  # 新增分数变量

running =True
moveRight=False
moveLeft=False
moveUp=False
moveDown=True

snake_speed = 70
move_accumulator = 0

while running:
    screen.fill([255,255,255])
    clk = clock.tick(60)
    move_accumulator += clk

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveRight=True
                moveLeft=False
                moveUp=False
                moveDown=False
            if event.key == pygame.K_LEFT:
                moveRight=False
                moveLeft=True
                moveUp=False
                moveDown=False
            if event.key == pygame.K_UP:
                moveRight=False
                moveLeft=False
                moveUp=True
                moveDown=False
            if event.key == pygame.K_DOWN:
                moveRight=False
                moveLeft=False
                moveUp=False
                moveDown=True
    if move_accumulator >= snake_speed:
        move_accumulator -= snake_speed

        for i in range(len(snake_list)-1,0,-1):
            snake_list[i][0]=snake_list[i-1][0]
            snake_list[i][1]=snake_list[i-1][1]
        if moveRight:
            snake_list[0][0] += 10
        if moveLeft:
            snake_list[0][0] -= 10
        if moveUp:
            snake_list[0][1] -= 10
        if moveDown:
            snake_list[0][1] += 10

    rect_snake_restlist.clear()
    for snake_point in snake_list:
        if snake_point==snake_list[0]:
            rect_snake_head=pygame.draw.circle(screen,[255,0,0],snake_point,5,0)
        else:
            rect_snake_restlist.append(pygame.draw.circle(screen,[255,0,0],snake_point,5,0))

    rect_food=pygame.draw.circle(screen,[255,0,0],food_point,15,0)

    # 计分板
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if rect_snake_head.colliderect(rect_food):
        snake_list.append([-1,-1])
        food_point=[random.randint(0,500),random.randint(0,500)]
        rect_food=pygame.draw.circle(screen,[255,0,0],food_point,15,0)
        score += 1  # 吃到食物加分

    if snake_list[0] in snake_list[1:]:
        running = False
    if snake_list[0][0]>500 or snake_list[0][0]<0 or snake_list[0][1]>500 or snake_list[0][1]<0:
        running = False
    pygame.display.update()


# 游戏结束虚化处理

bg = screen.copy()
# 2. 缩小再放大多次，达到虚化效果
for i in range(3):
    bg = pygame.transform.smoothscale(bg, (100, 100))
    bg = pygame.transform.smoothscale(bg, (500, 500))
# 3. 重新绘制虚化画面
screen.blit(bg, (0, 0))

# 游戏结束弹窗
gameover_text = font.render("GameOver!", True, (255, 0, 0))
score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
screen.blit(gameover_text, (100, 200))
screen.blit(score_text, (170, 250))
pygame.display.update()

# 等待用户操作
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            waiting = False

pygame.quit()

