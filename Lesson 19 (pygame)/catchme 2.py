import pygame  # не входит в стандартную библиотеку (pip install pygame)
from random import randint
import time

def get_randint(x, y):
    while True:
        n = randint(x, y)
        if n == 0:
            continue
        return n

def print_score(score, x, y, font_color=(0, 0, 0), font_type="PINGPONG.TTF", font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render('Score: ' + str(score), True, font_color)
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
        #self.clear()
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

pygame.display.flip()

time.sleep(2)

clock = pygame.time.Clock()
balls_count = 0
while True:
    display.fill(pygame.Color('white'))
    print_score(balls_count, width - 150, 30)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            for ball in balls:
                if ball.is_poin_in_ball(x, y) and ball.check_position():
                    if not ball.catched:
                        ball.stop()
                        balls_count += 1
                        ball.catch()

                
    for ball in balls:
        ball.move()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)