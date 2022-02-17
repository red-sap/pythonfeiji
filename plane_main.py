import pygame
import plane_sprites


class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(plane_sprites.SCEEEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(plane_sprites.CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(plane_sprites.HERO_FIRE_EVENT,500)
    def __create_sprites(self):
        bg1 = plane_sprites.secrren_role()
        bg2 = plane_sprites.secrren_role(isrole=True)
        # bg2.rect.y = -plane_sprites.SCEEEN_RECT.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = plane_sprites.Hero()
        self.hero_group =pygame.sprite.Group(self.hero)




    def start_game(self):
        print("开始游戏")
        while True:
            self.clock.tick(plane_sprites.FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()



    def __event_handler(self):
        for i in pygame.event.get():
            if i.type ==pygame.QUIT:
                PlaneGame.game_over()
            elif i.type == plane_sprites.CREATE_ENEMY_EVENT:
                enemy = plane_sprites.enemy_role()
                self.enemy_group.add(enemy)
            elif i.type == plane_sprites.HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT] :
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0


    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True )
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies) > 0 :
            self.hero.kill()
            PlaneGame.game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)


    @staticmethod
    def game_over():
        print("游戏结束")
        pygame.quit()
        exit()




if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()

