from configurations import *
from visual import *


clock=pg.time.Clock()

screen=pg.display.set_mode(WINDOW_SIZE)
screen.fill(((251, 235, 212))) 


pg.display.set_caption("Numeros")
icon=pg.image.load(IMG_PATH+ICON)
pg.display.set_icon(icon)


game_area=GameArea(screen)


running=True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running=False
        if event.type == pg.MOUSEBUTTONDOWN:
            game_area.btn_down(event.button, event.pos)
            
        if event.type == pg.MOUSEBUTTONUP:
            game_area.btn_up(event.button, event.pos)
            
