import pygame, sys, string
import pygameui as pgu

pygame.init()

win_width = 900
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("This is a catption")

def draw(win):
    win.fill((38, 70, 83))

    for element in text_elements:
        element.draw(win)
        element.update()
    for element in clickable_elements:
        element.draw(win)
        element.update()

    pygame.display.flip()

#  Text elements
text_elements = []
title = pgu.Text((450, 90), "This is a title",  (244, 162, 97), fontSize = 100, fontName = "elephant")
undertitle = pgu.Text((450, 150), "This is an undertitle", (233, 196, 106), fontSize = 20, fontName = "elephant")
text_elements.append(title)
undertitle.jump((450, 150), (450, 155), 40)
text_elements.append(undertitle)
you_have_written = pgu.Text((450, 580), "You have written: ", (233, 196, 106), fontSize = 20)
text_elements.append(you_have_written)
# Button elements
clickable_elements = []
start_button = pgu.Element((450, 300), rectWidth = 300, content = "Start!", rectColor = (233, 196, 106), textColor = (231, 111, 81), fontSize= 50)
start_button.flow((450, 305), (450, 315), 60)
clickable_elements.append(start_button)
other_button = pgu.Element((800, 400), content = "Other", fontSize= 50)
clickable_elements.append(other_button)

# Input elements
input_element = pgu.Input((win_width//2, 400))
clickable_elements.append(input_element)

clock = pygame.time.Clock()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if start_button.was_clicked(clickable_elements):
        undertitle.hide_toggle()

    you_have_written.change("You have written: " + input_element.getValue())
    input_element.work(events, clickable_elements)
    draw(win)
    clock.tick(60)
