import pygame
import time
from pl import Player
from apple import Apple


pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

pl = Player(0, 0, 15, 15, 0)
ap = Apple(0, 0, 5)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			pl.orientation = 0
		if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			pl.orientation = 1
		if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			pl.orientation = 2
		if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			pl.orientation = 3

	pl.move()
	if(pl.checkApple(ap)):
		ap.generatePosition()
	#ap.generatePosition()
			
	screen.fill((0, 0, 0))

	pygame.draw.rect(screen, (200, 100, 50), pygame.Rect(pl.pos_x, pl.pos_y, pl.size, pl.size))
	pygame.draw.rect(screen, (10, 100, 0), pygame.Rect(ap.pos_x, ap.pos_y, ap.size, ap.size))
	
	pygame.display.flip()
	#time.sleep(0.2)
	
	clock.tick(10)