from pygame import *
import random

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
        
#class Bike(Sprite):
#    def get_keyboard_event(self):
#        pass
        
def Intersect(s1_x, s1_y, s2_x, s2_y):
    if (s1_x > s2_x - 40) and (s1_x < s2_x + 40) and (s1_y > s2_y -
        40) and (s1_y < s2_y + 40):
        return 1
    else:
        return 0

def main():
    RIGHT_BORDER = 500
    LEFT_BORDER = 100
    BIKE_HORISONTAL_SPEED = 10
    BIKE_SPEED = 15
    key.set_repeat(1, 1)
    player = Sprite(20, 400, 'data/player.png')
    enemy = Sprite(random.randrange(100, 500), 0, 'data/enemy.png')
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
        screen.fill((0,200,0))
        screen.fill((200,200,200), ((100, 0), (440, 480)))
        tree1.render()
        tree1.y += 10
        if (tree1.y > 480):
            tree1.y = -110
        tree2.render()
        tree2.y += 10
        if (tree2.y > 480): 
            tree2.y = -110
        whiteline1.render()
        whiteline1.y += 10
        if (whiteline1.y > 480):
            whiteline1.y = -80
        whiteline2.render()
        whiteline2.y += 10
        if (whiteline2.y > 480):
            whiteline2.y = -80
        enemy.render()
        enemy.y += 15
        if (enemy.y > 480):
            enemy.y = -100
            enemy.x = random.randrange(100, 500)
#        x, y = mouse.get_pos()
#        if (x < 100):
#            x = 100
#        if (x > 500):
#            x = 500
#        player.x = x
        
        scoretext = scorefont.render('Score: ' + str(score), 
                                     True, (255,255,255), (0,0,0))
        screen.blit(scoretext, (5,5))
        if (Intersect(player.x, player.y, enemy.x, enemy.y)):
#            mixer.Sound.play(crasheffect)
            if (score > maxscore):
                maxscore = score
                score = 0
        
        for ourevent in event.get():
            if ourevent.type == QUIT:
                quit = 1
            if ourevent.type == KEYDOWN:
                if ourevent.key == K_RIGHT and player.x < RIGHT_BORDER:
                    player.x += BIKE_HORISONTAL_SPEED
                if ourevent.key == K_LEFT and player.x > LEFT_BORDER:
                    player.x -= BIKE_HORISONTAL_SPEED
        player.render()

        display.update()
        time.delay(BIKE_SPEED)
        score += 1
    print 'Your maximum score was:', maxscore

init()
screen = display.set_mode((640,480))
display.set_caption('Moto')
main()