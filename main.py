import random
from setting import *

surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shoot Bug")

class Fly:
    def __init__(self):
        self.fly=0
        self.dx=0
        self.dy=0
    def fly_Rect(self):
        self.fly = pygame.Rect(fly_image.get_rect())
        self.fly.left = random.choice(fly_pos)
        self.fly.top = random.randint(0, screen_height)
        self.dx = random.randint(-9, 9)
        self.dy = random.randint(-9, 9)
        return (self.fly, self.dx, self.dy)

while running:
    if start == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start = 1
                elif event.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    sys.exit()

        start_image = start_font.render('Catch the Flies', True, BLACK)
        press_r_image = score_font.render('Press \'r\' to start', True, YELLOW)
        press_q_image = end_font.render('Press \'q\' to quit', True, BLACK)

        screen.blit(background, (0, 0))
        screen.blit(start_image, (screen_width / 2 - start_image.get_width() / 2, screen_height / 3 - start_image.get_height() / 2))
        screen.blit(press_r_image, (screen_width / 2 - press_r_image.get_width() / 2, screen_height / 3 * 2 - press_r_image.get_height() / 2))
        screen.blit(press_q_image, (screen_width / 2 - press_q_image.get_width() / 2, screen_height / 3 * 2 - press_r_image.get_height() / 2 + 70))
        pygame.display.update()

    elif start == 1:
        how_to_play = start_font.render('How to play', True, BLACK)
        p1_play = how_font.render('player1 up: w left: a right: d down: s catch fly: CAPS LOCK', True, BLACK)
        p2_play = how_font.render('player2 up: ↑ left: ← right: → down: ↓ catch fly: R_CTRL', True, BLACK)

        screen.blit(background, (0, 0))
        screen.blit(how_to_play, (screen_width / 2 - how_to_play.get_width() / 2, 30))
        screen.blit(p1_play, (screen_width / 2 - p1_play.get_width() / 2, screen_height / 3 - p1_play.get_height() / 2+20))
        screen.blit(p2_play, (screen_width / 2 - p2_play.get_width() / 2, screen_height / 3 * 2 - p2_play.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(3000)

        for i in range(3):
            screen.blit(background, (0, 0))
            pygame.display.update()
            countdown = 3 - i
            count_down = countdown_font.render(f'{countdown}', True, BLACK)
            screen.blit(count_down, (screen_width / 2 - count_down.get_width() / 2, screen_height / 2 - count_down.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(1000)

        start = 2

    elif start == 2:
        if i == 0:
            fly=Fly()
            flies.append(fly.fly_Rect())

        i += 1
        if i == 10:
            i = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    to_y1 -= speed
                elif event.key == pygame.K_a:
                    to_x1 -= speed
                elif event.key == pygame.K_d:
                    to_x1 += speed
                elif event.key == pygame.K_s:
                    to_y1 += speed
                elif event.key == pygame.K_CAPSLOCK:
                    for (fly, dx, dy) in flies:
                        if fly.collidepoint(cross1_x_pos + cross1_width / 2, cross1_y_pos + cross1_height / 2):
                            dead_flies.append((fly, dx, dy))
                            flies.remove((fly, dx, dy))
                            p1_score += 1

                elif event.key == pygame.K_RCTRL:
                    for (fly, dx, dy) in flies:
                        if fly.collidepoint(cross2_x_pos + cross2_width / 2, cross2_y_pos + cross2_height / 2):
                            dead_flies.append((fly, dx, dy))
                            flies.remove((fly, dx, dy))
                            p2_score += 1
                elif event.key == pygame.K_UP:
                    to_y2 -= speed
                elif event.key == pygame.K_LEFT:
                    to_x2 -= speed
                elif event.key == pygame.K_RIGHT:
                    to_x2 += speed
                elif event.key == pygame.K_DOWN:
                    to_y2 += speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x1 = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y1 = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x2 = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y2 = 0

        if running:
            for (fly, dx, dy) in flies:
                fly.left += dx
                fly.top += dy

        cross1_x_pos += to_x1
        cross1_y_pos += to_y1
        cross2_x_pos += to_x2
        cross2_y_pos += to_y2

        if cross1_x_pos < 0:
            cross1_x_pos = 0
        elif cross1_x_pos > screen_width - cross1_width:
            cross1_x_pos = screen_width - cross1_width

        if cross1_y_pos < 0:
            cross1_y_pos = 0
        elif cross1_y_pos > screen_height - cross1_height:
            cross1_y_pos = screen_height - cross1_height

        if cross2_x_pos < 0:
            cross2_x_pos = 0
        elif cross2_x_pos > screen_width - cross2_width:
            cross2_x_pos = screen_width - cross2_width

        if cross2_y_pos < 0:
            cross2_y_pos = 0
        elif cross2_y_pos > screen_height - cross2_height:
            cross2_y_pos = screen_height - cross2_height

        screen.blit(background, (0, 0))

        for (fly, dx, dy) in dead_flies:
            screen.blit(dead_fly, fly)
            fly.top+=2

        p1_score_image = score_font.render(f'player1: {p1_score}', True, BLACK)
        screen.blit(p1_score_image, (10, 10))
        p2_score_image = score_font.render(f'player2: {p2_score}', True, BLACK)
        screen.blit(p2_score_image, (screen_width - 10 - p2_score_image.get_width(), 10))

        for (fly, dx, dy) in flies:
            screen.blit(fly_image, fly)

        for (fly, dx, dy) in flies:
            if not fly.colliderect(screen.get_rect()):
                flies.remove((fly, dx, dy))

        for (fly, dx, dy) in dead_flies:
            if not fly.colliderect(screen.get_rect()):
                dead_flies.remove((fly, dx, dy))

        screen.blit(cross1, (cross1_x_pos, cross1_y_pos))
        screen.blit(cross2, (cross2_x_pos, cross2_y_pos))
        pygame.display.update()

        if p1_score >= 10:
            start = 0
            pygame.time.delay(1000)
            end1_image = start_font.render('Player1 Win!', True, BLACK)
            screen.blit(end1_image, (screen_width / 2 - end1_image.get_width() / 2, screen_height / 2 - end1_image.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(2000)
            p1_score=0
            p2_score=0
            for (fly, dx, dy) in dead_flies:
                dead_flies.remove((fly, dx, dy))
            for (fly, dx, dy) in flies:
                flies.remove((fly, dx, dy))

        elif p2_score >= 10:
            start = 0
            pygame.time.delay(1000)
            end2_image = start_font.render('Player2 Win!', True, BLACK)
            screen.blit(end2_image, (screen_width / 2 - end2_image.get_width() / 2, screen_height / 2 - end2_image.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(2000)
            p1_score=0
            p2_score=0
            for (fly, dx, dy) in dead_flies:
                dead_flies.remove((fly, dx, dy))
            for (fly, dx, dy) in flies:
                flies.remove((fly, dx, dy))

    clock.tick(FPS)
