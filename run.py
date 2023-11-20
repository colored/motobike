import pygame
import random

# Initialize pygame
pygame.init()

# Base class for sprite objects
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)

    def render(self, screen):
        screen.blit(self.bitmap, (self.x, self.y))

class Bike(Sprite):
    FLEXIBILITY = 1

    def __init__(self, xpos=320, ypos=400, filepath='data/player.png'):
        super().__init__(xpos, ypos, filepath)
        self._speed = 1

    def get_keyboard_event(self, ourevent):
        if ourevent.type == pygame.KEYDOWN:
            if ourevent.key == pygame.K_RIGHT and self.x < Road.RIGHT_BORDER:
                self.x += self.FLEXIBILITY
            elif ourevent.key == pygame.K_LEFT and self.x > Road.LEFT_BORDER:
                self.x -= self.FLEXIBILITY

    @property
    def speed(self):
        return min(self._speed + 0.1, 50)

    @speed.setter
    def speed(self, value):
        self._speed = value

class Enemy(Sprite):
    def __init__(self, xpos, ypos, filepath):
        super().__init__(xpos, ypos, filepath)

class Road:
    RIGHT_BORDER = 500
    LEFT_BORDER = 100

def intersect(s1_x, s1_y, s2_x, s2_y):
    return (s1_x > s2_x - 40) and (s1_x < s2_x + 40) and (s1_y > s2_y - 40) and (s1_y < s2_y + 40)

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Moto')

    key = pygame.key
    key.set_repeat(1, 1)

    road = Road()
    player = Bike()
    enemy = Enemy(random.randrange(Road.LEFT_BORDER, Road.RIGHT_BORDER), 0, 'data/enemy.png')
    tree1 = Sprite(10, 0, 'data/tree.png')
    tree2 = Sprite(550, 240, 'data/tree.png')
    whiteline1 = Sprite(315, 0, 'data/whiteline.png')
    whiteline2 = Sprite(315, 240, 'data/whiteline.png')

    scorefont = pygame.font.Font(None, 60)
    score, maxscore, quit_game = 0, 0, False

    # Main cycle
    while not quit_game:
        screen.fill((0, 200, 0))
        screen.fill((200, 200, 200), ((100, 0), (440, 480)))

        # Rendering trees
        for tree in [tree1, tree2]:
            tree.render(screen)
            tree.y += player.speed
            if tree.y > 480:
                tree.y = -110

        # Rendering white lines
        for whiteline in [whiteline1, whiteline2]:
            whiteline.render(screen)
            whiteline.y += player.speed
            if whiteline.y > 480:
                whiteline.y = -80

        # Handling enemy
        enemy.render(screen)
        enemy.y += 5
        if enemy.y > 480:
            enemy.y = -100
            enemy.x = random.randrange(Road.LEFT_BORDER, Road.RIGHT_BORDER)

        # Displaying score and speed
        scoretext = scorefont.render(f'Score: {score}', True, (255, 255, 255), (0, 0, 0))
        speedtext = scorefont.render(f'Speed: {player.speed:.1f}', True, (255, 255, 255), (0, 0, 0))
        screen.blit(scoretext, (5, 5))
        screen.blit(speedtext, (300, 5))

        # Collision detection
        if intersect(player.x, player.y, enemy.x, enemy.y):
            maxscore = max(score, maxscore)
            score = 0
            player.speed = 1

        # Event handling
        for ourevent in pygame.event.get():
            if ourevent.type == pygame.QUIT:
                quit_game = True
            player.get_keyboard_event(ourevent)

        player.render(screen)
        pygame.display.update()
        pygame.time.delay(10)

        score += 1

    print(f'Your maximum score was: {maxscore}')

if __name__ == '__main__':
    main()
