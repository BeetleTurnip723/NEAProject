'''
NEA Year 12 Project
Author: Joe Sykes
Date Started: 9/9/22
Idea:
My idea for my NEA is to make a formula one set-up simulator where you get randomised a track, and either if it is raining or not, and you choose your driver and try to create the perfect set-up for them to win the race
'''
# automake the other drivers set-ups and then give a recommendation to the reader to say what they can do better
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import pygame
import pygame_menu
from pygame import display

SCREENWIDTH, SCREENHEIGHT = 1440, 1000
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


pygame.init()
pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
# for cornering, F is for fast cornering, M is for medium cornering, S is for slow cornering

drivers = {
    "Mercedes": {
        "Lewis Hamilton": {
            "Rating": 95,               # OVR
            "Race-pace": 96,               # Pace
            "Carefulness": 96,               # Carefulness
            "Wet-weather Driving": 92,               # Wet-weather Driving
            "Cornering Style": "F"                 # Cornering Style
        },
        "George Russell": {
            "Rating:": 89,               # OVR
            "Race-pace": 93,               # Pace
            "Carefulness": 84,               # Carefulness
            "Wet-weather Driving": 90,               # Wet-weather Driving
            "Cornering Style": "M"                 # Cornering Style
        }
    },

    "Red Bull": {
        "Max Verstappen": {
            "97",               # OVR
            "99",               # Pace
            "92",               # Carefulness
            "99",               # Wet-weather Driving
            "F"                 # Cornering Style
        },
        "Sergio Perez": {
            "88",               # OVR
            "82",               # Pace
            "95",               # Carefulness
            "87",               # Wet-weather Driving
            "S"                 # Cornering Style
        }
    },

    "Ferrari": {
        "Charles Leclerc": {
            "91",               # OVR
            "94",               # Pace
            "90",               # Carefulness
            "88",               # Wet-weather Driving
            "M"                 # Cornering Style
        },
        "Carlos Sainz": {
            "88",               # OVR
            "85",               # Pace
            "87",               # Carefulness
            "92",               # Wet-weather Driving
            "F"                 # Cornering Style
        }
    },

    "McLaren": {
        "Lando Norris": {
            "90",               # OVR
            "93",               # Pace
            "87",               # Carefulness
            "90",               # Wet-weather Driving
            "M"                 # Cornering Style
        },
        "Oscar Piastri": {
            "82",               # OVR
            "86",               # Pace
            "78",               # Carefulness
            "82",               # Wet-weather Driving
            "F"                 # Cornering Style
        }
    },


}


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 1440, 1000)
        self.setWindowTitle("F1 Set-Up Simulator")
        self.initUI()

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText("F1 Set-Up Simulator")
        self.label.adjustSize()
        self.label.move(660, 0)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Play")
        self.button1.move(670, 50)
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("well done, you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()

print(drivers['Mercedes']['Lewis Hamilton'])


# menu = pygame_menu.Menu("Start",1240,800, theme=pygame_menu.themes.THEME_ORANGE)

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Main Menu")
carImg = pygame.image.load("MAINMENUCAR.png")
font = pygame.font.Font(None, 75)
MAINMENUTEXT = font.render("F1 Set-Up Simulator", False, white)
# game loop


def game():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill(black)
        SCREEN.blit(carImg, (550, 400))
        SCREEN.blit(MAINMENUTEXT, (475, 50))
        pos = pygame.mouse.get_pos()
        print(pos)

        pygame.display.update()

    pygame.quit()


# game()
