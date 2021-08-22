import pygame 
import os
import random 

pygame.init() #initilizing pygame
win_height = 400
win_width = 800
i = 0

win = pygame.display.set_mode((win_width,win_height)) #drawing out window 


#images used for loading hero 
left = [pygame.image.load(os.path.join("Assets/Hero", "L1.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L2.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L3.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L4.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L5.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L6.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L7.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L8.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L9.png"))]

right = [pygame.image.load(os.path.join("Assets/Hero", "R1.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R2.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R3.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R4.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R5.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R6.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R7.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R8.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R9.png"))]

#enemy 
left_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "L1E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "L2E.png")),     
            pygame.image.load(os.path.join("Assets/Enemy", "L3E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "L4E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "L5E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "L6E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "L7E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "L8E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "L9P.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "L10P.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "L11P.png"))
]
right_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "R1E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R2E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R3E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R4E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R5E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R6E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R7E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R8E.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R9P.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R10P.png")),
            pygame.image.load(os.path.join("Assets/Enemy", "R11P.png")),
]

#bullet images
bullet_img = pygame.image.load(os.path.join("Assets/Bullets", "light_bullet.png")) #loading bullet image
bi = pygame.transform.scale(bullet_img, (15, 15)) #sizing bullet image

bckg = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Background.png")), (win_width, win_height))#loaded bckg image
bg = pygame.transform.scale(bckg,(1000,500)) #sizing the bckg image 



#Class for Hero 
class Hero: 
    def __init__(self,x,y): #variables for walking of the characters
        self.x = x
        self.y = y
        self.vel_x = 10
        self.vel_y = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        self.jump = False
        self.bullets = []
        self.hitBox = (self.x,self.y,64,64)
        self.health = 30 
        self.lives = 5
        self.alive = True
        self.score = 0
        
        #variable used in jump of the character
        self.jump = False 
        self.cool_down_count = 0

    #first method: hero getting moved with keys 
    def move_hero (self, keys):
        if(keys[pygame.K_RIGHT]) and self.x <= win_width - 62: 
            self.x += self.vel_x
            self.face_right = True 
            self.face_left = False 
        elif(keys[pygame.K_LEFT]) and self.x >= 0:
            self.x -= self.vel_x
            self.face_right = False
            self.face_left = True 

        else: 
            self.step_index = 0 #repeat the images 

    #second method 
    #drawing the characters
    def draw(self,win):
        self.hitBox = (self.x + 10,self.y + 10,45,50) #to draw border again & again
        pygame.draw.rect(win,(255,0,0),(self.x + 15, self.y -5, 30,10))
        pygame.draw.rect(win,(0,255,0),(self.x + 15, self.y - 5, self.health,10))
        #pygame.draw.rect(win,(0,0,0), self.hitBox,2)
        if self.step_index >= 9:
            self.step_index = 0
        if self.face_left: 
            win.blit(left[self.step_index],(self.x,self.y))
            self.step_index += 1
        if self.face_right: 
            win.blit(right[self.step_index],(self.x,self.y))
            self.step_index += 1
    
    #third method: jumping velocity
    def jump_motion(self,keys):
        if keys[pygame.K_SPACE]and self.jump is False: 
            self.jump = True
        if self.jump:
            self.y -= self.vel_y * 4
            self.vel_y -= 1
        if self.vel_y <- 10:
            self.jump = False          
            self.vel_y = 10 

    #fourth method: direction of player
    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    #fifth method: shooting bullets
    def shoot_bullet(self):
        self.cool_down()
        if (keys[pygame.K_v] and self.cool_down_count == 0):
            #creating bullet instances when 'V' key is pressed 
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move_bullet()
            if bullet.off_screen():
                self.bullets.remove(bullet) 
        self.hit()

    #6th method: cooldown for bullets 
    def cool_down(self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1
    
    #when bullets touchees enemy
    def hit(self):
        for enemy in enemies:
            for bullet in self.bullets: 
                if enemy.hitBox[0] < bullet.x < enemy.hitBox[0] + enemy.hitBox[2] and enemy.hitBox[1] < bullet.y < enemy.hitBox[1] + enemy.hitBox[3]:
                    print("Player has hit the Enemy") 
                    enemy.health -= 5
                    player.bullets.remove(bullet)
                    #when enemy is at 0 helth:
                    if (enemy.health == 0):
                        enemies.remove(enemy)
                        player.score += 1


class Bullet:
    #initizling variables for Bullet
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    #drawing bullets
    def draw_bullet(self):
        win.blit(bi, (self.x,  self.y))
                  
    #direction of moving bullets 
    def move_bullet(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15
    
    def off_screen(self): #when bullet goes offscreen
      return not(self.x >= 0 and self.x <= win_width)
      
class Enemy:
    #initializing enemy variables 
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction 
        self.step_Index = 0
        self.hitBox = (self.x,self.y)
        self.health = 30


    #animation for enemies, one index to another
    def step(self):
        if self.step_Index >= 33:
            self.step_Index = 0

    #drawing enemy
    def draw(self,win):
        self.hitBox = (self.x + 15, self.y + 5, 35, 55)
        pygame.draw.rect(win,(255,0,0),(self.x + 15, self.y -10, 30,10))
        if self.health >= 0:
             pygame.draw.rect(win,(0,255,0),(self.x + 15, self.y - 10, self.health,10))

       
        #pygame.draw.rect(win,(255,0,0),self.hitBox,2)
        
        #direction of enemy
        self.step()
        if self.direction == left:
            win.blit(left_enemy[self.step_Index//3],(self.x,self.y))
        if self.direction == right:
            win.blit(right_enemy[self.step_Index//3],(self.x,self.y))
        self.step_Index += 1


    #moving 
    def move(self):
        if self.direction == left:
            self.x -= 3
        if self.direction == right:
            self.x += 3
        self.hit()

    #offscreen bullets
    def off_screen(self):
        return not (self.x >= -50 and self.x <= win_width + 50)
    
    #when enemy hits player
    def hit(self):
        if player.hitBox[0] < enemy.x + 32 < player.hitBox[0] + player.hitBox[2] and player.hitBox[1] < enemy.y + 32 < player.hitBox[1] + player.hitBox[3]:
                    print("Enemy has hit the Player")  
                    if player.health > 0:
                        player.health -= 1 
                        if player.health == 0 and player.lives > 0:
                          player.lives -= 1
                          player.health = 30
                          #if there is no more lives/health remaining
                        elif player.health == 0 and player.lives == 0:
                            player.alive = False 


                   

#drawing the game
def draw_game():
    win.fill((0,0,0)) #filling canvas color
    win.blit(bckg,(0,0))
    player.draw(win)
    for bullet in player.bullets:
        bullet.draw_bullet() #drawing bullet
    for enemy in enemies:
        enemy.draw(win)
    #checking if the player is dead or not
    if player.alive == False:
        win.fill((100,0,0))
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Game Over, press 'R' to restart", True,(0,0,0))
        textRect = text.get_rect()
        textRect.center = (win_width//2, win_height//2)
        win.blit(text,textRect)
        if keys[pygame.K_r]:
            player.alive = True
            player.lives = 5
            player.health = 30
    

        
    #displaying player life
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Lives = " + str(player.lives),True,(0,0,0))
    win.blit(text,(650,20))
    #player's score
    text = font.render("Score: " + str(player.score),True,(0,0,0))
    win.blit(text,(50,20))
    pygame.time.delay(30)
    pygame.display.update()



#creating instance of objects in hero (1 instance --> 1 hero)
player = Hero(250,290)

#creatng instances for enemy
enemies = []


 #creating main loop and calling all the functions
run = True 
while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    #input 
    keys = pygame.key.get_pressed()
    
    #calling the function movement
    player.move_hero(keys)
    player.jump_motion(keys)
    player.shoot_bullet()

    #calling the functions of enemies
    if len(enemies) == 0:                        
        rand_n = random.randint(0,1)
        if rand_n == 1:
            enemy = Enemy(750,300,left)
            enemies.append(enemy)
        if rand_n == 0:
            enemy =  Enemy(50,300,right)
            enemies.append(enemy) 
    
    for enemy in enemies:
        enemy.move()
        if enemy.off_screen():
            enemies.remove(enemy)

    
    draw_game()
