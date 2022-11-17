''' Первый танк целится и стреляет  мышкой, ездит на a, d. Смена снарядов на пробел.
    Второй танк целится на 9, 0. Стреляет на стрелочку вниз. Ездит на стрелочки. Смена снарядов на стрелочку вверх.'''

import math
from random import choice, randint

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx
        self.vy -= 4
        self.y -= self.vy

        if self.x >= (800 - self.r):
            self.x = self.x - self.vx
            self.vx = self.vx * -1
        if self.y >= (600 - self.r):
            self.y = self.y + self.vy
            if abs(self.vy + self.vx) > 5:
                self.vy = self.vy * -0.7
                self.vx = self.vx * 0.7
            else:
                balls.remove(self)

        if self.x <= (0 + self.r):
            self.x = self.x - self.vx
            self.vx = self.vx * -1





    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (obj.r + self.r) > (((obj.x - self.x)**2 + (obj.y - self.y)**2)**0.5):
            #print(obj.r,self.r,((obj.x - self.x)**2 + (obj.y - self.y)**2)**0.5)
            return True
        else:
            #print(obj.r,self.r,((obj.x - self.x)**2 + (obj.y - self.y)**2)**0.5)
            return False


class Ball2(Ball):
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.r >= 100:
            self.r += 1
            if self.r > 110:
                balls.remove(self)
        else:
            self.x += self.vx
            self.vy -= 4
            self.y -= self.vy

            if self.vy < 0:
                self.r = 100
                self.color = YELLOW



            if self.x >= (800 + self.r):
                self.x = self.x - self.vx
                self.vx = self.vx * -1
            if self.y >= (600 + self.r):
                self.y = self.y + self.vy
                self.vy = self.vy * -1
            if self.x < 0:
                balls.remove(self)


class Ball3(Ball):
    def move(self):
        if self.r >= 100:
            self.r += 1
            if self.r > 110:
                balls.remove(self)
        else:
            self.x += self.vx
            self.vy -= 4
            self.y -= self.vy

            if self.x >= (800 - self.r):
                self.x = self.x - self.vx
                self.vx = self.vx * -1
            if self.y >= (600 - self.r):
                self.y = self.y + self.vy
                if abs(self.vy + self.vx) > 5:
                    self.vy = self.vy * -0.7
                    self.vx = self.vx * 0.7
                else:
                    self.r = 100
                    self.color = 0xffa500


        if self.x <= (0 + self.r):
            self.x = self.x - self.vx
            self.vx = self.vx * -1

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 40
        self.y = 580
        self.bul = 1
        self.r = 5

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        if self.bul == 1:
            new_ball = Ball(self.screen, self.x, self.y)
        else:
            new_ball = Ball2(self.screen, self.x, self.y)

        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.an = -math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = -math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(
            self.screen,
            self.color,
            [self.x, self.y],
            [self.x + self.f2_power * math.cos(self.an) , self.y - self.f2_power * math.sin(self.an)],
            5)
        pygame.draw.rect(
            self.screen,
            (46, 87, 201),
            [self.x - 20,
            self.y,
            40,
            20]
        )
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

class Gun2(Gun):
    def targetting(self, event):
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        if self.bul == 1:
            new_ball = Ball(self.screen, self.x, self.y)
        else:
            new_ball = Ball2(self.screen, self.x, self.y)

        new_ball.r += 5
        #self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        #self.an = -math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))
    def draw(self):
        pygame.draw.line(
            self.screen,
            self.color,
            [self.x, self.y],
            [self.x + self.f2_power * math.cos(self.an) , self.y - self.f2_power * math.sin(self.an)],
            5)
        pygame.draw.rect(
            self.screen,
            (200, 5, 55),
            [self.x - 20,
            self.y,
            40,
            20]
        )

class Target:
    def __init__(self, screen):
        self.points = 0
        self.live = 1
        self.screen = screen
        self.x = 600
        self.y = 300
        self.r = 19
        self.color = RED
        self.f = 0.0
        self.dv = -40
        self.d = 1
        # FIXME: don't work!!! How to call this functions when object is created?
        # self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(200, 600)
        y = self.y = randint(100, 550)
        r = self.r = randint(25, 35)
        color = self.color = RED
        self.live = 1
        self.dv = randint(-50, 50)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (self.x, self.y),
            self.r,
            1
        )
        #self.f += 0.05
        #self.x += 1 * math.cos(self.f)
        #self.y += 1 * math.sin(self.f)
        if (self.dv > 50):
            self.d = -1
        if (self.dv < -50):
            self.d = 1
        self.dv += self.d
        self.x += self.d





class Target2(Target):
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (self.x, self.y),
            self.r,
            1
        )
        # self.f += 0.05
        # self.x += 1 * math.cos(self.f)
        # self.y += 1 * math.sin(self.f)
        if (self.dv > 50):
            self.d = -1
        if (self.dv < -50):
            self.d = 1
        self.dv += self.d
        self.y += self.d
        b = randint(1, 200)
        if b == 7:
            new_ball = Ball3(self.screen, self.x, self.y + self.r + 6)
            new_ball.r += 5

            new_ball.vx = 0
            new_ball.vy = -5
            balls.append(new_ball)





pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []

f1 = pygame.font.Font(None, 30)


clock = pygame.time.Clock()

gun = Gun(screen)
gun2 = Gun2(screen)
konecs = False
koneck = False


for i in range(3):
    targets.append(Target(screen))

targets.append(Target2(screen))

finished = False

while not finished:
    screen.fill(WHITE)
    # очки
    k = 0
    for i in targets:
        k += i.points
    text1 = f1.render(str(k), True,
                      (180, 180, 180))
    screen.blit(text1, (10, 10))

    if konecs == True:
        text2 = f1.render('Синий проиграл', True,
                          (180, 180, 180))
        screen.blit(text2, (270, 300))
    if koneck == True:
        text3 = f1.render('Красный  проиграл', True,
                          (180, 180, 180))
        screen.blit(text3, (270, 270))

    gun.draw()
    gun2.draw()
    for i in range(len(targets)):
        targets[i].draw()

    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_d):
                gun.x += 5
            elif (event.key == pygame.K_a):
                gun.x -= 5
            elif (event.key == pygame.K_SPACE):
                gun.bul = gun.bul * -1

            elif (event.key == pygame.K_RIGHT):
                gun2.x += 5
            elif (event.key == pygame.K_LEFT):
                gun2.x -= 5
            elif (event.key == pygame.K_UP):
                gun2.bul = gun2.bul * -1

            elif (event.key == pygame.K_DOWN):
                gun2.fire2_start(event)
            elif (event.key == pygame.K_0):
                gun2.targetting(event)
                gun2.an = gun2.an - 0.15
            elif (event.key == pygame.K_9):
                gun2.targetting(event)
                gun2.an = gun2.an + 0.15
        elif (event.type == pygame.KEYUP):
            if (event.key == pygame.K_DOWN):
                gun2.fire2_end(event)


    for b in balls:
        b.move()

        if b.hittest(gun2):
            koneck = True
        if b.hittest(gun):
            konecs = True
        for target in targets:
            if b.hittest(target) and target.live:
                target.live = 0
                target.hit()
                target.new_target()

    gun.power_up()
    gun2.power_up()

pygame.quit()
