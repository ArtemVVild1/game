import pygame

pygame.init()
W, H = 1200, 840
screen = pygame.display.set_mode((W, H))  # flags = pygame.NOFRAME - убрать рамку у окна
clock = pygame.time.Clock()
fps = 60
action_lst = ['Idle', 'Attack', 'Dead', 'Run', 'Jump', 'Jupm_Throw', 'Jump_Attack', 'Slide', 'Throw', ]
action = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'img/sprite/{action_lst[action]}__00{str(0)}.png')
        self.rect = self.image.get_rect(x=500, bottom=H)
        self.jump = False
        self.jump_count = 10
        self.slide_count = 0
        self.right = False  # 0
        self.left = False  # 0
        self.frame = 0

    def update(self, *args) -> None:
        if self.right:
            self.image = pygame.image.load(
                f'img/sprite/{action_lst[action]}__00{str(int(self.frame))}.png').convert_alpha()
            if args[2] == 3:
                self.rect.x += 5
            if args[2] == 7 and self.slide_count:
                self.slide_count -= 1
                self.rect.x += 25 / 3
            if self.jump is True:
                if self.jump_count >= -10:
                    if self.jump_count < 0:
                        self.rect.y += (self.jump_count ** 2) // 2
                    else:
                        self.rect.y -= (self.jump_count ** 2) // 2
                self.jump_count -= 1
            else:
                self.jump = False
                self.jump_count = 10
        elif self.left:
            self.image = pygame.transform.flip(
                pygame.image.load(f'img/sprite/{action_lst[action]}__00{str(int(self.frame))}.png'), 1,
                0).convert_alpha()
            if args[2] == 3:
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
                self.jump_count = 10
        else:
            self.rect.bottom = H
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
            action = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                hero.right = True
                hero.left = False
                action = 3
            if event.key == pygame.K_a:
                hero.left = True
                hero.right = False
                action = 3
            if event.key == pygame.K_s:
                hero.slide_count = 30
                action = 7
            if event.key == pygame.K_w:
                hero.jump = True
                hero.jump_count = 10
                action = 4
            if event.key == pygame.K_SPACE:
                action = 1
            if event.key == pygame.K_q:
                action = 8


    screen.fill((0, 0, 0))
    hero.update(H, W, action)
    screen.blit(hero.image, hero.rect)
    pygame.display.update()
    clock.tick(fps)
