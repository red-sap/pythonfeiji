import pygame
from plane_sprites import  *


pygame.init()

screen = pygame.display.set_mode((480,700)) #屏幕的大小


bg = pygame.image.load("./images/background.png")

screen.blit(bg,(0,0))  #绘制屏幕的位置

pygame.display.update()
# pygame.display.update()

hero = pygame.image.load("./images/me2.png")

screen.blit(hero,(200,300)) #绘制飞机的位置
pygame.display.update()     #上图






clock = pygame.time.Clock()

hero_rect = pygame.Rect(200,300,102,126) #记录飞机的位置和大小

enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)
enemy_group = pygame.sprite.Group(enemy,enemy1)




while True:
    clock.tick(60)

    #监听事件

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()

    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    #让精灵组调用两个方法
    #update
    enemy_group.update()

    enemy_group.draw(screen)


    pygame.display.update()
    if hero_rect.y == -126:
        hero_rect.y = 700


