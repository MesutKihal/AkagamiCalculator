import pygame
import time
import math
import sys

pygame.init()

black = (0,0,0)
white = (255,255,255)
blue = (0,64,128)
green = (34,177,76)
red = (217,0,5)
grey = (50,50,50)

width = 280
height = 340
bg = pygame.image.load('RedHair.jpg')
clock = pygame.time.Clock()
fps = 60

font = pygame.font.SysFont('tahoma', 24)
error_font = pygame.font.SysFont('rod', 14)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Calculator')
entry = ''
equation = ''
message = ''

column = [10,62,114,166,218]
row = [64,119,174,229,284]

#Class
class Button(object):
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.width = 50
        self.height = 48
        self.color = grey
        self.font = pygame.font.SysFont('tunga', 48)
        self.txtrnd = self.font.render(self.text, True, white)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))
        screen.blit(self.txtrnd, (self.x+(self.width//3),self.y-(self.height//4)))

class SpecialButton(object):
    def __init__(self, x, y, width, height,color, btntext, text):
        self.x = x
        self.y = y
        self.btntext = btntext
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont('couriernew', 32, bold = True)
        self.txtrnd = self.font.render(self.btntext, True, white)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))
        screen.blit(self.txtrnd, (self.x+(self.width//5),self.y+(self.height//4)))

#GridLayout        
seven = Button(column[0], row[1], '7')
eight = Button(column[1], row[1], '8')
nine = Button(column[2], row[1], '9')

four = Button(column[0], row[2], '4')
five = Button(column[1], row[2], '5')
six = Button(column[2], row[2], '6')

one = Button(column[0], row[3], '1')
two = Button(column[1], row[3], '2')
three = Button(column[2], row[3], '3')

equals = SpecialButton(column[4], row[3], 50, 103, red, '=', '=')
dot = Button(column[2], row[4], '.')
zero = SpecialButton(column[0],row[4],100 ,48 ,grey ,'0', '0')

clear = SpecialButton(column[3], row[0], 50, 48, green, 'AC', 'AC')
add = SpecialButton(column[3], row[1], 50, 48, blue, '+', '+')
sub = SpecialButton(column[3], row[2], 50, 48, blue, '-', '-')
mul = SpecialButton(column[3], row[3], 50, 48, blue, '*', '*')
div = SpecialButton(column[3], row[4], 50, 48, blue,'/', '/')

bracketO = Button(column[1], row[0], '(')
bracketC = Button(column[2], row[0], ')')
power = SpecialButton(column[0], row[0], 50, 48, grey,'^', '**')
clearE = SpecialButton(column[4], row[0], 50, 48, green,'CE', 'CE')
squareRoot = SpecialButton(column[4], row[1], 50, 48, grey,'√(', 'math.sqrt(')
percent = SpecialButton(column[4], row[2], 50, 48, grey,'%', '/100')

#DrawFunction
def drawWindow():
    screen.fill(white)
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, white, (10,10,260,48))
    screen.blit(entry_text, (10,10))
    screen.blit(error_text, (10,40))
    seven.draw(screen)
    eight.draw(screen)
    nine.draw(screen)
    four.draw(screen)
    five.draw(screen)
    six.draw(screen)
    one.draw(screen)
    two.draw(screen)
    three.draw(screen)
    equals.draw(screen)
    zero.draw(screen)
    dot.draw(screen)
    clear.draw(screen)
    add.draw(screen)
    sub.draw(screen)
    mul.draw(screen)
    div.draw(screen)
    bracketO.draw(screen)
    bracketC.draw(screen)
    power.draw(screen)
    clearE.draw(screen)
    squareRoot.draw(screen)
    percent.draw(screen)
    pygame.display.update()
    
#Mainloop
while True:
    clock.tick(fps)
    error_text = error_font.render(message, True, red)
    try:
        entry_text = font.render(equation, True, black)
    except TypeError:
        entry = str(entry)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if seven.x < mouse[0] < seven.x + seven.width and seven.y < mouse[1] < seven.y + seven.height and not entry.isalpha():
                entry = entry + str(seven.text)
                equation = equation + str(seven.text)
            if eight.x < mouse[0] < eight.x + eight.width and eight.y < mouse[1] < eight.y + eight.height and not entry.isalpha():
                entry = entry + str(eight.text)
                equation = equation + str(eight.text)
            if nine.x < mouse[0] < nine.x + nine.width and nine.y < mouse[1] < nine.y + nine.height and not entry.isalpha():
                entry = entry + str(nine.text)
                equation = equation + str(nine.text)
            if four.x < mouse[0] < four.x + four.width and four.y < mouse[1] < four.y + four.height and not entry.isalpha():
                entry = entry + str(four.text)
                equation = equation + str(four.text)
            if five.x < mouse[0] < five.x + five.width and five.y < mouse[1] < five.y + five.height and not entry.isalpha():
                entry = entry + str(five.text)
                equation = equation + str(five.text)
            if six.x < mouse[0] < six.x + six.width and six.y < mouse[1] < six.y + six.height and not entry.isalpha():
                entry = entry + str(six.text)
                equation = equation + str(six.text)
            if one.x < mouse[0] < one.x + one.width and one.y < mouse[1] < one.y + one.height and not entry.isalpha():
                entry = entry + str(one.text)
                equation = equation + str(one.text)
            if two.x < mouse[0] < two.x + two.width and two.y < mouse[1] < two.y + two.height and not entry.isalpha():
                entry = entry + str(two.text)
                equation = equation + str(two.text)
            if three.x < mouse[0] < three.x + three.width and three.y < mouse[1] < three.y + three.height and not entry.isalpha():
                entry = entry + str(three.text)
                equation = equation + str(three.text)
            if zero.x < mouse[0] < zero.x + zero.width and zero.y < mouse[1] < zero.y + zero.height and not entry.isalpha():
                entry = entry + str(zero.text)
                equation = equation + str(zero.text)
            if dot.x < mouse[0] < dot.x + dot.width and dot.y < mouse[1] < dot.y + dot.height and not entry.isalpha():
                entry = entry + str(dot.text)
                equation = equation + str(dot.text)
            if bracketO.x < mouse[0] < bracketO.x + bracketO.width and bracketO.y < mouse[1] < bracketO.y + bracketO.height and not entry.isalpha():
                entry = entry + str(bracketO.text)
                equation = equation + str(bracketO.text)
            if bracketC.x < mouse[0] < bracketC.x + bracketC.width and bracketC.y < mouse[1] < bracketC.y + bracketC.height and not entry.isalpha():
                entry = entry + str(bracketC.text)
                equation = equation + str(bracketC.text)
            if power.x < mouse[0] < power.x + power.width and power.y < mouse[1] < power.y + power.height and not entry.isalpha():
                entry = entry + str(power.text)
                equation = equation + str(power.btntext)
            if squareRoot.x < mouse[0] < squareRoot.x + squareRoot.width and squareRoot.y < mouse[1] < squareRoot.y + squareRoot.height and not entry.isalpha():
                entry = entry + str(squareRoot.text)
                equation = equation + str(squareRoot.btntext)

            if equals.x < mouse[0] < equals.x + equals.width and equals.y < mouse[1] < equals.y + equals.height:                
                try:
                    if entry == 'Error':
                        entry = entry
                        equation = entry
                    else:
                        entry = str(eval(entry))
                        equation = entry
                except ZeroDivisionError:
                    entry = 'Error'
                    message = 'Division By Zero'
                except SyntaxError:
                    entry = 'Error'
                    message = 'Invalid Operation'
            if clear.x < mouse[0] < clear.x + clear.width and clear.y < mouse[1] < clear.y + clear.height:
                entry = ''
                equation = ''
                message = ''
            if clearE.x < mouse[0] < clearE.x + clearE.width and clearE.y < mouse[1] < clearE.y + clearE.height and not entry.isalpha():
                if entry[-10:-1] == 'math.sqrt':
                    entry = entry[:-9]
                    equation = equation[:-1]
                else:
                    entry = entry[:-1]
                    equation = equation[:-1]
            if add.x < mouse[0] < add.x + add.width and add.y < mouse[1] < add.y + add.height and not entry.isalpha():
                entry = entry + str(add.text)
                equation = equation + str(add.text)
            if sub.x < mouse[0] < sub.x + sub.width and sub.y < mouse[1] < sub.y + sub.height and not entry.isalpha():
                entry = entry + str(sub.text)
                equation = equation + str(sub.text)
            if mul.x < mouse[0] < mul.x + mul.width and mul.y < mouse[1] < mul.y + mul.height and not entry.isalpha():
                entry = entry + str(mul.text)
                equation = equation + str(mul.text)
            if div.x < mouse[0] < div.x + div.width and div.y < mouse[1] < div.y + div.height and not entry.isalpha():
                entry = entry + str(div.text)
                equation = equation + str(div.text)
            if percent.x < mouse[0] < percent.x + percent.width and percent.y < mouse[1] < percent.y + percent.height and not entry.isalpha():
                entry = entry + str(percent.text)
                equation = equation + str(percent.btntext)


    drawWindow()

pygame.quit()
