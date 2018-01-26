#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((250, 170), 0, 32)
my_font = pygame.font.SysFont('arial', 20)

#To play music, simply select and play
#pygame.mixer.music.load("Track1.mp3")
#pygame.mixer.music.play()

#Add enemies to list to be rendered
def add_enemies():
	if len(enemy_list) < 3:
		rannum = random.randint(1, 2)
		if rannum == 1:
			enemy_list.append(Sprite(random.randrange(270, 340), random.randrange(0, 150), 'Images/BasicEnemy.png'))
		if rannum == 2:
			enemy_list.append(Sprite(random.randrange(260, 330), random.randrange(0, 150), 'Images/EnemyPod.png'))

#Handles sprite rendering, etc
class Sprite():
	def __init__(self, start_x, start_y, imagename):
		self.x = start_x
		self.y = start_y		
		self.starting_y = self.y
		self.falling = False
		self.imagename = imagename
		self.sprite = pygame.image.load(self.imagename).convert_alpha()		
	def render(self):
		screen.blit(self.sprite, (self.x, self.y))
		if self.imagename == 'Images/LittleLumps.png' or self.imagename == 'Images/Lumps.png':
			screen.blit(self.sprite, (self.x+320, self.y))
			if 'Little' in self.imagename:
				self.x-=2
			elif '/Lumps' in self.imagename:
				self.x-=5
		if self.x < -319: self.x = 0
		#These enemies will try to follow you
		if self.imagename == 'Images/BasicEnemy.png':
			if ship.x < self.x: self.x -= 2
			if ship.x >= self.x: self.x -= 1
			if ship.y <= self.y: self.y -= 1
			if ship.y > self.y: self.y += 1
		if self.imagename == 'Images/EnemyPod.png':
			self.x -=1
			#With the following, this enemy will bounce
			if self.y >= self.starting_y - 20 and self.falling == False: self.y -= 1
			if self.y <= self.starting_y - 19 and self.falling == False: self.falling = True
			if self.y <= self.starting_y + 20 and self.falling == True: self.y += 1
			if self.y >= self.starting_y + 19 and self.falling == True: self.falling = False
			
def collision(pos_x, pos_y, obj_x, obj_y): #Sets collision detection
	if (pos_x > obj_x-12) and (pos_x <obj_x+12) and (pos_y > obj_y-12) and (pos_y < obj_y +12):
			return True
	else:
		return False
		
lumps = Sprite(0, -40, 'Images/Lumps.png')
littlelumps = Sprite(0, 0, 'Images/LittleLumps.png')
ship = Sprite(50, 100, 'Images/ship-norm.png')

speed = 2 #Ship's current speed setting
move_x, move_y = 0, 0

bullets = []
enemy_list = []
bullet_wait = 0
running = True
life = 3

while running:
	add_enemies()
	screen.fill((10, 0, 15))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			running = False
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				running = False
			if event.key == K_l:
				if speed < 4: speed += 1
			if event.key == K_k:
				if speed > 1: speed -= 1
			if event.key == K_w: move_y = -1
			if event.key == K_s: move_y = +1
			if event.key == K_d: move_x = +1
			if event.key == K_a: move_x = -1
			if event.key == K_p:
				if bullet_wait< 1:
					bullets.append(Sprite(ship.x, ship.y, 'Images/bullet.png'))
				bullet_wait+=5
		if event.type == KEYUP:
			if event.key == K_w: move_y = 0
			if event.key == K_s: move_y = 0
			if event.key == K_d: move_x = 0
			if event.key == K_a: move_x = 0
			
	if bullet_wait > 0: bullet_wait -=1
	
	
	if ship.x < -4: ship.x +=4
	if ship.x > 235: ship.x -= 4
	if ship.y > 160: ship.y -= 4
	if ship.y < 0: ship.y += 4
	
	ship.x += (move_x * speed); ship.y += (move_y * speed)
	
	speed_setting = my_font.render("Speed: %d"%speed, True, (0, 0, 0), (100, 100, 100))
	life_meter = my_font.render('Life: %d'%life, True, (0, 0, 0), (100, 100, 100))
	
	littlelumps.render()
	lumps.render()
	
	for enemy in enemy_list:
		enemy.render()
		if enemy.x < -10: enemy_list.remove(enemy)
			
	ship.render()
	
	#This'll display your stats
	screen.blit(speed_setting, (0, 0))
	screen.blit(life_meter, (60, 0))
	
	if len(bullets) >0:
		for bullet in bullets:
			bullet.render()
			bullet.x += 7
			if bullet.x > 340: bullets.remove(bullet)
			for enemy in enemy_list:
				if collision(enemy.x, enemy.y, bullet.x, bullet.y):
					enemy_list.remove(enemy)
					bullets.remove(bullet)
					
	# Take a hit, lose life
	for enemy in enemy_list:
		if collision(ship.x, ship.y, enemy.x, enemy.y):
			life -= 1
			enemy_list = []
			if life < 0: 
				running = False
				pygame.quit()
	clock.tick(60)
	pygame.display.update()