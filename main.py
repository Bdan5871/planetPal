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
    pygame.draw.line(screen, color, (center[0]-gap, center[1]-100), (center[0]-gap+length, center[1]-100), 4)
    pygame.draw.line(screen, color, (center[0]+gap-length, center[1]-100), (center[0]+gap, center[1]-100), 4)


def drawVerticalLineEyes(screen, center, color, width):
    gap = 200
    halfLength = 75
    pygame.draw.line(screen, color, (center[0]-gap, center[1]-100-halfLength),
                     (center[0]-gap, center[1]-100+halfLength), 4)
    pygame.draw.line(screen, color, (center[0]+gap, center[1]-100-halfLength),
                     (center[0]+gap, center[1]-100+halfLength), 4)


def drawShockedEyes(screen, center, color, width):
    gap = 200
    halfLength = 50
    pygame.draw.line(screen, color, (center[0]-gap, center[1]-100-halfLength),
                     (center[0]-gap, center[1]-100+halfLength), 4)
    pygame.draw.line(screen, color, (center[0]+gap, center[1]-100-halfLength),
                     (center[0]+gap, center[1]-100+halfLength), 4)
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


def drawMouthNeutral(screen, center, color, width):
    halfLength = 250
    pygame.draw.line(screen, color, (center[0]-halfLength, center[1]+200), (center[0]+halfLength, center[1]+200), width)


def drawMouthHappy(screen, center, color, width):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-200, halfLength*2, halfLength*2), math.radians(200), math.radians(340), width)


def drawMouthDerpy(screen, center, color, width):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-500, halfLength*2, halfLength*2), math.radians(240), math.radians(300), width)


def drawMouthSmile(screen, center, color, width):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-300, halfLength*2, halfLength*2), math.radians(240), math.radians(300), width)


def drawMouthSad(screen, center, color, width):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]+5, halfLength*2, halfLength*2), math.radians(20), math.radians(160), width)


def drawMouthAngry(screen, center, color, width):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]+100, halfLength*2, halfLength*2), math.radians(50), math.radians(130), width)


def drawMouthFrog(screen, center, color, width):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-100, halfLength*2, halfLength*6), math.radians(20), math.radians(160), width)
    # pygame.draw.line(screen, color, (center[0]-halfLength+16, center[1]+63),
    #                  (center[0]-halfLength+16, center[1]+300), 4)
    # pygame.draw.line(screen, color, (center[0] + halfLength - 17, center[1] + 63),
    #                  (center[0] + halfLength-17, center[1] + 300), 4)



def drawMouthFrogOriginal(screen, center, color, width):
    halfLength = 250
    pygame.draw.arc(screen, color,
                    (center[0]-halfLength, center[1]-100, halfLength*2, halfLength*2), math.radians(20), math.radians(160), width)


def drawMouthUpset(screen, center, color, width):
    points = []
    amplitude = 10
    frequency = .05
    halfLength = 250
    for x in range(int(center[0]-halfLength), int(center[0] + halfLength), 5):
        y = int(amplitude * math.sin(frequency * x) + center[1]+100)
        points.append((x, y))
    pygame.draw.lines(screen, color, False, points, width)


def drawMouthSurprised(screen, center, color, width):
    radius = 100
    pygame.draw.circle(screen, color, (center[0], center[1]+100+radius), radius, 0)


def talk(screen, center, color, screenColor, width):
    frequency = random.random()
    halfLength = 250
    points = []
    for x in range(int(center[0] - halfLength), int(center[0] + halfLength), 5):
        amplitude = random.randint(10, 50)
        y = int(amplitude * math.sin(frequency * x) + center[1] + 150)
        points.append((x, y))
    deleteMouth(screen, center, screenColor)
    pygame.draw.lines(screen, color, False, points, width)


def blink(screen, open, center, color, screenColor):
    if open:
        deleteEyes(screen, center, screenColor)
        drawLineEyes(screen, center, color, 4)
        return False
    else:
        deleteEyes(screen, center, screenColor)
        drawCircleEyes(screen, center, color, 4)
        return True


def blinkVertical(screen, open, center, color):
    if open:
        deleteEyes(screen, center, WHITE)
        drawVerticalLineEyes(screen, center, color, 4)
        return False
    else:
        deleteEyes(screen, center, WHITE)
        drawCircleEyes(screen, center, color, 4)
        return True


def blinkFrog(screen, open, center, color):
    if open:
        deleteEyes(screen, center, LIGHTGREEN)
        #drawCircleEyes(screen, center, BLACK, 4)
        drawLineEyes(screen, center, color, 4)
        return False
    else:
        deleteEyes(screen, center, LIGHTGREEN)
        drawCircleEyes(screen, center, color, 4)
        return True


def blinkAngry(screen, open, center, color):
    if open:
        deleteEyes(screen, center, WHITE)
        drawLineEyes(screen, center, color, 4)
        return False
    else:
        deleteEyes(screen, center, WHITE)
        drawAngryEyes(screen, center, color, 4)
        return True


def changeMouth(screen, expression, center, color, screenColor, width):
    if expression.lower() == "happy":
        deleteMouth(screen, center, screenColor)
        drawMouthHappy(screen, center, color, width)
    elif expression.lower() == "sad":
        deleteMouth(screen, center, screenColor)
        drawMouthSad(screen, center, color, width)
    elif expression.lower() == "angry":
        deleteMouth(screen, center, screenColor)
        drawMouthAngry(screen, center, color, width)
    elif expression.lower() == "neutral":
        deleteMouth(screen, center, screenColor)
        drawMouthNeutral(screen, center, color, width)
    elif expression.lower() == "frog":
        deleteMouth(screen, center, screenColor)
        drawMouthFrogOriginal(screen, center, color, width)
    elif expression.lower() == "surprised":
        deleteMouth(screen, center, screenColor)
        drawMouthSurprised(screen, center, color, width)
    elif expression.lower() == "upset":
        deleteMouth(screen, center, screenColor)
        drawMouthUpset(screen, center, color, width)
    elif expression.lower() == "smile":
        deleteMouth(screen, center, screenColor)
        drawMouthSmile(screen, center, color, width)
    elif expression.lower() == "derpy":
        deleteMouth(screen, center, screenColor)
        drawMouthDerpy(screen, center, color, width)


def changeEyes(screen, type, center, color, screenColor, width):
    if type.lower() == "happy":
        deleteEyes(screen, center, screenColor)
        drawCircleEyes(screen, center, color, width)
    elif type.lower() == "sad":
        deleteEyes(screen, center, screenColor)
        drawDeadInsideEyes(screen, center, color, width)
    elif type.lower() == "angry":
        deleteEyes(screen, center, screenColor)
        drawAngryEyes(screen, center, color, width)
    elif type.lower() == "neutral":
        deleteEyes(screen, center, screenColor)
        drawLineEyes(screen, center, color, width)
    elif type.lower() == "shocked":
        deleteEyes(screen, center, screenColor)
        drawShockedEyes(screen, center, color, width)
    elif type.lower() == "vertical":
        deleteEyes(screen, center, screenColor)
        drawVerticalLineEyes(screen, center, color, width)


def delete(screen, center, color):
    pygame.draw.rect(screen, color,(0, 0, center[0]*2, center[1]*2))


def deleteEyes(screen, center, color):
    gap = 200
    radius = 105
    pygame.draw.circle(screen, color, (center[0] - gap, center[1] - 100), radius, width)
    pygame.draw.circle(screen, color, (center[0] + gap, center[1] - 100), radius, width)


def deleteMouth(screen, center, color):
    halfLength = 500
    pygame.draw.rect(screen, color, (center[0]-halfLength, center[1]+5, halfLength*2, halfLength*3))


width = 1250
height = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
ORANGE = (255, 128, 0)
LIGHTBLUE = (35, 160, 220)
PURPLEBLUE = (50, 100, 255)
DARKBLUE = (0, 100, 255)
LIGHTGREEN = (0, 255, 100)
PINK = (255, 141, 161)

screenCenter = (width/2, height/2)

screenColor = LIGHTBLUE
faceColor = BLACK

screen, clock = initWindow(width, height, screenColor)

#pygame.draw.ellipse(screen, screenColor, (0, 0, width, height))

expressions = [
    "happy", "sad", "angry", "neutral",
    "frog", "surprised", "upset", "smile", "derpy"
]
eye_types = [
    "happy", "sad", "angry", "neutral",
    "shocked", "vertical"
]
frequency = .05
talking = False
tracker = 0
talkingSpeed = 5
i = 0
j = 0
eyeWidth = 0
mouthWidth = 10

drawCircleEyes(screen, screenCenter, faceColor, eyeWidth)
drawMouthHappy(screen, screenCenter, faceColor, mouthWidth)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                i = 0
                j = 5
                delete(screen, screenCenter, screenColor)
                drawMouthHappy(screen, screenCenter, faceColor, mouthWidth)
                drawVerticalLineEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_2:
                i = 0
                j = 0
                delete(screen, screenCenter, screenColor)
                drawMouthHappy(screen, screenCenter, faceColor, mouthWidth)
                drawCircleEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_3:
                i = 5
                j = 0
                delete(screen, screenCenter, screenColor)
                drawMouthSurprised(screen, screenCenter, faceColor, mouthWidth)
                drawCircleEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_4:
                i = 7
                j = 5
                delete(screen, screenCenter, screenColor)
                drawMouthSmile(screen, screenCenter, faceColor, mouthWidth)
                drawVerticalLineEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_5:
                i = 7
                j = 0
                delete(screen, screenCenter, screenColor)
                drawMouthSmile(screen, screenCenter, faceColor, mouthWidth)
                drawCircleEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_6:
                i = 3
                j = 0
                delete(screen, screenCenter, screenColor)
                drawMouthNeutral(screen, screenCenter, faceColor, mouthWidth)
                drawCircleEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_7:
                i = 3
                j = 3
                delete(screen, screenCenter, screenColor)
                drawMouthNeutral(screen, screenCenter, faceColor, mouthWidth)
                drawLineEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_8:
                i = 6
                j = 0
                delete(screen, screenCenter, screenColor)
                drawMouthUpset(screen, screenCenter, faceColor, mouthWidth)
                drawCircleEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_9:
                i = 3
                j = 2
                delete(screen, screenCenter, screenColor)
                drawMouthNeutral(screen, screenCenter, faceColor, mouthWidth)
                drawDeadInsideEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_0:
                i = 7
                j = 2
                delete(screen, screenCenter, screenColor)
                drawMouthSmile(screen, screenCenter, faceColor, mouthWidth)
                drawDeadInsideEyes(screen, screenCenter, faceColor, eyeWidth)
            elif event.key == pygame.K_UP:
                if expressions[i] == "derpy":
                    delete(screen, screenCenter, screenColor)
                    changeEyes(screen, eye_types[j], screenCenter, faceColor, screenColor, eyeWidth)
                elif expressions[i] == "frog":
                    delete(screen, screenCenter, screenColor)
                    changeEyes(screen, eye_types[j], screenCenter, faceColor, screenColor, eyeWidth)
                i += 1
                if i >= len(expressions):
                    i = 0
                changeMouth(screen, expressions[i], screenCenter, faceColor, screenColor, mouthWidth)
            elif event.key == pygame.K_DOWN:
                if expressions[i] == "derpy":
                    delete(screen, screenCenter, screenColor)
                    changeEyes(screen, eye_types[j], screenCenter, faceColor, screenColor, eyeWidth)
                elif expressions[i] == "frog":
                    delete(screen, screenCenter, screenColor)
                    changeEyes(screen, eye_types[j], screenCenter, faceColor, screenColor, eyeWidth)
                i -= 1
                if i < 0:
                    i = len(expressions) - 1
                changeMouth(screen, expressions[i], screenCenter, faceColor, screenColor, mouthWidth)
            elif event.key == pygame.K_RIGHT:
                j += 1
                if j >= len(eye_types):
                    j = 0
                changeEyes(screen, eye_types[j], screenCenter, faceColor, screenColor, eyeWidth)
            elif event.key == pygame.K_LEFT:
                j -= 1
                if j < 0:
                    j = len(eye_types) - 1
                changeEyes(screen, eye_types[j], screenCenter, faceColor, screenColor, eyeWidth)
            elif event.key == pygame.K_SPACE:
                changeEyes(screen, "neutral", screenCenter, faceColor, screenColor, eyeWidth)
                pygame.display.update()
                time.sleep(.25)
                changeEyes(screen, eye_types[j], screenCenter, faceColor, screenColor, eyeWidth)
            elif event.key == pygame.K_t:
                talking = not talking
    if talking and tracker%talkingSpeed == 0:
        talk(screen, screenCenter, faceColor, screenColor, mouthWidth)
    elif not talking:
        changeMouth(screen, expressions[i], screenCenter, faceColor, screenColor, mouthWidth)
    tracker += 1
    pygame.display.update()
    clock.tick(60)
pygame.quit()