'''
NEA Year 12 Project
Author: Joe Sykes
Date Started: 9/9/22
'''

# automake the other drivers set-ups and then give a recommendation to the reader to say what they can do better
import PyQt5
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QSlider, QLabel, QLineEdit
import sys
import math
import time
import random
from PyQt5.uic import loadUi
import pygame
from pygame import display

pygame.font.init()

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
            "Name": "Lewis Hamilton",
            "Rating": 95,
            "Race-pace": 96,
            "Carefulness": 96,
            "Wet-weather Driving": 92,
            "Cornering Style": "F"
        },
        "George Russell": {
            "Name": "George Russell",
            "Rating:": 89,
            "Race-pace": 93,
            "Carefulness": 84,
            "Wet-weather Driving": 90,
            "Cornering Style": "M"
        }
    },

    "Red Bull": {
        "Max Verstappen": {
            "Name": "Max Verstappen",
            "Rating:": 97,
            "Race-pace": 99,
            "Carefulness": 92,
            "Wet-weather Driving": 99,
            "Cornering Style": "F"
        },
        "Sergio Perez": {
            "Name": "Sergio Perez",
            "Rating:": 88,
            "Race-pace": 82,
            "Carefulness": 95,
            "Wet-weather Driving": 87,
            "Cornering Style": "S"
        }
    },

    "Ferrari": {
        "Charles Leclerc": {
            "Name": "Charles Leclerc",
            "Rating:": 91,
            "Race-pace": 94,
            "Carefulness": 90,
            "Wet-weather Driving": 88,
            "Cornering Style": "M"
        },
        "Carlos Sainz": {
            "Name": "Carlos Sainz",
            "Rating:": 88,
            "Race-pace": 85,
            "Carefulness": 87,
            "Wet-weather Driving": 92,
            "Cornering Style": "F"
        }
    },

    "McLaren": {
        "Lando Norris": {
            "Name": "Lando Norris",
            "Rating:": 90,
            "Race-pace": 93,
            "Carefulness": 87,
            "Wet-weather Driving": 90,
            "Cornering Style": "M"
        },
        "Oscar Piastri": {
            "Name": "Oscar Piastri",
            "Rating:": 82,
            "Race-pace": 86,
            "Carefulness": 78,
            "Wet-weather Driving": 82,
            "Cornering Style": "F"
        }
    },

    "Aston Martin": {
        "Fernando Alonso": {
            "Name": "Fernando Alonso",
            "Rating:": 91,
            "Race-pace": 89,
            "Carefulness": 92,
            "Wet-weather Driving": 92,
            "Cornering Style": "S"
        },
        "Lance Stroll": {
            "Name": "Lance Stroll",
            "Rating:": 85,
            "Race-pace": 85,
            "Carefulness": 83,
            "Wet-weather Driving": 87,
            "Cornering Style": "M"
        }
    },
    "Alpine": {
        "Esteban Ocon": {
            "Name": "Esteban Ocon",
            "Rating:": 86,
            "Race-pace": 88,
            "Carefulness": 83,
            "Wet-weather Driving": 87,
            "Cornering Style": "S"
        },
        "Pierre Gasly": {
            "Name": "Pierre Gasly",
            "Rating:": 87,
            "Race-pace": 87,
            "Carefulness": 85,
            "Wet-weather Driving": 89,
            "Cornering Style": "F"
        }
    },
    "Alpha Tauri": {
        "Nyck de Vries": {
            "Name": "Nyck de Vries",
            "Rating:": 80,
            "Race-pace": 83,
            "Carefulness": 77,
            "Wet-weather Driving": 80,
            "Cornering Style": "M"
        },
        "Yuki Tsunoda": {
            "Name": "Yuki Tsunoda",
            "Rating:": 83,
            "Race-pace": 85,
            "Carefulness": 80,
            "Wet-weather Driving": 81,
            "Cornering Style": "S"
        }
    },
    "HAAS": {
        "Nico Hulkenberg": {
            "Name": "Nico Hulkenberg",
            "Rating:": 84,
            "Race-pace": 80,
            "Carefulness": 86,
            "Wet-weather Driving": 86,
            "Cornering Style": "M"
        },
        "Kevin Magnussen": {
            "Name": "Kevin Magnussen",
            "Rating:": 84,
            "Race-pace": 86,
            "Carefulness": 82,
            "Wet-weather Driving": 84,
            "Cornering Style": "F"
        }
    },
    "Alfa Romeo": {
        "Valtteri Bottas": {
            "Name": "Valtteri Bottas",
            "Rating:": 88,
            "Race-pace": 87,
            "Carefulness": 89,
            "Wet-weather Driving": 88,
            "Cornering Style": "S"
        },
        "Guanyu Zhou": {
            "Name": "Guanyu Zhou",
            "Rating:": 80,
            "Race-pace": 84,
            "Carefulness": 76,
            "Wet-weather Driving": 80,
            "Cornering Style": "F"
        }
    },
    "Williams": {
        "Alex Albon": {
            "Name": "Alex Albon",
            "Rating:": 87,
            "Race-pace": 88,
            "Carefulness": 85,
            "Wet-weather Driving": 86,
            "Cornering Style": "M"
        },
        "Logan Sargeant": {
            "Name": "Logan Sargeant",
            "Rating:": 78,
            "Race-pace": 80,
            "Carefulness": 75,
            "Wet-weather Driving": 79,
            "Cornering Style": "S"
        }
    }


}
driver = ''
finish_lap_time = 0


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


car = pygame.image.load('car.png')
grass = scale_image(pygame.image.load('grass.jpeg'), 7)
track = scale_image(pygame.image.load('track.png'), 0.6)
track_border = scale_image(pygame.image.load('track_border.png'), 0.6)
track_bord_mask = pygame.mask.from_surface(track_border)
finish_line = scale_image(pygame.image.load('finish_line.jpeg'), 0.1)
finish_line_mask = pygame.mask.from_surface(finish_line)
fin_pos = (500, 640)
font = pygame.font.SysFont("monospace", 50)
images = [(grass, (0, 0)), (track, (0, 0)), (finish_line, (500, 640)), (track_border, (0, 0))]


def blit_rotate_ctr(screen, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    screen.blit(rotated_image, new_rect.topleft)


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

    def settings_menu(self, value):
        self.favourite_team = str(value)
        self.settings_win.show()
        return self.favourite_team

    def exit_menu(self):
        self.close()
        print("Exiting...")


class SettingsWindow(QMainWindow):

    def __init__(self):
        super(SettingsWindow, self).__init__()
        loadUi("SettingsMenu.ui", self)
        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.fav_team_set_lbl = self.findChild(QLabel, "fav_team_set_lbl")
        self.label2 = self.findChild(QLabel, "label_2")
        self.backbutton = self.findChild(QPushButton, "back_button")

        self.fav_team_set_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)

        self.slider.valueChanged.connect(self.slide_it)
        self.backbutton.clicked.connect(self.passing_favourite_team)

    def passing_favourite_team(self):

        self.close()

    def slide_it(self, value):

        if value == 0:
            value = 'Red Bull'
        elif value == 1:
            value = 'Ferrari'
        elif value == 2:
            value = 'Mercedes'
        elif value == 3:
            value = 'McLaren'
        elif value == 4:
            value = 'Alpine'
        elif value == 5:
            value = 'Alfa Romeo'
        elif value == 6:
            value = 'Aston Martin'
        elif value == 7:
            value = 'Alpha Tauri'
        elif value == 8:
            value = 'Haas'
        elif value == 9:
            value = 'Williams'
        self.fav_team_set_lbl.setText(str(value))
        # self.fav_team_set_lbl = str(value)
        return value

    def back_button_pressed(self):
        self.close()


class TeamSelectWindow(QMainWindow):

    def __init__(self):
        super(TeamSelectWindow, self).__init__()
        loadUi("TeamSelectMenu.ui", self)
        self.backButton = self.findChild(QPushButton, "backButton")
        self.fav_team_lbl = self.findChild(QLabel, "fav_team_lbl")
        self.rb_max_v_confirm = self.findChild(QPushButton, "max_v_cfm_but")
        self.rb_srg_p_confirm = self.findChild(QPushButton, "ser_p_cfm_but")
        self.mer_lew_h_confirm = self.findChild(QPushButton, "lew_h_cfm_but")
        self.mer_geo_r_confirm = self.findChild(QPushButton, "geo_r_cfm_but")
        self.fer_cha_l_confirm = self.findChild(QPushButton, "cha_l_cfm_but")
        self.fer_car_s_confirm = self.findChild(QPushButton, "car_s_cfm_but")
        self.mcl_lan_n_confirm = self.findChild(QPushButton, "lan_n_cfm_but")
        self.mcl_osc_p_confirm = self.findChild(QPushButton, "osc_p_cfm_but")
        self.alp_est_o_confirm = self.findChild(QPushButton, "est_o_cfm_but")
        self.alp_pie_g_confirm = self.findChild(QPushButton, "pie_g_cfm_but")
        self.ast_fer_a_confirm = self.findChild(QPushButton, "fer_a_cfm_but")
        self.ast_lan_s_confirm = self.findChild(QPushButton, "lan_s_cfm_but")
        self.rom_val_b_confirm = self.findChild(QPushButton, "val_b_cfm_but")
        self.rom_gua_z_confirm = self.findChild(QPushButton, "gua_z_cfm_but")
        self.tau_yuk_t_confirm = self.findChild(QPushButton, "yuk_t_cfm_but")
        self.tau_nyc_d_confirm = self.findChild(QPushButton, "nyc_d_cfm_but")
        self.haa_kev_m_confirm = self.findChild(QPushButton, "kev_m_cfm_but")
        self.haa_nic_h_confirm = self.findChild(QPushButton, "nic_h_cfm_but")
        self.wil_ale_a_confirm = self.findChild(QPushButton, "ale_a_cfm_but")
        self.wil_log_s_confirm = self.findChild(QPushButton, "log_s_cfm_but")

        self.SettingsMenu = SettingsWindow()
        self.SetUpScreen = SetUpScreen()


        self.fav_team_lbl.setText(driver)

        self.backButton.clicked.connect(self.back_to_main_menu)

        self.rb_max_v_confirm.clicked.connect(self.drv_confirmed), self.rb_max_v_confirm.clicked.connect(self.max_v)
        self.rb_srg_p_confirm.clicked.connect(self.drv_confirmed), self.rb_srg_p_confirm.clicked.connect(self.srg_p)
        self.mer_lew_h_confirm.clicked.connect(self.drv_confirmed), self.mer_lew_h_confirm.clicked.connect(self.lew_h)
        self.mer_geo_r_confirm.clicked.connect(self.drv_confirmed), self.mer_geo_r_confirm.clicked.connect(self.geo_r)
        self.fer_cha_l_confirm.clicked.connect(self.drv_confirmed), self.fer_cha_l_confirm.clicked.connect(self.cha_l)
        self.fer_car_s_confirm.clicked.connect(self.drv_confirmed), self.fer_car_s_confirm.clicked.connect(self.car_s)
        self.mcl_lan_n_confirm.clicked.connect(self.drv_confirmed), self.mcl_lan_n_confirm.clicked.connect(self.lan_n)
        self.mcl_osc_p_confirm.clicked.connect(self.drv_confirmed), self.mcl_osc_p_confirm.clicked.connect(self.osc_p)
        self.alp_est_o_confirm.clicked.connect(self.drv_confirmed), self.alp_est_o_confirm.clicked.connect(self.est_o)
        self.alp_pie_g_confirm.clicked.connect(self.drv_confirmed), self.alp_pie_g_confirm.clicked.connect(self.pie_g)
        self.ast_fer_a_confirm.clicked.connect(self.drv_confirmed), self.ast_fer_a_confirm.clicked.connect(self.fer_a)
        self.ast_lan_s_confirm.clicked.connect(self.drv_confirmed), self.ast_lan_s_confirm.clicked.connect(self.lan_s)
        self.rom_val_b_confirm.clicked.connect(self.drv_confirmed), self.rom_val_b_confirm.clicked.connect(self.val_b)
        self.rom_gua_z_confirm.clicked.connect(self.drv_confirmed), self.rom_gua_z_confirm.clicked.connect(self.gua_z)
        self.tau_yuk_t_confirm.clicked.connect(self.drv_confirmed), self.tau_yuk_t_confirm.clicked.connect(self.yuk_t)
        self.tau_nyc_d_confirm.clicked.connect(self.drv_confirmed), self.tau_nyc_d_confirm.clicked.connect(self.nyc_d)
        self.haa_kev_m_confirm.clicked.connect(self.drv_confirmed), self.haa_kev_m_confirm.clicked.connect(self.kev_m)
        self.haa_nic_h_confirm.clicked.connect(self.drv_confirmed), self.haa_nic_h_confirm.clicked.connect(self.nic_h)
        self.wil_ale_a_confirm.clicked.connect(self.drv_confirmed), self.wil_ale_a_confirm.clicked.connect(self.ale_a)
        self.wil_log_s_confirm.clicked.connect(self.drv_confirmed), self.wil_log_s_confirm.clicked.connect(self.log_s)

    def drv_confirmed(self):
        self.SetUpScreen.show()

    def max_v(self):
        global driver
        driver = drivers["Red Bull"]["Max Verstappen"]
        print(driver)

    def srg_p(self):
        global driver
        driver = drivers["Red Bull"]["Sergio Perez"]
        print(driver)

    def lew_h(self):
        global driver
        driver = drivers["Mercedes"]["Lewis Hamilton"]
        print(driver)

    def geo_r(self):
        global driver
        driver = drivers["Mercedes"]["George Russell"]
        print(driver)

    def cha_l(self):
        global driver
        driver = drivers["Ferrari"]["Charles Leclerc"]
        print(driver)

    def car_s(self):
        global driver
        driver = drivers["Ferrari"]["Carlos Sainz"]
        print(driver)

    def lan_n(self):
        global driver
        driver = drivers["McLaren"]["Lando Norris"]
        print(driver)

    def osc_p(self):
        global driver
        driver = drivers["McLaren"]["Oscar Piastri"]
        print(driver)

    def est_o(self):
        global driver
        driver = drivers["Alpine"]["Esteban Ocon"]
        print(driver)

    def pie_g(self):
        global driver
        driver = drivers["Alpine"]["Pierre Gasly"]
        print(driver)

    def fer_a(self):
        global driver
        driver = drivers["Aston Martin"]["Fernando Alonso"]
        print(driver)

    def lan_s(self):
        global driver
        driver = drivers["Aston Martin"]["Lance Stroll"]
        print(driver)

    def val_b(self):
        global driver
        driver = drivers["Alfa Romeo"]["Valtteri Bottas"]
        print(driver)

    def gua_z(self):
        global driver
        driver = drivers["Alfa Romeo"]["Guanyu Zhou"]
        print(driver)

    def yuk_t(self):
        global driver
        driver = drivers["Alpha Tauri"]["Yuki Tsunoda"]
        print(driver)

    def nyc_d(self):
        global driver
        driver = drivers["Alpha Tauri"]["Nyck de Vries"]
        print(driver)

    def kev_m(self):
        global driver
        driver = drivers["HAAS"]["Kevin Magnussen"]
        print(driver)

    def nic_h(self):
        global driver
        driver = drivers["HAAS"]["Nico Hulkenberg"]
        print(driver)

    def ale_a(self):
        global driver
        driver = drivers["Williams"]["Alex Albon"]
        print(driver)

    def log_s(self):
        global driver
        driver = drivers["Williams"]["Logan Sargeant"]
        print(driver)

    def back_to_main_menu(self):
        self.close()


class SetUpScreen(QMainWindow):

    def __init__(self):
        super(SetUpScreen, self).__init__()
        loadUi("SetUpScreen.ui", self)
        self.confirmbutton = self.findChild(QPushButton, "confirm_button")
        self.confirmbutton.clicked.connect(self.entering_race)
        self.lap_menu = LapFinishedMenu()
        self.race_sim = RaceSimulation()

    def entering_race(self):
        self.close()

        class Car():

            def __init__(self, top_vel, rot_vel):
                super().__init__()
                self.image = car
                self.top_vel = top_vel
                self.speed = 0.0
                self.rot_vel = rot_vel
                self.angle = 270.0
                self.x, self.y = (550, 650)
                self.accel = 10
                self.level_start_time = 0
                self.start = False

            def acc_forward(self):
                self.speed = min(self.speed + self.accel, self.top_vel)
                self.move()

            def move(self):
                rad = math.radians(self.angle)
                vert = math.cos(rad) * self.speed
                hor = math.sin(rad) * self.speed

                self.y -= vert
                self.x -= hor

            def decelerate(self):
                self.speed = max(self.speed - self.accel / 10, 0)
                self.move()

            def rotate(self, left=False, right=False):
                if left:
                    self.angle += self.rot_vel
                elif right:
                    self.angle -= self.rot_vel

            def draw(self, screen):
                blit_rotate_ctr(screen, self.image, (self.x, self.y), self.angle)

            def collide(self, mask, x=0, y=0):
                car_mask = pygame.mask.from_surface(car)
                offset = (int(self.x - x), int(self.y - y))
                poc = mask.overlap(car_mask, offset)
                return poc

            def bounce(self):
                self.speed = -self.speed * 3
                self.move()

            def rev_bounce(self):
                self.speed = -self.speed * 3
                self.move()

            def reverse(self):
                self.speed = max(self.speed - self.accel, -self.top_vel / 2)
                self.move()

            def restart(self):
                self.x, self.y = (550, 650)
                self.angle = 270.0
                self.speed = 0

            def start_level(self):
                self.start = True
                self.level_start_time = time.time()

            def lap_time(self):
                if not self.start:
                    return 0
                return round(time.time() - self.level_start_time)

        def main():

            pygame.init()

            screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
            pygame.display.set_caption("Race")
            car = Car(6, 6)
            clock = pygame.time.Clock()

            running = True
            while running:

                clock.tick(60)

                draw(screen, images, car)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break

                while not car.start:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            break
                        if event.type == pygame.KEYDOWN:
                            car.start_level()

                keys = pygame.key.get_pressed()
                track_collision = car.collide(track_bord_mask)
                finish_collision = car.collide(finish_line_mask, *fin_pos)
                moving = False

                if keys[pygame.K_LEFT]:
                    car.rotate(left=True)
                if keys[pygame.K_RIGHT]:
                    car.rotate(right=True)
                if keys[pygame.K_UP]:
                    moving = True
                    car.acc_forward()
                if keys[pygame.K_DOWN]:
                    car.reverse()
                    if finish_collision != None:
                        car.rev_bounce()
                    if track_collision != None:
                        car.rev_bounce()
                if not moving:
                    car.decelerate()
                if keys[pygame.K_x]:
                    pygame.quit()

                if car.collide(track_bord_mask) != None:
                    car.bounce()

                if finish_collision != None:
                    if finish_collision[0] == 24:
                        car.bounce()
                    else:
                        screen.fill(black)
                        global finish_lap_time
                        finish_lap_time = car.lap_time()
                        print(finish_lap_time)
                        break

            pygame.display.quit()

        def draw(screen, images, car):
            for img, pos in images:
                screen.blit(img, pos)
                time_text = font.render(f"Time: {car.lap_time()}s", 1, (255, 255, 255))
                screen.blit(time_text, (10, 700))

            car.draw(screen)
            pygame.display.update()

        if __name__ == "__main__":
            main()
        self.lap_finished()
        print(self.race_sim.ovr_driver_stat())

    def lap_finished(self):
        self.lap_menu.show()


class LapFinishedMenu(QMainWindow):
    def __init__(self):
        super(LapFinishedMenu, self).__init__()
        loadUi('LapFinishedMenu.ui', self)
        self.race_sim = RaceSimulation()


class RaceSimulation:

    def IsItRaining(self):
        global raining
        raining = False
        rain_chance = random.randint(1, 30)
        if rain_chance <= 4:
            raining = True
            print("It is raining")
        else:
            print("It is not")

    def ovr_driver_stat(self):
        if driver['Cornering Style'] == 'F':
            driver_style_ovr = 90
        elif driver['Cornering Style'] == 'M':
            driver_style_ovr = 95
        else:
            driver_style_ovr = 85
        driver_OVR = driver['Carefulness'] + driver['Wet-weather Driving'] + driver_style_ovr


    def UltimateRacePace(self):
        self.IsItRaining()
        if raining == True:
            race_pos = 6
            print(race_pos)



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.setFixedWidth(SCREENWIDTH)
    win.setFixedHeight(SCREENHEIGHT)
    app.exec_()
    sys.exit(app.exec_())


window()


