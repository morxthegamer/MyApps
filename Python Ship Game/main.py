import pygame as pg

pg.init()

FPS = 60
X, Y, VEL, WIDTH, HEIGHT = 0, 0, 5, 100, 100
clock = pg.time
img = pg.image.load("icon.png")
SCREEN = pg.display.set_mode((800, 500))
pg.display.set_caption("Ball Game")
pg.display.set_icon(img)
keys = pg.key.get_pressed()

SCREEN.fill((0,0,0))

def move():
    global X, Y

    if keys[pg.K_W]: X += 1
    if keys[pg.K_S]: X -= 1
    if keys[pg.K_A]: Y += 1
    if keys[pg.K_D]: Y -= 1

def loop(run: bool):
    while run:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

if __name__ == "__main__":
    loop(True)