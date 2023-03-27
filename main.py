import pygame, sys
from pygame.locals import QUIT
import random

SIZE = 50
COLUMNS = 4

pygame.init()
screen = pygame.display.set_mode((400, 300))

def create_cards():
    result = []
    for i in range(6):
        card = pygame.image.load(f"card{i}.jfif")
        size = (SIZE, SIZE)
        card = pygame.transform.scale(card, size)
        result.append(card)
    return 2 * result

cards = create_cards()
random.shuffle(cards)

def draw_card(i):
    row = i // COLUMNS
    column = i % COLUMNS
    pos = (column * (SIZE+5), row * (SIZE+5))
    screen.blit(cards[i], pos)    

def draw_game():
    screen.fill(background)
    for i in range(len(cards)):
        draw_card(i)
    pygame.display.update()

def wait_event():
    global running
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False

def run():
    pygame.display.set_caption('Hello World!')
    while running:
        draw_game()
        wait_event()

running = True
background = (220, 220, 220)

run()