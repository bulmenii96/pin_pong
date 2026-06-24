import pygame
from random import *
pygame.init()
 
class Hitbox(): 
    def __init__(self, screen, x, y, width, height, color, weight):
        self.screen = screen
 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
 
        if weight < 0:
            weight = 1
        self.weight = int(weight)
 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def drow_hitbox(self):
        pygame.draw.rect(self.screen,self.color, self.rect, self.weight )
    
    def fill(self):
        pygame.draw.rect(self.screen,self.color, self.rect)
 
    def is_clicked(self,click_position):
        return self.rect.collidepoint(click_position[0],click_position[1])
 
class Pictures(Hitbox):
    def __init__(self, screen, x, y, width, height, color, weight, image_path):
        Hitbox.__init__(self, screen, x, y, width, height, color, weight)
        self.image_path = image_path
        self.set_picture()
 
    def set_picture(self):
        if self.image_path.lower().endswith('.png'):
            self.image = pygame.transform.scale(pygame.image.load(self.image_path).convert_alpha(), (self.width, self.height))
        else:
            self.image = pygame.transform.scale(pygame.image.load(self.image_path).convert(), (self.width, self.height))
    def draw_picture(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))       
class Player(Hitbox):
    def __init__(self, screen, x, y, width, height, color, weight, speed):
        Hitbox.__init__(self, screen, x, y, width, height, color, weight)
        self.speed = speed
 
        self.dx = 0
        self.dy = 0
    
    def move(self):
        self.rect.y += self.speed * self.dy
 
    def cantroller1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.dy = -1
        elif keys[pygame.K_s] and not keys[pygame.K_w]:
            self.dy = 1
        else:
            self.dy = 0
 
    def cantroller2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.dy = -1
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.dy = 1
        else:
            self.dy = 0


 
    def colide_screen(self):
        if self.rect.y > 520:
            self.rect.y = 520
        elif self.rect.y < 0:
            self.rect.y = 0
class Ball(Pictures):
    def __init__(self, screen, x, y, width, height, color, weight,image_path, speed_x, speed_y):
        Pictures.__init__(self, screen, x, y, width, height, color, weight, image_path)
        self.speed_y = speed_y
        self.speed_x = speed_x
 
        self.dx = choice([-1,1])
        self.dy = 0
 
    
    def move(self):
        self.rect.x += self.speed_x * self.dx
        self.rect.y += int(self.speed_y * self.dy)
    def collision(self,player1,player2,coins):
        if self.rect.colliderect(player1.rect):
            if self.dx < 0:
                if player1.rect.right - self.rect.left <= self.speed_x:
                    self.rect.left = player1.rect.right
                    self.dy = randint(-10,10)/10
                    self.dx = 1
                    coins += 1
        elif self.rect.colliderect(player2.rect):
            if self.dx > 0:
                if player2.rect.left - self.rect.right <= self.speed_x:
                    self.rect.right = player2 .rect.left
                    self.dy = randint(-10,10)/10
                    self.dx = -1
                    coins += 1
        return coins
 
    def collision_stena(self):
        if self.rect.bottom > 720:
            self.rect.bottom = 720
            self.dy = -self.dy
        elif self.rect.top < 0:
            self.rect.top = 0
            self.dy = -self.dy
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed_x = 0
            self.speed_y = 0
            self.rect.x = 620
            self.rect.y = 450
        elif self.rect.right > 1280:
            self.rect.right = 1280
            self.speed_x = 0
            self.speed_y = 0
            self.rect.x = 620
            self.rect.y = 400
 
    
 
lastx = 0
lasty = 0
 
    
 
screen_title = 'Догонялки'
screen_width = 1280
screen_height = 720
screen_color = (250,250,250)
 
coins =  0
 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(screen_title)
ball1 = Ball(screen, 620, 450, 20, 20, (250, 250, 250), 1,'мяч1.png',5,5 )
coin = Pictures(screen, 40, 90, 50, 50, (250, 250, 250), 1,'dollar.png' )
shop = Pictures(screen, 40, 40, 50, 50, (250, 250, 250), 1,'store.png' )
close = Pictures(screen, 600, 10, 100, 80, (250, 250, 250), 1,'closed.png' )
player1 = Player(screen, 20, 300, 40, 200, (0, 0, 0), 1,2 )
player2 = Player(screen, 1220, 300, 40, 200, (0, 0, 0), 1,2 )
tickrate = 60
clock = pygame.time.Clock()
shop_ecran = Pictures(screen, 0, 0, 1280, 720, (250, 250, 250), 1,'shop_ecran.jpg')

 
mimi_ecran2 = Pictures(screen, 150, 100, 250, 150, (252, 3, 3), 3,'фон2.jpg')
mimi_ecran3 = Pictures(screen, 450, 100, 250, 150, (252, 3, 3), 3,'фон3.jpg')
mimi_ecran4 = Pictures(screen, 750, 100, 250, 150, (252, 3, 3), 3,'фон4.jpg')
mimi_ecran5 = Pictures(screen, 150, 350, 250, 150, (252, 3, 3), 3,'фон5.jpg')

mimi_ball2 = Pictures(screen, 250, 270, 50, 50, (252, 3, 3), 3,'мяч2.png')
 
mimi_ball3 = Pictures(screen, 350, 270, 50, 50, (252, 3, 3), 3,'мяч3.png')
mimi_ball4 = Pictures(screen, 450, 270, 50, 50, (252, 3, 3), 3,'мяч4.png')
is_working = True
shop_ecrans = False
shop_ecran_proverka = False
ecran2 = False
ekran = False

no_mini_ecran2 = False
no_mini_ecran3 = False
no_mini_ecran4 = False
no_mini_ecran5 = False

ecran_proverka2 = False
ecran_proverka3 = False
ecran_proverka4 = False
ecran_proverka5 = False

no_mini_ball2 = False
no_mini_ball3 = False
no_mini_ball4 = False

ball_proverka2 = False
ball_proverka3 = False
ball_proverka4 = False

 
while is_working:


 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_working = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:        
                if ball1.speed_x == 0 and ball1.speed_y == 0:
                    ball1.dx = choice([-1,1])
                    ball1.speed_x = 5  
                    ball1.speed_y = 5
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_position = event.pos
                if shop.is_clicked(click_position):
                    
                    shop_ecrans = True
                    shop_ecran_proverka = True
                    lastx = ball1.speed_x
                    lasty = ball1.speed_y
                    xlast = ball1.rect.x
                    ylast = ball1.rect.y 
                    dx_ = ball1.dx     
                    dy_ = ball1.dy            
                if shop_ecran_proverka:
                        if mimi_ecran2.is_clicked(click_position):
                            if not ecran_proverka2:
                                if coins >= 10:
                                    coins -= 10
                                    no_mini_ecran2 = True
                                    ecran_proverka2 = True
                            elif ecran_proverka2:
                                no_mini_ecran2 = True
                        if no_mini_ecran2:

                                ecran = Pictures(screen, 0, 0, 1280, 720, (250, 250, 250), 1,'фон2.jpg')
                                ekran = True 
                                no_mini_ecran3 = False
                                no_mini_ecran4 = False
                                no_mini_ecran5 = False

                        if mimi_ecran3.is_clicked(click_position):
                            if not ecran_proverka3:
                                if coins >= 15:
                                    coins -= 15
                                    no_mini_ecran3 = True
                                    ecran_proverka3 = True
                            elif ecran_proverka3:
                                no_mini_ecran3 = True
                        if no_mini_ecran3:

                                ecran = Pictures(screen, 0, 0, 1280, 720, (250, 250, 250), 1,'фон3.jpg')
                                ekran = True 
                                no_mini_ecran2 = False
                                no_mini_ecran4 = False
                                no_mini_ecran5 = False


                        if mimi_ecran4.is_clicked(click_position):
                            if not ecran_proverka4:
                                if coins >= 20:
                                    coins -= 20
                                    no_mini_ecran4 = True
                                    ecran_proverka4 = True
                            elif ecran_proverka4:
                                no_mini_ecran4 = True
                        if no_mini_ecran4:

                                ecran = Pictures(screen, 0, 0, 1280, 720, (250, 250, 250), 1,'фон4.jpg')
                                ekran = True 
                                no_mini_ecran2 = False
                                no_mini_ecran3 = False
                                no_mini_ecran5 = False

                        

                        if mimi_ecran5.is_clicked(click_position):
                            if not ecran_proverka5:
                                if coins >= 30:
                                    coins -= 30
                                    no_mini_ecran5 = True
                                    ecran_proverka5 = True
                            elif ecran_proverka5:
                                no_mini_ecran5 = True
                        if no_mini_ecran5:

                                ecran = Pictures(screen, 0, 0, 1280, 720, (250, 250, 250), 1,'фон5.jpg')
                                ekran = True 
                                no_mini_ecran2 = False
                                no_mini_ecran3 = False
                                no_mini_ecran4 = False
                                

                        if mimi_ball2.is_clicked(click_position):
                            if not ball_proverka2:
                                if coins >= 10:
                                    coins -= 10
                                    no_mini_ball2 = True
                                    ball_proverka2 = True
                            elif ball_proverka2:
                                no_mini_ball2 = True
                        if no_mini_ball2:

                                ball1  = Ball(screen, 0, 0, 25, 25, (250, 250, 250), 1,'мяч2.png', 0, 0)

                                no_mini_ball3 = False
                                no_mini_ball4 = False


                        if mimi_ball3.is_clicked(click_position):
                            if not ball_proverka3:
                                if coins >= 15:
                                    coins -= 15
                                    no_mini_ball3 = True
                                    ball_proverka3 = True
                            elif ball_proverka3:
                                no_mini_ball3 = True
                        if no_mini_ball3:

                                ball1  = Ball(screen, 0, 0, 30, 30, (250, 250, 250), 1,'мяч3.png',0,0)
                                no_mini_ball2 = False
                                no_mini_ball4 = False


                        if mimi_ball4.is_clicked(click_position):
                            if not ball_proverka4:
                                if coins >= 20:
                                    coins -= 20
                                    no_mini_ball4 = True
                                    ball_proverka4 = True
                            elif ball_proverka4:
                                no_mini_ball4 = True
                        if no_mini_ball4:

                                ball1  = Ball(screen, 0, 0, 40, 40, (250, 250, 250), 1,'мяч4.png',0,0)
                                no_mini_ball2 = False
                                no_mini_ball3 = False


 
                if close.is_clicked(click_position):
                    shop_ecrans = False
                    shop_ecran_proverka = False
                    player1.speed = 5
                    player2.speed = 5
                    ball1.speed_x = lastx
                    ball1.speed_y = lasty
                    ball1.rect.x = xlast
                    ball1.rect.y = ylast
                    ball1.dx = dx_
                    ball1.dy = dy_
                    

                    
                    
 
                
 
                                
 
                 
    screen.fill(screen_color) 
    if ekran:
        ecran.draw_picture()
 

    player1.fill()
    player1.colide_screen()
    player1.cantroller1()
    player1.move()
    player2.fill()
    player2.cantroller2()
    player2.move()
    player2.cantroller1()
    player2.colide_screen()    
    ball1.draw_picture()
    ball1.collision_stena()
    coins = ball1.collision(player1,player2,coins)
    ball1.move()
    coin.draw_picture()
    shop.draw_picture()
    screen.blit(pygame.font.SysFont(None,40).render(str(coins),True,(0,0,0)),(100,100))
 
    if shop_ecrans:
        shop_ecran.draw_picture()
        player1.speed = 0
        player2.speed = 0
        ball1.speed_x = 0    
        ball1.speed_y = 0    
        close.draw_picture()
 
        mimi_ecran2.draw_picture()
        mimi_ecran3.draw_picture()
        mimi_ecran4.draw_picture()
        mimi_ecran5.draw_picture()
        mimi_ball2.draw_picture()
        mimi_ball3.draw_picture()
        mimi_ball4.draw_picture()

        if not ecran_proverka2:
            screen.blit(pygame.font.SysFont(None,40).render('цена 10',True,(0,0,0)),(230,250))
        if no_mini_ecran2:
            mimi_ecran2.color = (7, 252, 3)
            mimi_ecran2.drow_hitbox()

        if not no_mini_ecran2:
            mimi_ecran2.color = (248, 0, 0)
            mimi_ecran2.drow_hitbox()


        if not ecran_proverka3:
            screen.blit(pygame.font.SysFont(None,40).render('цена 15',True,(0,0,0)),(470,250))

        if no_mini_ecran3:
            mimi_ecran3.color = (7, 252, 3)
            mimi_ecran3.drow_hitbox()

        if not no_mini_ecran3:
            mimi_ecran3.color = (248, 0, 0)
            mimi_ecran3.drow_hitbox()


        if not ecran_proverka4:
            screen.blit(pygame.font.SysFont(None,40).render('цена 20',True,(0,0,0)),(770,250))

        if no_mini_ecran4:
            mimi_ecran4.color = (7, 252, 3)
            mimi_ecran4.drow_hitbox()

        if not no_mini_ecran4:
            mimi_ecran4.color = (248, 0, 0)
            mimi_ecran4.drow_hitbox()





        if not ecran_proverka5:
            screen.blit(pygame.font.SysFont(None,40).render('цена 25',True,(0,0,0)),(230,500))

        if no_mini_ecran5:
            mimi_ecran5.color = (7, 252, 3)
            mimi_ecran5.drow_hitbox()

        if not no_mini_ecran5:
            mimi_ecran5.color = (248, 0, 0)
            mimi_ecran5.drow_hitbox()

        if not ball_proverka2:
            screen.blit(pygame.font.SysFont(None,30).render('цена 10',True,(0,0,0)),(250, 320))

        if no_mini_ball2:
            mimi_ball2.color = (7, 252, 3)
            mimi_ball2.drow_hitbox()

        if not no_mini_ball2:
            mimi_ball2.color = (248, 0, 0)
            mimi_ball2.drow_hitbox()


        if not ball_proverka3:
            screen.blit(pygame.font.SysFont(None,30).render('цена 15',True,(0,0,0)),(350, 320))

        if no_mini_ball3:
            mimi_ball3.color = (7, 252, 3)
            mimi_ball3.drow_hitbox()

        if not no_mini_ball3:
            mimi_ball3.color = (248, 0, 0)
            mimi_ball3.drow_hitbox()

        if not ball_proverka4:
            screen.blit(pygame.font.SysFont(None,30).render('цена 20',True,(0,0,0)),(450, 320))

        if no_mini_ball4:
            mimi_ball4.color = (7, 252, 3)
            mimi_ball4.drow_hitbox()

        if not no_mini_ball4:
            mimi_ball4.color = (248, 0, 0)
            mimi_ball4.drow_hitbox()






 
    
    coin.draw_picture()
    screen.blit(pygame.font.SysFont(None,40).render(str(coins),True,(0,0,0)),(100,100))
 
    pygame.display.update()
    clock.tick(tickrate)