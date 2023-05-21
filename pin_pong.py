
from pygame import *
font.init()
from random import *
font1 = font.SysFont('Arial', 36)
window = display.set_mode((700, 500))
display.set_caption("пин ронг")
background = transform.scale(image.load("fon.jpg"), (700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 480:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed
lost_1 = 0
lost_2 = 0
roket1 = Player("roket.png", 20, 250, 70, 140, 6)
roket2 = Enemy("roket.png", 590, 250, 70, 140, 6)
ball = GameSprite('ball.jpg', 200, 200, 50, 50, 5)
popitka = 1

game = True
clock = time.Clock()
FPS = 60

#mixer.music.play()
speed = 10
speed_x = 3
speed_y = 3
finish = False
font = font.SysFont('Arial', 70)
lose_r = font.render('Player2 LOST!', True, (255, 215, 0))
lose_l = font.render('Player1 LOST!', True, (255, 215, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                if finish == True:
                    lost = 0
                    popitka = popitka + 1
    if finish != True:
        window.blit(background,(0,0))
        # if sprite.collide_rect(vrag, bullet):
        #     window.blit(win, (200, 200))
        #     finish = True
    #         money.play()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 480 or ball.rect.y < 0:
                speed_y *= -1
        if sprite.collide_rect(roket1, ball) or sprite.collide_rect(roket2, ball):
            
            speed_x *= -1
        # text_try = font1.render("Попытка:" + str(popitka), 1, (255, 255, 255))
        # window.blit(text_try, (0, 100)) 
        
        #   money.play()
        ball.recet()
        roket1.update()
        roket1.recet()
        roket2.update()
        roket2.recet()
        # bullets.update()
        # monsters.update()
        # player.recet()
        if ball.rect.x < -10:
            lost_1 = lost_1 +1
        if lost_1 >= 1:
            window.blit(lose_l, (200, 200))
            finish = True
        if ball.rect.x > 700:
            lost_2 = lost_2 +1
        if lost_2 >= 1:
            window.blit(lose_r, (200, 200))
            finish = True
        
    


    display.update()
    clock.tick(FPS)









