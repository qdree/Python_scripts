import time 
import pygame, sys
from pygame.locals import *
import gtk.gdk

width = gtk.gdk.screen_width()
height = gtk.gdk.screen_height()
password = "arsenal"

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1280, height))
# pygame.display.set_caption('Hello World!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)

while True: # main game loop
	DISPLAYSURF.fill(BLACK)

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_q: 
				pygame.quit()
				quit()
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type is KEYDOWN and event.key == K_w:
			pygame.display.set_mode((1280, height))
		if event.type is KEYDOWN and event.key == K_f:
			pygame.display.set_mode((1280, height), FULLSCREEN)

	pygame.display.update()
	# time.sleep(1)