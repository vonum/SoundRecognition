import pygame
import time
import pyaudio
from pl import Player
from apple import Apple
from recordinput import record
from ann import get_ann
import numpy as np
from utils import calculatefft
from utils import adaptivelocalmax
from numpy import sqrt, square, mean

def texts(score):
   font=pygame.font.Font(None,30)
   scoretext=font.render("Score:"+str(score), 1,(255,255,255))
   screen.blit(scoretext, (300, 20))

def renderSnake(pl):
	for row in pl.pos:
		pygame.draw.rect(screen, (200, 100, 50), pygame.Rect(row[0], row[1], pl.size, pl.size))

ann = get_ann()

freqs = np.array(np.exp(np.linspace(np.log(264), np.log(2000), 150)))
round_freqs = np.round(freqs, 0)

T = 0.1
round_freqs = round_freqs * T

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

CHUNK = 9600
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 96000

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
				channels=CHANNELS,
				rate=RATE,
				input=True,
				frames_per_buffer=CHUNK)

pl = Player(0, 0, 10, 10, 0)
ap = Apple(0, 0, 10)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			stream.stop_stream()
			stream.close()
			p.terminate()
			done = True

		if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			pl.orientation = 0
		if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			pl.orientation = 1
		if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			pl.orientation = 2
		if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			pl.orientation = 3

	a = record(p, stream)
	#rms = sqrt(mean(square(a)))
	a = calculatefft(RATE, a)[0]
	
	amptest = []
	amptest.append(adaptivelocalmax(a, round_freqs.astype(np.int64)))

	res = ann.predict(np.array(amptest))

	a = np.argmax(res)
	b = np.amax(res)
	if b > 0.95:
		pl.orientation = a

	pl.move()
	if(pl.checkApple(ap)):
		ap.generatePosition()
			
	screen.fill((0, 0, 0))

	texts(pl.score)

	renderSnake(pl)
	#pygame.draw.rect(screen, (200, 100, 50), pygame.Rect(pl.pos[0][0], pl.pos[0][1], pl.size, pl.size))
	pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(ap.pos_x, ap.pos_y, ap.size, ap.size))
	
	pygame.display.flip()
	#time.sleep(0.2)
	
	clock.tick(10)


