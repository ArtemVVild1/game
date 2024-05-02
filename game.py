import time

import pygame

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))  # flags = pygame.NOFRAME - убрать рамку у окна
clock = pygame.time.Clock()
fps = 60
side = {'Right':False,'Left':False}
action_lst = {'Idle':False, 'Attack':False, 'Dead':False, 'Run':False, 'Jump':False, 'Jupm_Throw':False, 'Jump_Attack':False, 'Slide':False, 'Throw':False, }
action_count = {'slide_count':0,'jump_count':10}

class Player(pygame.sprite.Sprite):
    def __init__(self, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'img/Idle__00{str(0)}.png')
        self.rect = self.image.get_rect(x= W/2, bottom=H/2)
        self.jump = False
        self.jump_count = 10
        self.frame = 0

    def update(self, *args) -> None:
        anim_key = 0
        if action_lst['Run']:
            if side['Right']:
                self.rect.x += 5
            elif side['Left']:
                self.rect.x -= 5
            anim_key = 3

        if action_count['slide_count'] and action_lst['Slide']:
            if side['Right']:
                self.rect.x += 25 / 3
            elif side['Left']:
                self.rect.x -= 25 / 3
            action_count['slide_count'] -= 1
            anim_key = 7
        if self.jump:
            if self.jump_count >= -10:
                if self.jump_count < 0:
                    self.rect.y += (self.jump_count ** 2) / 2
                else:
                    self.rect.y -= (self.jump_count ** 2) / 2
            self.jump_count -= 1
        else:
            self.jump = False
            self.jump_count = 10
        if side['Right']:
            self.image = pygame.image.load(
                    f'img/{list(action_lst)[anim_key]}__00{str(int(self.frame))}.png').convert_alpha()
        elif side['Left']:
            self.image = pygame.transform.flip(
                pygame.image.load(f'img/{list(action_lst)[anim_key]}__00{str(int(self.frame))}.png'), 1,
                0).convert_alpha()
            """if self.jump is True:
                if self.jump_count >= -10:
                    if self.jump_count < 0:
                        self.rect.y += (self.jump_count ** 2) // 2
                    else:
                        self.rect.y -= (self.jump_count ** 2) // 2
                self.jump_count -= 1
            else:
                self.jump = False
                self.jump_count = 10"""

            """if action_lst['Run']:
                self.rect.x -= 5
            if args[2] == 7 and self.slide_count:
                self.slide_count += 1
                self.rect.x -= 25 / 3
            if self.jump is True:
                if self.jump_count >= -10:
                    if self.jump_count < 0:
                        self.rect.y += (self.jump_count ** 2) // 2
                    else:
                        self.rect.y -= (self.jump_count ** 2) // 2
                self.jump_count -= 1
            else:
                self.jump = False
                self.jump_count = 10"""

        self.frame += 0.4
        self.frame %= 9

hero = Player()
pygame.display.set_caption('#')  # задать название для окна

while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP:
            action_lst = {i: False for i in action_lst}
            action_lst['Idle'] = True
            anim_key = 0
        if event.type == pygame.KEYDOWN:
            action_lst = {i: False for i in action_lst}
            if event.key == pygame.K_d:
                action_lst['Run'] = True
                side['Right'] = True
                side['Left'] = False
            if event.key == pygame.K_a:
                action_lst['Run'] = True
                side['Left'] = True
                side['Right'] = False
            if event.key == pygame.K_s:
                action_lst['Slide'] = True
                action_count['slide_count'] = 30
            if event.key == pygame.K_w:
                hero.jump = True
                hero.jump_count = 10
            """for i,l in action_lst.items():
                print(i,l)
            print('*'*100)"""

    screen.fill((0, 0, 0))
    hero.update(H, W,)
    screen.blit(hero.image, hero.rect)
    pygame.display.update()
    clock.tick(fps)s)






import time

import pygame

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))  # flags = pygame.NOFRAME - убрать рамку у окна
clock = pygame.time.Clock()
fps = 60
side = {'Right':True,'Left':False}
action_lst = {'Idle':False, 'Attack':False, 'Dead':False, 'Run':False, 'Jump':False, 'Jupm_Throw':False, 'Jump_Attack':False, 'Slide':False, 'Throw':False, }
action_count = {'slide_count':0,'jump_count':0}

class Player(pygame.sprite.Sprite):
    def __init__(self, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'img/Idle__00{str(0)}.png')
        self.rect = self.image.get_rect(x= W/2, bottom=H/2)
        self.jump = False
        self.jump_count = 10
        self.frame = 0

    def update(self, *args) -> None:
        anim_key = 0
        if action_lst['Run']:
            if side['Right']:
                self.rect.x += 5
            elif side['Left']:
                self.rect.x -= 5
            anim_key = 3

        if action_count['slide_count'] and action_lst['Slide']:
            if side['Right']:
                self.rect.x += 25 / 3
            elif side['Left']:
                self.rect.x -= 25 / 3
            action_count['slide_count'] -= 1
            anim_key = 7
        if action_lst['Jump']:
            action_count['jump_count']-=1
            print(action_count['jump_count'])
            if action_count['jump_count']<-1:
                action_lst['Jump'] = False
                action_count['jump_count'] = 0
            if action_count['jump_count'] >= 4:
                self.rect.y-=10
            if action_count['jump_count'] < 4:
                self.rect.y+=10


            """if action_count['jump_count'] >= -20:
                if action_count['jump_count'] < 0:
                    self.rect.y += 10
                else:
                    self.rect.y -= 10
                action_count['jump_count'] -= 1
        else:
            action_lst['Jump'] = False
            action_count['jump_count'] = 0"""
        if side['Right']:
            self.image = pygame.image.load(
                    f'img/{list(action_lst)[anim_key]}__00{str(int(self.frame))}.png').convert_alpha()
        elif side['Left']:
            self.image = pygame.transform.flip(
                pygame.image.load(f'img/{list(action_lst)[anim_key]}__00{str(int(self.frame))}.png'), 1,
                0).convert_alpha()
            """if self.jump is True:
                if self.jump_count >= -10:
                    if self.jump_count < 0:
                        self.rect.y += (self.jump_count ** 2) // 2
                    else:
                        self.rect.y -= (self.jump_count ** 2) // 2
                self.jump_count -= 1
            else:
                self.jump = False
                self.jump_count = 10"""

            """if action_lst['Run']:
                self.rect.x -= 5
            if args[2] == 7 and self.slide_count:
                self.slide_count += 1
                self.rect.x -= 25 / 3
            if self.jump is True:
                if self.jump_count >= -10:
                    if self.jump_count < 0:
                        self.rect.y += (self.jump_count ** 2) // 2
                    else:
                        self.rect.y -= (self.jump_count ** 2) // 2
                self.jump_count -= 1
            else:
                self.jump = False
                self.jump_count = 10"""

        self.frame += 0.4
        self.frame %= 9

hero = Player()
pygame.display.set_caption('#')  # задать название для окна

while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP:
            # action_lst = {i: False for i in action_lst}
            action_lst['Idle'] = True
            anim_key = 0
        if event.type == pygame.KEYDOWN:
            action_lst = {i: False for i in action_lst}
            if event.key == pygame.K_d:
                action_lst['Run'] = True
                side['Right'] = True
                side['Left'] = False
            if event.key == pygame.K_a:
                action_lst['Run'] = True
                side['Left'] = True
                side['Right'] = False
            if event.key == pygame.K_s:
                action_lst['Slide'] = True
                action_count['slide_count'] = 30
            if event.key == pygame.K_w:
                if action_count['jump_count'] == 0 and action_lst['Jump'] is False:
                    action_lst['Jump'] = True
                    action_count['jump_count'] = 8
            """for i,l in action_lst.items():
                print(i,l)
            print('*'*100)"""

    screen.fill((0, 0, 0))
    hero.update(H, W,)
    screen.blit(hero.image, hero.rect)
    pygame.display.update()
    clock.tick(fps)
