from aetypes import Property

from pygame import *
import random

class Sprite(object):
    '''Base class for sprite objects'''
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
        
class Bike(Sprite):
    FLEXIBILITY = 10

    def __init__(self, xpos=320, ypos=400, filepath='data/player.png'):
        Sprite.__init__(self, xpos, ypos, filepath)
        self._speed = 1

    def get_keyboard_event(self, ourevent):
        if ourevent.type == KEYDOWN:
            if ourevent.key == K_RIGHT and self.x < 500: #Road.get_right_border(road):
                self.x += self.FLEXIBILITY
            if ourevent.key == K_LEFT and self.x > 100: #Road.get_left_border(road):
                self.x -= self.FLEXIBILITY

    @property
    def speed(self):
        if self._speed < 50:
            self._speed += 0.1
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed




class Enemy(Sprite):
    def __init__(self, xpos, ypos, filepath):
        Sprite.__init__(self, xpos, ypos, filepath)

class Road():
    RIGHT_BORDER = 500
    LEFT_BORDER = 100
    def get_right_border(self):
        return self.RIGHT_BORDER
    def get_left_border(self):
        return self.LEFT_BORDER


def Intersect(s1_x, s1_y, s2_x, s2_y):
    if (s1_x > s2_x - 40) and (s1_x < s2_x + 40) and (s1_y > s2_y -
        40) and (s1_y < s2_y + 40):
        return 1
    else:
        return 0

def main():
    key.set_repeat(1, 1)
    road = Road()
    player = Bike()
    enemy = Enemy(random.randrange(100, 500), 0, 'data/enemy.png')
    tree1 = Sprite(10, 0, 'data/tree.png')
    tree2 = Sprite(550, 240, 'data/tree.png')
    whiteline1 = Sprite(315, 0, 'data/whiteline.png')
    whiteline2 = Sprite(315, 240, 'data/whiteline.png')
    scorefont = font.Font(None, 60)
    score = 0
    maxscore = 0
    quit = 0
    #Main cycle:
    while quit == 0:
        #======Screen
        screen.fill((0,200,0))
        screen.fill((200,200,200), ((100, 0), (440, 480)))
        
        #------------TREES
        tree1.render()
        tree1.y += player.speed
        if (tree1.y > 480):
            tree1.y = -110
        tree2.render()
        tree2.y += player.speed
        if (tree2.y > 480): 
            tree2.y = -110
        #=======Whiteline
        whiteline1.render()
        whiteline1.y += player.speed
        if (whiteline1.y > 480):
            whiteline1.y = -80
        whiteline2.render()
        whiteline2.y += player.speed
        if (whiteline2.y > 480):
            whiteline2.y = -80
        #----------ENEMIES--------------
        enemy.render()
        enemy.y += 5
        if (enemy.y > 480):
            enemy.y = -100
            enemy.x = random.randrange(100, 500)

        #----------SCORE----------------------        
        scoretext = scorefont.render('Score: ' + str(score), 
                                     True, (255,255,255), (0,0,0))
        screen.blit(scoretext, (5, 5))
        speedtext = scorefont.render('Speed: ' + str(player.speed),
                                     True, (255,255,255), (0,0,0))
        screen.blit(speedtext, (300, 5))
        
        #----------Intersections----------------------
        if (Intersect(player.x, player.y, enemy.x, enemy.y)):
#            mixer.Sound.play(crasheffect)
            if (score > maxscore):
                maxscore = score
                score = 0
            player.speed=1
                
        #------------Events---------------
        for ourevent in event.get():
            if ourevent.type == QUIT:
                quit = 1
            player.get_keyboard_event(ourevent)
        #----------------------------------
        player.render()
        display.update()
        time.delay(10)
        
        #----------SCORE COUNTER=-------------------
        score += 1
    print 'Your maximum score was:', maxscore

init()
screen = display.set_mode((640,480))
display.set_caption('Moto')
main()