import math
import pygame
import time
import random


def initWindow(width, height, color):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(color)
    clock = pygame.time.Clock()

    return screen, clock


def drawCircleEyes(screen, center, color, width):
    gap = 200
    radius = 75
    pygame.draw.circle(screen, color, (center[0]-gap, center[1]-100), radius, width)
    pygame.draw.circle(screen, color, (center[0]+gap, center[1]-100), radius, width)


def drawLineEyes(screen, center, color, width):
    gap = 300
    length = 200
    pygame.draw.line(screen, color, (center[0]-gap, center[1]-100), (center[0]-gap+length, center[1]-100), width)
    pygame.draw.line(screen, color, (center[0]+gap-length, center[1]-100), (center[0]+gap, center[1]-100), width)


def drawVerticalLineEyes(screen, center, color, width):
    gap = 200
    halfLength = 75
    pygame.draw.line(screen, color, (center[0]-gap, center[1]-100-halfLength),
                     (center[0]-gap, center[1]-100+halfLength), width)
    pygame.draw.line(screen, color, (center[0]+gap, center[1]-100-halfLength),
                     (center[0]+gap, center[1]-100+halfLength), width)


def drawShockedEyes(screen, center, color, width):
    gap = 200
    halfLength = 50
    pygame.draw.line(screen, color, (center[0]-gap, center[1]-100-halfLength),
                     (center[0]-gap, center[1]-100+halfLength), width)
    pygame.draw.line(screen, color, (center[0]+gap, center[1]-100-halfLength),
                     (center[0]+gap, center[1]-100+halfLength), width)
    pygame.draw.circle(screen, color, (center[0]+gap, center[1]-70+halfLength), 10)
    pygame.draw.circle(screen, color, (center[0] - gap, center[1] - 70 + halfLength), 10)


def drawDeadInsideEyes(screen, center, color, width):
    gap = 200
    radius = 100
    pointsRight = [(center[0]-gap, center[1]-105)]
    for angle in range(0, 181, 5):
        x = center[0]-gap + radius * math.cos(math.radians(angle))
        y = center[1]-105 + radius * math.sin(math.radians(angle))
        pointsRight.append((x, y))

    pointsLeft = [(center[0] + gap, center[1] - 105)]
    for angle in range(0, 181, 5):
        x = center[0] + gap + radius * math.cos(math.radians(angle))
        y = center[1] - 105 + radius * math.sin(math.radians(angle))
        pointsLeft.append((x, y))

    pygame.draw.polygon(screen, color, pointsRight, width)
    pygame.draw.polygon(screen, color, pointsLeft, width)


def drawAngryEyes(screen, center, color, width):
    gap = 200
    radius = 100
    pointsRight = [(center[0]-gap, center[1]-100)]
    for angle in range(45, 226, 5):
        x = center[0]-gap + radius * math.cos(math.radians(angle))
        y = center[1]-100 + radius * math.sin(math.radians(angle))
        pointsRight.append((x, y))

    pointsLeft = [(center[0] + gap, center[1] - 100)]
    for angle in range(-45, 136, 5):
        x = center[0] + gap + radius * math.cos(math.radians(angle))
        y = center[1] - 100 + radius * math.sin(math.radians(angle))
        pointsLeft.append((x, y))

    pygame.draw.polygon(screen, color, pointsRight, width)
    pygame.draw.polygon(screen, color, pointsLeft, width)


def drawHeartEyes(screen, center, color, width):
    # doesn't work
    half_size = 100 / 2
    quarter_size = 100 / 4

    pygame.draw.circle(screen, color, (screenCenter[0] - quarter_size, screenCenter[1]), quarter_size)

    pygame.draw.circle(screen, color, (screenCenter[0] + quarter_size, screenCenter[1]), quarter_size)

    points = [(screenCenter[0] - half_size, screenCenter[1]), (screenCenter[0] + half_size, screenCenter[1]),
              (screenCenter[0], screenCenter[1] + 75)]
    pygame.draw.polygon(screen, color, points)


def drawMouthNeutral(screen, center, color):
    halfLength = 250
    pygame.draw.line(screen, color, (center[0]-halfLength, center[1]+200), (center[0]+halfLength, center[1]+200), 4)


def drawMouthHappy(screen, center, color):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-200, halfLength*2, halfLength*2), math.radians(200), math.radians(340), 4)


def drawMouthDerpy(screen, center, color):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-500, halfLength*2, halfLength*2), math.radians(240), math.radians(300), 4)


def drawMouthSmile(screen, center, color):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-300, halfLength*2, halfLength*2), math.radians(240), math.radians(300), 4)


def drawMouthSad(screen, center, color):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]+5, halfLength*2, halfLength*2), math.radians(20), math.radians(160), 4)


def drawMouthAngry(screen, center, color):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]+100, halfLength*2, halfLength*2), math.radians(50), math.radians(130), 4)


def drawMouthFrog(screen, center, color):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-100, halfLength*2, halfLength*6), math.radians(20), math.radians(160), 4)
    # pygame.draw.line(screen, color, (center[0]-halfLength+16, center[1]+63),
    #                  (center[0]-halfLength+16, center[1]+300), 4)
    # pygame.draw.line(screen, color, (center[0] + halfLength - 17, center[1] + 63),
    #                  (center[0] + halfLength-17, center[1] + 300), 4)



def drawMouthFrogOriginal(screen, center, color):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-100, halfLength*2, halfLength*2), math.radians(20), math.radians(160), 4)


def drawMouthUpset(screen, center, color):
    points = []
    amplitude = 10
    frequency = .05
    halfLength = 250
    for x in range(int(center[0]-halfLength), int(center[0] + halfLength), 5):
        y = int(amplitude * math.sin(frequency * x) + center[1]+100)
        points.append((x, y))
    pygame.draw.lines(screen, color, False, points, 4)


def drawMouthSurprised(screen, center, color):
    radius = 100
    pygame.draw.circle(screen, color, (center[0], center[1]+100+radius), radius, 4)



def talk(screen, center, color):
    frequency = random.random()
    halfLength = 250
    points = [(center[0]-halfLength, center[1]+150)]
    for x in range(int(center[0] - halfLength), int(center[0] + halfLength), 5):
        amplitude = random.randint(10, 50)
        y = int(amplitude * math.sin(frequency * x) + center[1] + 150)
        points.append((x, y))
    deleteMouth(screen, center)
    pygame.draw.lines(screen, color, False, points, 4)


def blink(screen, open, center, color):
    if open:
        deleteEyes(screen, center, WHITE)
        drawLineEyes(screen, center, color, 4)
        return False
    else:
        deleteEyes(screen, center, WHITE)
        drawCircleEyes(screen, center, BLACK, 4)
        return True


def blinkFrog(screen, open, center, color):
    if open:
        deleteEyes(screen, center, LIGHTGREEN)
        #drawCircleEyes(screen, center, BLACK, 4)
        drawLineEyes(screen, center, color, 4)
        return False
    else:
        deleteEyes(screen, center, LIGHTGREEN)
        drawCircleEyes(screen, center, BLACK, 4)
        return True



def blinkAngry(screen, open, center, color):
    if open:
        deleteEyes(screen, center, WHITE)
        drawLineEyes(screen, center, color, 4)
        return False
    else:
        deleteEyes(screen, center, WHITE)
        drawAngryEyes(screen, center, BLACK, 4)
        return True


def changeMouth(screen, expression, center, color):
    if expression.lower() == "happy":
        deleteMouth(screen, center)
        drawMouthHappy(screen, center, color)
    elif expression.lower() == "sad":
        deleteMouth(screen, center)
        drawMouthSad(screen, center, color)
    elif expression.lower() == "angry":
        deleteMouth(screen, center)
        drawMouthAngry(screen, center, color)
    elif expression.lower() == "neutral":
        deleteMouth(screen, center)
        drawMouthNeutral(screen, center, color)
    elif expression.lower() == "frog":
        deleteMouth(screen, center)
        drawMouthFrog(screen, center, color)


def deleteEyes(screen, center, color):
    gap = 200
    radius = 105
    pygame.draw.circle(screen, color, (center[0] - gap, center[1] - 100), radius, width)
    pygame.draw.circle(screen, color, (center[0] + gap, center[1] - 100), radius, width)


def deleteMouth(screen, center):
    halfLength = 250
    pygame.draw.rect(screen, WHITE, (center[0]-halfLength, center[1]+5, halfLength*2, halfLength*3))


width = 1250
height = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 128, 0)
LIGHTBLUE = (25, 200, 255)
LIGHTGREEN = (0, 255, 100)

screenCenter = (width/2, height/2)

screen, clock = initWindow(width, height, WHITE)
expressions = ["Happy", "Angry", "Neutral", "Sad"]
frequency = .05
i = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    eyeWidth = 4
    drawCircleEyes(screen, screenCenter, BLACK, eyeWidth)
    #open = blink(screen, open, screenCenter, BLACK)
    #drawMouthHappy(screen, screenCenter, BLACK)
    if i > 3:
        i = 0
    #changeMouth(screen, expressions[i], screenCenter, BLACK)
    drawMouthDerpy(screen, screenCenter, BLACK)
    #talk(screen, screenCenter, BLACK)
    i += 1
    pygame.display.update()
    time.sleep(.1)
    clock.tick(60)
pygame.quit()