'''
NEA Year 12 Project
Author: Joe Sykes
Date Started: 9/9/22
Idea:
My idea for my NEA is to make a formula one set-up simulator where you get randomised a track, and either if it is raining or not, and you choose your driver and try to create the perfect set-up for them to win the race
'''
# automake the other drivers set-ups and then give a recommendation to the reader to say what they can do better
import PyQt5
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QSlider, QLabel
import sys

from PyQt5.uic import loadUi
import pygame
import pygame_menu
from pygame import display

SCREENWIDTH, SCREENHEIGHT = 1440, 1000
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



# for cornering, F is for fast cornering, M is for medium cornering, S is for slow cornering

drivers = {
    "Mercedes": {
        "Lewis Hamilton": {
            "Rating": 95,
            "Race-pace": 96,
            "Carefulness": 96,
            "Wet-weather Driving": 92,
            "Cornering Style": "F"
        },
        "George Russell": {
            "Rating:": 89,
            "Race-pace": 93,
            "Carefulness": 84,
            "Wet-weather Driving": 90,
            "Cornering Style": "M"
        }
    },

    "Red Bull": {
        "Max Verstappen": {
            "Rating:": 97,
            "Race-pace": 99,
            "Carefulness": 92,
            "Wet-weather Driving": 99,
            "Cornering Style": "F"
        },
        "Sergio Perez": {
            "Rating:": 88,
            "Race-pace": 82,
            "Carefulness": 95,
            "Wet-weather Driving": 87,
            "Cornering Style": "S"
        }
    },

    "Ferrari": {
        "Charles Leclerc": {
            "Rating:": 91,
            "Race-pace": 94,
            "Carefulness": 90,
            "Wet-weather Driving": 88,
            "Cornering Style": "M"
        },
        "Carlos Sainz": {
            "Rating:": 88,
            "Race-pace": 85,
            "Carefulness": 87,
            "Wet-weather Driving": 92,
            "Cornering Style": "F"
        }
    },

    "McLaren": {
        "Lando Norris": {
            "Rating:": 90,
            "Race-pace": 93,
            "Carefulness": 87,
            "Wet-weather Driving": 90,
            "Cornering Style": "M"
        },
        "Oscar Piastri": {
            "Rating:": 82,
            "Race-pace": 86,
            "Carefulness": 78,
            "Wet-weather Driving": 82,
            "Cornering Style": "F"
        }
    },

    "Aston Martin": {
        "Fernando Alonso": {
            "Rating:": 91,
            "Race-pace": 89,
            "Carefulness": 92,
            "Wet-weather Driving": 92,
            "Cornering Style": "S"
        },
        "Lance Stroll": {
            "Rating:": 85,
            "Race-pace": 85,
            "Carefulness": 83,
            "Wet-weather Driving": 87,
            "Cornering Style": "M"
        }
    },
    "Alpine": {
        "Esteban Ocon": {
            "Rating:": 86,
            "Race-pace": 88,
            "Carefulness": 83,
            "Wet-weather Driving": 87,
            "Cornering Style": "S"
        },
        "Pierre Gasly": {
            "Rating:": 87,
            "Race-pace": 87,
            "Carefulness": 85,
            "Wet-weather Driving": 89,
            "Cornering Style": "F"
        }
    },
    "Alpha Tauri": {
        "Nyck de Vries": {
            "Rating:": 80,
            "Race-pace": 83,
            "Carefulness": 77,
            "Wet-weather Driving": 80,
            "Cornering Style": "M"
        },
        "Yuki Tsunoda": {
            "Rating:": 83,
            "Race-pace": 85,
            "Carefulness": 80,
            "Wet-weather Driving": 81,
            "Cornering Style": "S"
        }
    },
    "HAAS": {
        "Nico Hulkenberg": {
            "Rating:": 84,
            "Race-pace": 80,
            "Carefulness": 86,
            "Wet-weather Driving": 86,
            "Cornering Style": "M"
        },
        "Kevin Magnussen": {
            "Rating:": 84,
            "Race-pace": 86,
            "Carefulness": 82,
            "Wet-weather Driving": 84,
            "Cornering Style": "F"
        }
    },
    "Alfa Romeo": {
        "Valtteri Bottas": {
            "Rating:": 88,
            "Race-pace": 87,
            "Carefulness": 89,
            "Wet-weather Driving": 88,
            "Cornering Style": "S"
        },
        "Guanyu Zhou": {
            "Rating:": 80,
            "Race-pace": 84,
            "Carefulness": 76,
            "Wet-weather Driving": 80,
            "Cornering Style": "F"
        }
    },
    "Williams": {
        "Alex Albon": {
            "Rating:": 87,
            "Race-pace": 88,
            "Carefulness": 85,
            "Wet-weather Driving": 86,
            "Cornering Style": "M"
        },
        "Logan Sargeant": {
            "Rating:": 78,
            "Race-pace": 80,
            "Carefulness": 75,
            "Wet-weather Driving": 79,
            "Cornering Style": "S"
        }
    }


}


class TeamSelectWindow(QMainWindow):

    def __init__(self):
        super(TeamSelectWindow, self).__init__()
        loadUi("TeamSelectMenu.ui", self)


class SettingsWindow(QMainWindow):

    def __init__(self):
        super(SettingsWindow, self).__init__()
        loadUi("SettingsMenu.ui", self)
        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.label = self.findChild(QLabel, "label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.slider.valueChanged.connect(self.slide_it)

    def slide_it(self, value):
        self.label.setText(str(value))

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi("MAINMENU.ui", self)
        self.playButton = self.findChild(QPushButton, "playButton")
        self.settingsButton = self.findChild(QPushButton, "settingsButton")
        self.exitButton = self.findChild(QPushButton, "exitButton")

        self.playButton.clicked.connect(self.team_select_menu)
        self.settingsButton.clicked.connect(self.settings_menu)
        self.exitButton.clicked.connect(self.exit_menu)

        self.team_select_window = TeamSelectWindow()
        self.settings_win = SettingsWindow()
        self.show()

    def team_select_menu(self):
        self.team_select_window.show()

    def settings_menu(self):
        self.settings_win.show()

    def exit_menu(self):
        self.close()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.setFixedWidth(SCREENWIDTH)
    win.setFixedHeight(SCREENHEIGHT)
    app.exec_()
    sys.exit(app.exec_())


window()

print(drivers['Mercedes']['Lewis Hamilton'])

