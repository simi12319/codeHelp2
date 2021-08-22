import pygame
import os
import random

pygame.init()
win_height = 400
win_width = 800
win = pygame.display.set_mode((win_width, win_height))

standing = pygame.image.load(os.path.join("Assets/Hero", "standing.png"))

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

eleft = pygame.image.load(os.path.join("Assets","monkey.png"))
Eleft = pygame.transform.scale(eleft, (30, 30))

bullet_img = pygame.image.load(os.path.join("Assets/Bullets", "light_bullet.png"))
bi = pygame.transform.scale(bullet_img, (15, 15))

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 10
        self.vel_y = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        self.jump = False
        self.bullets = []
        self.cool_down_count = 0
        self.hitBox = (self.x, self.y, 42, 55)

    # Movement function
    def movement(self, userInput):
        if (userInput[pygame.K_RIGHT]) and self.x <= win_width - 60:
            self.x += self.vel_x
            self.face_right = True
            self.face_left = False
        elif (userInput[pygame.K_LEFT]) and self.x >= 0:
            self.x -= self.vel_x
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    def draw_character(self, win):
        self.hitBox = (self.x + 10, self.y + 10, 42, 55) # So the hitbox can be drawn again
        pygame.draw.rect(win, (0, 0, 255), self.hitBox, 2)
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

    # Jumping
    def Jump(self, userInput):
        if userInput[pygame.K_UP] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vel_y * 4
            self.vel_y -= 1
        if self.vel_y < -10:
            self.jump = False
            self.vel_y = 10

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def Cool_Down(self):
        if self.cool_down_count >= 7:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot_bullet(self):
        self.hit()
        self.Cool_Down()
        if (userInput[pygame.K_SPACE] and self.cool_down_count == 0):
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move_bullet()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def hit(self):
        for enemy in enemies:
            for bullet in self.bullets:
                if enemy.hitBox[0] < bullet.x < enemy.hitBox[0] + enemy.hitBox[2] and enemy.hitBox[1] < bullet.y < enemy.hitBox[1] + enemy.hitBox[3]:
                    print("You have hit the enemy!")

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def draw_bullet(self):
        win.blit(bi, (self.x, self.y))

    def move_bullet(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

    def off_screen(self):
        return not(self.x >= 0 and self.x <= win_width)

class Enemy():
    def __init__(self, x, y, direction):
        self.x =  x
        self.y = y
        self.direction = direction
        self.step_index = 0
        self.hitBox = (self.x, self.y, 42, 55)

    def step(self):
        if self.step_index >= 33:
            self.step_index = 0
    
    def draw_enemy(self, win):
        self.step()
        self.hitBox = (self.x, self.y, 30, 30)
        pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)
        win.blit(Eleft,(self.x,self.y))

    def move_enemy(self):
        self.hit_hero()
        if self.direction == left:
            self.x -= 3
        if self.direction == right:
            self.x += 3

    def off_screen(self):
        return not(self.x >= -50 and self.x <= win_width + 50)

    def hit_hero(self):
        if player.hitBox[0] < enemy.x + 32 < player.hitBox[0] + player.hitBox[2] and player.hitBox[1] < enemy.y + 32 < player.hitBox[1] + player.hitBox[3]:
            print("Enemy has hit you!")

# main funciton
def game():
    win.fill((240, 240, 240))
    player.draw_character(win)
    for bullet in player.bullets:
        bullet.draw_bullet()
    for enemy in enemies:
        enemy.draw_enemy(win)
    pygame.time.delay(30)
    pygame.display.update()

player = Hero(250, 300)

enemies = []

#main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #name spacing
    userInput = pygame.key.get_pressed()

    #calling all our functions
    player.movement(userInput)
    player.Jump(userInput)
    player.shoot_bullet()

    if len(enemies) == 0:
        rand_n = random.randint(0,1)
        if rand_n == 1:
            enemy = Enemy(750, 300, left)
            enemies.append(enemy)
        if rand_n == 0:
            enemy = Enemy(50, 300, right)
            enemies.append(enemy)
    for enemy in enemies:
        enemy.move_enemy()
        if enemy.off_screen():
            enemies.remove(enemy)

    game()