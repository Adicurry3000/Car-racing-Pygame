import random
import time
import pygame

pygame.init()

crash_sound = pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("Swagger.mp3")

display_width = 900
display_height = 700

black = (0, 0, 0)
white = (255, 255, 255)
red = (200,0,0)
blue = (130, 202, 250)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)



car_width = 110

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('a bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
caricon = pygame.image.load('caricon.png')

pygame.display.set_icon(caricon)

pause = False


def things_crossed(count):
    font = pygame.font.SysFont("comicsansms", 35)
    text = font.render("Dodged : "+str(count), True, black)
    game_display.blit(text, (0,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(game_display, color, [int(thingx), int(thingy), int(thingw), int(thingh)])


def car(x, y):
    game_display.blit(carImg, (x, y))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    largetext = pygame.font.SysFont("comicsansms", 110)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = (int(display_width/2), int(display_height/2))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)

    game_loop()


def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largetext = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Crashed", largetext)
    TextRect.center = (int(display_width / 2), int(display_height / 2))
    game_display.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("PLAY AGAIN", 150, 470, 140, 50, green, bright_green, "play")
        button("QUIT", 650, 470, 100, 50, red, bright_red, "quit")

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_display, ic, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "unpause":
                global pause
                pygame.mixer.music.unpause()
                pause = False
    else:
        pygame.draw.rect(game_display, ac, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSerf, textRect = text_objects(msg, smallText)
    textRect.center = (int(x + (w / 2)), int(y + (h / 2)))
    game_display.blit(textSerf, textRect)



def stop():

    pygame.mixer.music.pause()
    largetext = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largetext)
    TextRect.center = (int(display_width / 2), int(display_height / 2))
    game_display.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("CONTINUE", 150, 470, 120, 50, green, bright_green, "unpause")
        button("QUIT", 650, 470, 100, 50, red, bright_red, "quit")

        pygame.display.update()
        clock.tick(15)


def game_into():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(white)
        largetext = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("A Bit Racey", largetext)
        TextRect.center = (int(display_width / 2), int(display_height / 2))
        game_display.blit(TextSurf, TextRect)

        button("RACE!", 150, 470, 100, 50, green, bright_green, "play")
        button("QUIT", 650, 470, 100, 50, red, bright_red, "quit")

        pygame.display.update()
        clock.tick(15)



def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    x = int(display_width * 0.45)
    y = int(display_height * 0.77)
    x_change = 0

    game_exit = False

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 2
    thing_width = 100
    thing_height = 100
    dodged = 0

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    stop()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0

        x += x_change

        game_display.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed
        car(x,y)
        things_crossed(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.1
            thing_width += 10

        if y < thing_starty + thing_height:
            if thing_startx < x < thing_startx + thing_width or thing_startx < x + car_width < thing_startx + thing_width:
                crash()
        pygame.display.update()
        clock.tick(180)

game_into()
game_loop()
pygame.quit()
quit()
