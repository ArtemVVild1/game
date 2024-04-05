import pygame

pygame.init()
W, H = 1200, 840
screen = pygame.display.set_mode((W, H))  # flags = pygame.NOFRAME - убрать рамку у окна
clock = pygame.time.Clock()
fps = 60


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = 0
        self.dy = 0
        self.jump = False  # 0
        self.jump_count = 10
        self.slide = False  # 0
        self.walk = False  # 0
        self.right = False  # 0
        self.left = False  # 0
        self.frame = 0

    def update(self, *args) -> None:
        key = pygame.key.get_pressed()
        lst_png = ['000.png', '001.png', '002.png', '003.png', '004.png', '005.png',
                   '006.png', '007.png', '008.png', '009.png', ]

        if key[pygame.K_d]:
            self.rect.x += 3
            self.right = True
            self.image = pygame.image.load(f'hero/Movement/Run_right/Run__{lst_png[int(self.frame)]}')

        if key[pygame.K_a]:
            self.rect.x -= 3
            self.left = True
            self.image = pygame.image.load(f'hero/Movement/Run_left/Run__{lst_png[int(self.frame)]}')
        self.frame += 0.5
        self.frame %= 9

        if key[pygame.K_s]:
            self.slide = True
            if self.right:
                self.rect.x += 5
                self.image = pygame.image.load(f'hero/Movement/Slide/Slide__{lst_png[int(self.frame)]}')
            if self.left:
                self.rect.x -= 5
                self.image = pygame.image.load(f'hero/Movement/Slide/Slide_ls__{lst_png[int(self.frame)]}')
            self.frame += 0.6
            self.frame %= 9

        if key[pygame.K_w]:
            self.jump = True
            if self.right:
                self.rect.x += 3
                self.image = pygame.image.load(f'hero/Movement/Jump/Jump__{lst_png[int(self.frame)]}')
            if self.left:
                self.rect.x -= 3
                self.image = pygame.image.load(f'hero/Movement/Jump/Jump_ls__{lst_png[int(self.frame)]}')
            self.frame += 0.2
            self.frame %= 9

            if self.jump_count >= -10:
                if self.jump_count < 0:
                    self.rect.y += (self.jump_count ** 2) // 2
                else:
                    self.rect.y -= (self.jump_count ** 2) // 2
                self.jump_count -= 1

            else:
                self.jump = False
                self.jump_count = 10

        """else:
            self.rect.y = H-self.rect.h
            self.frame+=0.2
            self.image = pygame.image.load(f'hero/Movement/Staing/Idle__{lst_png[int(self.frame)]}')"""


"""if self.walk:

elif self.slide:
    self.dy = self.rect.y
    self.image = pygame.image.load('hero/Movement/Slide/Slide__' + pers[int(self.frame)]).convert_alpha()
"""

hero = Object(30, 800, 'hero/Movement/Staing/Idle__000.png')
pygame.display.set_caption('#')  # задать название для окна
# background = pygame.image.load('background/Background.png')
# bg_x = 0
# bg_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYUP:
            hero.stay = True  # 1
            hero.right = False
            hero.left = False  # 0

    screen.fill((255, 255, 255))
    hero.update(W, H)
    screen.blit(hero.image, hero.rect)
    pygame.display.update()
    clock.tick(fps)
