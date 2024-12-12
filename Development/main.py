from configurations import *
from visual import *


clock = pg.time.Clock()
#Create a screen
screen = pg.display.set_mode(Window_size)
screen.fill(((251, 235, 212))) 

#Change the caption and the icon
pg.display.set_caption("Numeros")
icon = pg.image.load(Img_path+icon)
pg.display.set_icon(icon)

field_board = Field(screen)
hand_board = Hand(screen)

#Create a loop for the screen not to close until the user quits
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            field_board.btn_down(event.button, event.pos)
            hand_board.btn_down(event.button, event.pos)
        if event.type == pg.MOUSEBUTTONUP:
            field_board.btn_up(event.button, event.pos)
            hand_board.btn_up(event.button, event.pos)
