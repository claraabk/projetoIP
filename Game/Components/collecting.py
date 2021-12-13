import pygame as pg

class Hero:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.thickness = 20
        self.heigt = 20
        self.vel = 10
        self.colour = "WHITE"

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.x -= self.vel
        if keys[pg.K_d]:
            self.x += self.vel
        if keys[pg.K_w]:
            self.y -= self.vel
        if keys[pg.K_s]:
            self.y += self.vel

    def draw(self):
        pg.draw.rect(self.win, self.colour, (self.x, self.y, self.thickness, self.heigt))
    


def collect(buff, player): 
    # Creates rectangles to check position of player and collectible 
    player_rect = pg.Rect(player.x, player.y, 20, 20)
    buff_rect = pg.Rect(buff.x, buff.y, 20, 20)
    return pg.Rect.colliderect(buff_rect, player_rect)

def main():
    screen = pg.display.set_mode((600, 400))
    clock = pg.time.Clock()
    player = Hero(screen, 320, 240)
    buff = Hero(screen, 100, 200)
    done = False
    # Add later specific count for each collectible
    count_provisorio_buff = 0

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        player.control()

        screen.fill((40, 40, 40))
        player.draw()
        buff.draw()

        # Uses the function collect to check collision, move the collectible away from the screen to simulate the collect
        if collect(buff, player):
            # Change later to create a method inside the buff class, so the attribute is not changed directly
            buff.x = 1000
            buff.y = 1000
            count_provisorio_buff += 1

        pg.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    exit()