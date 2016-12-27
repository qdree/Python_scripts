import pygame
import random
from blob_class import Blob
import numpy as np
import logging

STARTING_BLOBS = 30

WIDTH = 1024
HEIGHT = 720
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

logging.basicConfig(filename = 'logfile.log', level=logging.INFO)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

def is_touching(b1,b2):
    return np.linalg.norm(np.array([b1.x,b1.y])-np.array([b2.x,b2.y])) < (b1.size + b2.size)

def handle_collisions(blob_list):

    blues, reds, greens = blob_list
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                logging.debug('Checking if blobs touching {} + {}'.format(repr(blue_blob), repr(other_blob)))
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if blue_blob.size <= 0:
                            try:
                                del blues[blue_id]
                            except KeyError:
                                pass

    for red_id, red_blob in reds.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                logging.debug('Checking if blobs touching {} + {}'.format(repr(red_blob), repr(other_blob)))
                if red_blob == other_blob:
                    pass
                else:
                    if is_touching(red_blob, other_blob):
                        red_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if red_blob.size <= 0:
                            try:
                               del reds[red_id]
                            except KeyError:
                                pass

    for green_id, green_blob in greens.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                logging.debug('Checking if blobs touching {} + {}'.format(repr(green_blob), repr(other_blob)))
                if green_blob == other_blob:
                    pass
                else:
                    if is_touching(green_blob, other_blob):
                        green_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if green_blob.size <= 0:
                            try:
                                del greens[green_id]
                            except KeyError:
                                pass
                            
    return blues, reds, greens

class SpeckledBlob(Blob):
    
    def __init__(self, color = (0, 0, 0), x_boundary = WIDTH, y_boundary = HEIGHT):
        super(SpeckledBlob, self).__init__(color, x_boundary, y_boundary)
        self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

    def __add__(self, other_blob):
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size
            
        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0
            
        elif other_blob.color == (0, 0, 255):
            # for now, nothing. Maybe later it does something more. 
            pass
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors!')


class BlueBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)
    
    def __add__(self, other_blob):
        logging.info('Blob add op: {} + {}'.format(repr(self), repr(other_blob)))
        if self.size > other_blob.size:
            self.size += other_blob.size
            other_blob.size = 0
        elif self.size == other_blob.size:
            cur_size = self.size
            self.size -= 2
            other_blob.size -= 2
        elif self.size < other_blob.size:
            other_blob.size += self.size
            self.size = 0            
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors!')


class RedBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)

    def __add__(self, other_blob): 
        logging.info('Blob add op: {} + {}'.format(repr(self), repr(other_blob)))
        if self.size > other_blob.size:
            self.size += other_blob.size
            other_blob.size = 0
        elif self.size == other_blob.size:
            cur_size = self.size
            self.size -= 2
            other_blob.size -= 2
        elif self.size < other_blob.size:
            other_blob.size += self.size
            self.size = 0            
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors!')


class GreenBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)

    def __add__(self, other_blob):
        logging.info('Blob add op: {} + {}'.format(repr(self), repr(other_blob)))
        if self.size > other_blob.size:
            self.size += other_blob.size
            other_blob.size = 0
        elif self.size == other_blob.size:
            cur_size = self.size
            self.size -= 2
            other_blob.size -= 2
        elif self.size < other_blob.size:
            other_blob.size += self.size
            self.size = 0            
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors!')


def draw_environment(blob_list):
    blues, reds, greens = handle_collisions(blob_list)
    game_display.fill(WHITE)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()

    pygame.display.update()
    return blues, reds, greens

def main():
    sparckled_blobs = dict(enumerate([SpeckledBlob() for i in range(10)]))
    
    blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_BLOBS)]))

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            blue_blobs, red_blobs, green_blobs = draw_environment([blue_blobs,red_blobs,green_blobs])
            clock.tick(60)
        except Exception as e:
            logging.critical(str(e))
            pygame.quit()
            quit()
            break


if __name__ == '__main__':
    # pygame.quit()
    main()