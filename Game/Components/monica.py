import pygame as pg
import os


class Hero:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y
        self.vel = 15

    def control(self):
        keys = pg.key.get_pressed()
        if self.y <= -50:
            self.y = 529
        if self.y >= 624:
            self.y = 1
        if keys[pg.K_w]:
            self.y -= self.vel
        if keys[pg.K_s]:
            self.y += self.vel

    def draw(self):
        x = pg.key.get_pressed()
        if x[pg.K_a]:
            monica = pg.image.load(os.path.join(os.path.dirname(__file__), "img/arma_esquerda.png"))
        elif x[pg.K_d]:
            monica = pg.image.load(os.path.join(os.path.dirname(__file__), "img/arma.png"))
        else:
            monica = pg.image.load(os.path.join(os.path.dirname(__file__), "img/arma_esquerda.png"))
        self.win.blit(monica, (self.x, self.y))


class Bullet:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

    def draw_right(self):
        sansao = pg.image.load(os.path.join(os.path.dirname(__file__), "img/sansao.png"))
        self.win.blit(sansao, (self.x+50, self.y+10))
        self.x += 20

    def draw_left(self):
        sansao = pg.image.load(os.path.join(os.path.dirname(__file__), "img/sansao.png"))
        self.win.blit(sansao, (self.x-10, self.y+10))
        self.x -= 20


def main():
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    player = Hero(screen, 375, 275)
    done = False

    shoots = []
    shootsR = []

    while not done:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN and event.key == pg.K_a:
                shoots.append(Bullet(screen, player.x, player.y))
            if event.type == pg.KEYDOWN and event.key == pg.K_d:
                shootsR.append(Bullet(screen, player.x, player.y))

        player.control()

        screen.fill((40, 40, 40))
        player.draw()
        for shoot in shoots:
            shoot.draw_left()

        for shoot in shootsR:
            shoot.draw_right()

        pg.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    exit()
