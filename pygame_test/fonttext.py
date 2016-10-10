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

fontObj = pygame.font.Font('freesansbold.ttf', 40)
textSurfaceObj1 = fontObj.render('PASSWORD', True, WHITE, BLACK)
textSurfaceObj2 = fontObj.render('CORRECT!', True, WHITE, BLACK)
textRectObj1 = textSurfaceObj1.get_rect()
textRectObj1.center = (1280 / 2.0, height / 2.0)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (1280 / 2.0 - 20, height / 2.0)
while True: # main game loop
	DISPLAYSURF.fill(BLACK)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()

	input_password = raw_input()
	while not input_password == password:
		DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
		input_password = raw_input()
	print ("Correct password!")
	if input_password == password:
		DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
		time.sleep(2)
		quit()
	
