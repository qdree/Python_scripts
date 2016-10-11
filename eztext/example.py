# EzText example
from pygame.locals import *
import pygame, sys, eztext

password = 'arsenal'

def main():
    # initialize pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((640,280))
    # fill the screen w/ white
    screen.fill((255,255,255))
    # here is the magic: making the text input
    # create an input with a max length of 45,
    # and a red color and a prompt saying 'type here: '
    txtbx = eztext.Input(maxlength=40, color=(255,255,255), prompt='PASSWORD:')
    # create the pygame clock
    clock = pygame.time.Clock()
    # main loop!

    while 1:
        # make sure the program is running at 30 fps
        clock.tick(15)

        # events for txtbx
        events = pygame.event.get()

        # process other events
        for event in events:
            # close it x button si pressed
            if event.type == QUIT: return

        # clear the screen
        screen.fill((0,0,0))
        
        # update txtbx
        txtbx.update(events)

        # check password input
        if txtbx.chk_value(password):
            print "correct"
        else:
            print "something wrong"
        
        # blit txtbx on the sceen
        txtbx.draw(screen)
        
        # refresh the display
        pygame.display.flip()

if __name__ == '__main__': main()
