import pygame

pygame.init()
win = pygame.display.set_mode((1025, 681))

pygame.display.set_caption("Angry Cat")

walkRight = [pygame.image.load('Cut png/effect cat/walk/walk1.png')]#,
             #pygame.image.load('')]
walkLeft = [pygame.image.load('Cut png/effect cat/walk/walk1.png')]#,
             #pygame.image.load('')]
playerSnand = pygame.image.load('Cut png/effect cat/walk/walk1.png')

bg = pygame.image.load('LVL1.png')

clock = pygame.time.Clock()

x = 20
y = 400
width = 50
height = 52
speed = 5

isJump = False
jumpCount = 10


left = False
right = False
animCount = 0

def drawWindow():
    global animCount
    win.blit(bg, (0,0))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[0], (x, y))
        animCount +=1
    elif right:
        win.blit(walkLeft[0], (x, y))
        animCount +=1
    else:
        win.blit(playerSnand, (x,y))

    pygame.display.update()


run = True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1025 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount <0:
                y +=(jumpCount **2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()
