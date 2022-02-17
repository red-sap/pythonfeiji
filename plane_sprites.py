import random
import pygame
SCEEEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

FRAME_PER_SEC = 60
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed =1 ):
        super(GameSprite,self).__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()


        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class secrren_role(GameSprite):
    def __init__(self, isrole=False):
        super().__init__("./images/background.png")
        if isrole:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCEEEN_RECT.height:
            self.rect.y = -self.rect.height


class enemy_role(GameSprite):
    def __init__(self):
        super(enemy_role, self).__init__("./images/enemy1.png")
        self.speed =random.randint(1,3)
        self.rect.y = -self.rect.height
        max_x = SCEEEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)
    def update(self):
        super(enemy_role, self).update()
        if self.rect.y  >= SCEEEN_RECT.height:
            #print("delete")
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        super(Hero, self).__init__("./images/me1.png",speed=0)
        self.rect.centerx = SCEEEN_RECT.centerx
        self.rect.bottom = SCEEEN_RECT.bottom -120
        self.bullets = pygame.sprite.Group()
        
    def update(self):
        self.rect.x  += self.speed
        if self.rect.x < 0 :
            self.rect.x = 0
        elif self.rect.right > SCEEEN_RECT.width:
            self.rect.right = SCEEEN_RECT.width


    def fire(self):
        print("1")
        for j in (0,1.2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - j * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)

class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super(Bullet, self).__init__("./images/bullet1.png", -2)




    def update(self):
        super(Bullet, self).update()
        if self.rect.bottom < 0 :
            self.kill()
        pass
    

