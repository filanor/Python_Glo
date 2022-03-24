import pygame  # не входит в стандартную библиотеку (pip install pygame)
from random import randint
import time

score = {
    "left": 0,
    "top": 0,
    "right": 0,
    "bottom": 0
}


def get_randint(x, y):
    while True:
        n = randint(x, y)
        if n == 0:
            continue
        return n

def print_score(score, x, y, font_color=(0, 0, 0), font_type="PINGPONG.TTF", font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render('a' + str(score), True, font_color)
    display.blit(text, (x, y))
    


class Ball:
    def __init__(self, display):
        self.display = display
        self.color = pygame.Color('Red')
        self.center_x = 100
        self.center_y = 100
        self.radius = 30
        self.catched = False
        
        self.vx = 0
        self.vy = 0
        
        
    def catch(self):
        self.catched = True

    def show(self):
        pygame.draw.circle(self.display, self.color, (self.center_x, self.center_y), self.radius)

    def clear(self):
        pygame.draw.circle(self.display, pygame.Color('white'), (self.center_x, self.center_y), self.radius)

    def go(self):
        self.center_x += self.vx
        self.center_y += self.vy
        
    def move(self):
        # self.clear()
        self.go()
        self.show()
        
    def stop(self):
        self.vx = 0
        self.vy = 0
        
    def check_position(self):
        if self.center_x > self.radius and self.center_x < width - self.radius:
            if self.center_y > self.radius and self.center_y < height - self.radius:
                return True
        return False

    def is_poin_in_ball(self, x, y):
        if (self.center_x - x) ** 2 + (self.center_y - y) ** 2 <= self.radius ** 2:
            return True
        return False
    
    
class RandomPointBall(Ball):
    def __init__(self, display):
        super().__init__(display)
        width, height = display.get_size()
        self.color = pygame.Color('green')
        self.center_x = randint(self.radius, width - self.radius)
        self.center_y = randint(self.radius, height - self.radius)
        
        
class RandomMovingBall(RandomPointBall):
    def __init__(self, display):
        super().__init__(display)

        self.vx = get_randint(-3, 3)
        self.vy = get_randint(-3, 3)


class BillyardBall(RandomMovingBall):
    def __init__(self, display):
        super().__init__(display)
        self.color = pygame.Color('red')
        
        
    def go(self):
        super().go()

        width, height = self.display.get_size()
        if self.center_x <= self.radius:
            score["left"] += 1
            self.vx = -self.vx
        elif self.center_x >= width - self.radius:
            score["right"] += 1
            self.vx = -self.vx
        elif self.center_y <= self.radius:
            score["top"] += 1
            self.vy = -self.vy
        elif self.center_y >= height - self.radius:
            score["bottom"] += 1
            self.vy = -self.vy

pygame.init()
width = 700
height = 400
display = pygame.display.set_mode((width, height))
display.fill(pygame.Color('white'))

font = pygame.font.Font(None, 35)

balls = []
for i in range(10):
    ball = RandomMovingBall(display)
    ball.show()
    balls.append(ball)
    billyardBall = BillyardBall(display)
    billyardBall.show()
    balls.append(billyardBall)

pygame.display.flip()

time.sleep(2)

clock = pygame.time.Clock()
balls_count = 0
while True:
    display.fill(pygame.Color('white'))
    print_score(score["left"], 20, 190)
    print_score(score["top"], 340, 20)
    print_score(score["right"], width - 50, 190)
    print_score(score["bottom"], 340, height - 50)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

                
    for ball in balls:
        ball.move()
    pygame.display.flip()
    clock.tick(60)