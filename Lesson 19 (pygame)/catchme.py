import pygame  # не входит в стандартную библиотеку (pip install pygame)
from random import randint
import time

def get_randint(x, y):
    while True:
        n = randint(x, y)
        if n == 0:
            continue
        return n
    

class Ball:
    def __init__(self, display):
        self.display = display
        self.color = pygame.Color('Red')
        self.center_x = 100
        self.center_y = 100
        self.radius = 30
        
        self.vx = 0
        self.vy = 0

    # Функция расующая шар
    def show(self):
        pygame.draw.circle(self.display, self.color, (self.center_x, self.center_y), self.radius)

    # Очищаем слад шарика
    def clear(self):
        pygame.draw.circle(self.display, pygame.Color('white'), (self.center_x, self.center_y), self.radius)

    # Перемещаем шарик
    def go(self):
        self.center_x += self.vx
        self.center_y += self.vy

    # Рисуем анимацию, объединяя методы класса
    def move(self):
        self.clear()
        self.go()
        self.show()
        
    def stop(self):
        self.vx = 0
        self.vy = 0        


# Создаем класс случайного шара, наследующего класс Ball
# class Название класса(Клас прародитель)
class RandomPointBall(Ball):
    def __init__(self, display):
        # Вначале вызываем конструктор прародителя
        super().__init__(display)
        
        # Затем изменяем необходимые параметры
        width, height = display.get_size()
        self.color = pygame.Color('blue')
        self.center_x = randint(self.radius, width - self.radius)
        self.center_y = randint(self.radius, height - self.radius)

class PointBall(Ball):
    def __init__(self, display, x, y):
        super().__init__(display)
        self.color = pygame.Color('yellow')
        self.center_x = x
        self.center_y = y


class RandomMovingBall(RandomPointBall):
    def __init__(self, display):
        super().__init__(display)

        self.vx = get_randint(-3, 3)
        self.vy = get_randint(-3, 3)





# Инициируем pygame
pygame.init()

width = 700
height = 400
# Создаем окно с заданными размерами (передаем картеж с размерами)
display = pygame.display.set_mode( (width, height) )
# Меняем цвет заливки окна (по умолчанию черный)
display.fill(pygame.Color('white'))

font = pygame.font.Font(None, 35)

balls = []
for i in range(10):
    ball = RandomMovingBall(display)
    ball.show()
    balls.append(ball)

# Обновляем экран. Иначе не применятся изменения сделанные выше и будет черный экран
pygame.display.flip()

time.sleep(2)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        # Обрабатываем событие закрытия окна (нажатие на кнопку закрытия)
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #x = event.pos[0]
            #y = event.pos[1]
            #ball = PointBall(display, x, y)
            # ball.show()
            balls_count = 0
            for ball in balls:
                ball.stop()
                if ball.center_x > ball.radius and ball.center_x < width - ball.radius:
                    if ball.center_y > ball.radius and ball.center_y < height - ball.radius:
                        balls_count += 1
            text = font.render('Шаров на поле: ' + str(balls_count), True, pygame.Color('black'))
            display.blit(text, [40, 40])

                
    for ball in balls:
        ball.move()
    pygame.display.flip()
    clock.tick(60)