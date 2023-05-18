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


# for cornering style, F is for fast cornering, M is for medium cornering, S is for slow cornering

drivers = {
    "Mercedes": {
        "Lewis Hamilton": {
            "Name": "Lewis Hamilton",        # this is the name of the driver, which will print above the confirm button
            "Rating": 95,                    # this is the overall rating of the driver
            "Race-pace": 96,                 # this is the race-pace of the driver ( how fast they are )
            "Carefulness": 96,               # this is the carefulness of the driver ( how likely they are to crash )
            "Wet-weather Driving": 92,       # this is the wet-weather skill ( their skill in the rain )
            "Cornering Style": "F"           # this is the cornering style, as mentioned above
        },
        "George Russell": {
            "Name": "George Russell",
            "Rating": 89,
            "Race-pace": 93,
            "Carefulness": 84,
            "Wet-weather Driving": 90,
            "Cornering Style": "M"
        }
    },

    "Red Bull": {
        "Max Verstappen": {
            "Name": "Max Verstappen",
            "Rating": 97,
            "Race-pace": 99,
            "Carefulness": 92,
            "Wet-weather Driving": 99,
            "Cornering Style": "F"
        },
        "Sergio Perez": {
            "Name": "Sergio Perez",
            "Rating": 88,
            "Race-pace": 82,
            "Carefulness": 95,
            "Wet-weather Driving": 87,
            "Cornering Style": "S"
        }
    },

    "Ferrari": {
        "Charles Leclerc": {
            "Name": "Charles Leclerc",
            "Rating": 91,
            "Race-pace": 94,
            "Carefulness": 90,
            "Wet-weather Driving": 88,
            "Cornering Style": "M"
        },
        "Carlos Sainz": {
            "Name": "Carlos Sainz",
            "Rating": 88,
            "Race-pace": 85,
            "Carefulness": 87,
            "Wet-weather Driving": 92,
            "Cornering Style": "F"
        }
    },

    "McLaren": {
        "Lando Norris": {
            "Name": "Lando Norris",
            "Rating": 90,
            "Race-pace": 93,
            "Carefulness": 87,
            "Wet-weather Driving": 90,
            "Cornering Style": "M"
        },
        "Oscar Piastri": {
            "Name": "Oscar Piastri",
            "Rating": 82,
            "Race-pace": 86,
            "Carefulness": 78,
            "Wet-weather Driving": 82,
            "Cornering Style": "F"
        }
    },

    "Aston Martin": {
        "Fernando Alonso": {
            "Name": "Fernando Alonso",
            "Rating": 91,
            "Race-pace": 89,
            "Carefulness": 92,
            "Wet-weather Driving": 92,
            "Cornering Style": "S"
        },
        "Lance Stroll": {
            "Name": "Lance Stroll",
            "Rating": 85,
            "Race-pace": 85,
            "Carefulness": 83,
            "Wet-weather Driving": 87,
            "Cornering Style": "M"
        }
    },
    "Alpine": {
        "Esteban Ocon": {
            "Name": "Esteban Ocon",
            "Rating": 86,
            "Race-pace": 88,
            "Carefulness": 83,
            "Wet-weather Driving": 87,
            "Cornering Style": "S"
        },
        "Pierre Gasly": {
            "Name": "Pierre Gasly",
            "Rating": 87,
            "Race-pace": 87,
            "Carefulness": 85,
            "Wet-weather Driving": 89,
            "Cornering Style": "F"
        }
    },
    "Alpha Tauri": {
        "Nyck de Vries": {
            "Name": "Nyck de Vries",
            "Rating": 80,
            "Race-pace": 83,
            "Carefulness": 77,
            "Wet-weather Driving": 80,
            "Cornering Style": "M"
        },
        "Yuki Tsunoda": {
            "Name": "Yuki Tsunoda",
            "Rating": 83,
            "Race-pace": 85,
            "Carefulness": 80,
            "Wet-weather Driving": 81,
            "Cornering Style": "S"
        }
    },
    "HAAS": {
        "Nico Hulkenberg": {
            "Name": "Nico Hulkenberg",
            "Rating": 84,
            "Race-pace": 80,
            "Carefulness": 86,
            "Wet-weather Driving": 86,
            "Cornering Style": "M"
        },
        "Kevin Magnussen": {
            "Name": "Kevin Magnussen",
            "Rating": 84,
            "Race-pace": 86,
            "Carefulness": 82,
            "Wet-weather Driving": 84,
            "Cornering Style": "F"
        }
    },
    "Alfa Romeo": {
        "Valtteri Bottas": {
            "Name": "Valtteri Bottas",
            "Rating": 88,
            "Race-pace": 87,
            "Carefulness": 89,
            "Wet-weather Driving": 88,
            "Cornering Style": "S"
        },
        "Guanyu Zhou": {
            "Name": "Guanyu Zhou",
            "Rating": 80,
            "Race-pace": 84,
            "Carefulness": 76,
            "Wet-weather Driving": 80,
            "Cornering Style": "F"
        }
    },
    "Williams": {
        "Alex Albon": {
            "Name": "Alex Albon",
            "Rating": 87,
            "Race-pace": 88,
            "Carefulness": 85,
            "Wet-weather Driving": 86,
            "Cornering Style": "M"
        },
        "Logan Sargeant": {
            "Name": "Logan Sargeant",
            "Rating": 78,
            "Race-pace": 80,
            "Carefulness": 75,
            "Wet-weather Driving": 79,
            "Cornering Style": "S"
        }
    }


}
driver = ''
finish_lap_time = 0
quali_lap_finished = False
raining = False
driver_OVR = 0
fav_team = ''
int_value_frt_wing = 30
int_value_rear_wing = 75
int_value_brake_prs = 50
int_value_frt_tyre_prs = 22
int_value_rear_tyre_prs = 20
set_up_rat = 0
driver_conf = 0
tip = ''


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
        self.settings_win.show()

    def exit_menu(self):
        sys.exit()


class SettingsWindow(QMainWindow):

    def __init__(self):
        super(SettingsWindow, self).__init__()
        loadUi("SettingsMenu.ui", self)
        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.fav_team_set_lbl = self.findChild(QLabel, "fav_team_set_lbl")
        self.backbutton = self.findChild(QPushButton, "back_button")

        self.fav_team_set_lbl.setAlignment(QtCore.Qt.AlignCenter)

        self.slider.valueChanged.connect(self.slide_it)
        self.backbutton.clicked.connect(self.passing_favourite_team)

    def passing_favourite_team(self):
        self.close()

    def slide_it(self, value):
        global fav_team
        if value == 0:
            fav_team = 'Red Bull'
        elif value == 1:
            fav_team = 'Ferrari'
        elif value == 2:
            fav_team = 'Mercedes'
        elif value == 3:
            fav_team = 'McLaren'
        elif value == 4:
            fav_team = 'Alpine'
        elif value == 5:
            fav_team = 'Alfa Romeo'
        elif value == 6:
            fav_team = 'Aston Martin'
        elif value == 7:
            fav_team = 'Alpha Tauri'
        elif value == 8:
            fav_team = 'Haas'
        elif value == 9:
            fav_team = 'Williams'
        self.fav_team_set_lbl.setText(str(fav_team))

    def back_button_pressed(self):
        self.close()


class TeamSelectWindow(QMainWindow):

    def __init__(self):
        super(TeamSelectWindow, self).__init__()
        loadUi("TeamSelectMenu.ui", self)
        self.backButton = self.findChild(QPushButton, "backButton")
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
        self.frt_wing_sld = self.findChild(QSlider, "frt_wing_slider")
        self.frt_wing_lbl = self.findChild(QLabel, "frt_wing_lbl")
        self.rear_wing_sld = self.findChild(QSlider, "rear_wing_slider")
        self.rear_wing_lbl = self.findChild(QLabel, "rear_wing_lbl")
        self.brake_prs_sld = self.findChild(QSlider, "brake_prs_slider")
        self.brake_prs_lbl = self.findChild(QLabel, "brake_prs_lbl")
        self.frt_tyre_prs_sld = self.findChild(QSlider, "frt_tyre_prs_slider")
        self.frt_tyre_prs_lbl = self.findChild(QLabel, "frt_tyre_prs_lbl")
        self.rear_tyre_prs_sld = self.findChild(QSlider, "rear_tyre_prs_slider")
        self.rear_tyre_prs_lbl = self.findChild(QLabel, "rear_tyre_prs_lbl")
        self.confirmbutton = self.findChild(QPushButton, "confirm_button")
        self.drv_cfm_but = self.findChild(QPushButton, "driver_conf_but")
        self.drv_cfm_lbl = self.findChild(QLabel, "driver_conf_lbl")
        self.confirmbutton.clicked.connect(self.entering_race)
        self.drv_cfm_but.clicked.connect(self.driver_conf)
        self.lap_menu = LapFinishedMenu()
        self.race_sim = RaceSimulation()

        self.frt_wing_sld.valueChanged.connect(self.frt_wing_sld_change)
        self.rear_wing_sld.valueChanged.connect(self.rear_wing_sld_change)
        self.brake_prs_sld.valueChanged.connect(self.brake_prs_sld_change)
        self.frt_tyre_prs_sld.valueChanged.connect(self.frt_tyre_prs_sld_change)
        self.rear_tyre_prs_sld.valueChanged.connect(self.rear_tyre_prs_sld_change)

    def frt_wing_sld_change(self, value_frt_wing):
        global int_value_frt_wing
        str_value_frt_wing = str(value_frt_wing) + "mm"
        int_value_frt_wing = int(value_frt_wing)
        self.frt_wing_lbl.setText(str_value_frt_wing)
        return int_value_frt_wing

    def rear_wing_sld_change(self, value_rear_wing):
        global int_value_rear_wing
        str_value_rear_wing = str(value_rear_wing) + "mm"
        int_value_rear_wing = int(value_rear_wing)
        self.rear_wing_lbl.setText(str_value_rear_wing)
        return int_value_rear_wing

    def brake_prs_sld_change(self, value_brake_prs):
        global int_value_brake_prs
        str_value_brake_prs = str(value_brake_prs) + "%"
        int_value_brake_prs = int(value_brake_prs)
        self.brake_prs_lbl.setText(str_value_brake_prs)
        return int_value_brake_prs

    def frt_tyre_prs_sld_change(self, value_frt_tyre_prs):
        global int_value_frt_tyre_prs
        str_value_frt_tyre_prs = str(value_frt_tyre_prs) + "PSI"
        int_value_frt_tyre_prs = int(value_frt_tyre_prs)
        self.frt_tyre_prs_lbl.setText(str_value_frt_tyre_prs)
        return int_value_frt_tyre_prs

    def rear_tyre_prs_sld_change(self, value_rear_tyre_prs):
        global int_value_rear_tyre_prs
        str_value_rear_tyre_prs = str(value_rear_tyre_prs) + "PSI"
        int_value_rear_tyre_prs = int(value_rear_tyre_prs)
        self.rear_tyre_prs_lbl.setText(str_value_rear_tyre_prs)
        return int_value_rear_tyre_prs

    def driver_conf(self):
        self.race_sim.set_up_lvl()
        self.drv_cfm_lbl.setText(str(driver_conf) + "%")

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
            car = Car(7, 7)
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
        self.race_sim.IsItRaining()
        self.race_sim.set_up_lvl()
        self.race_sim.ovr_driver_stat()
        self.race_sim.UltimateRacePace()
        self.lap_finished()

    def lap_finished(self):
        self.lap_menu.show()


class LapFinishedMenu(QMainWindow):
    def __init__(self):
        super(LapFinishedMenu, self).__init__()
        loadUi('LapFinishedMenu.ui', self)
        self.tip_lbl = self.findChild(QLabel, "tip_label")
        self.tip_but = self.findChild(QPushButton, "tip_but")
        self.exit_but = self.findChild(QPushButton, "exit_but")

        self.tip_but.clicked.connect(self.set_tip_lbl)
        self.exit_but.clicked.connect(self.exit_but_clck)

    def set_tip_lbl(self):

        tip_to_show = str(tip)
        self.tip_lbl.setText(tip_to_show)

    def exit_but_clck(self):
        sys.exit()


class RaceSimulation:

    def __init__(self):
        self.lap_fin_menu = LapFinishedMenu()
        self.tip_menu = Tip_Selection_Menu()
        self.frt_wing_rat = 0
        self.rear_wing_rat = 0
        self.brake_prs_rat = 0
        self.frt_tyre_prs_rat = 0
        self.rear_tyre_prs_rat = 0

    def IsItRaining(self):
        global raining
        rain_chance = random.randint(1, 30)
        if rain_chance <= 5:
            raining = True
        else:
            raining = False

    def set_up_lvl(self):
        if int_value_frt_wing > 34:
            self.frt_wing_rat = 85
        elif int_value_frt_wing < 34:
            self.frt_wing_rat = 90
        else:
            self.frt_wing_rat = 100

        if int_value_rear_wing > 76:
            self.rear_wing_rat = 90
        elif int_value_rear_wing < 76:
            self.rear_wing_rat = 85
        else:
            self.rear_wing_rat = 100

        if int_value_brake_prs > 87:
            self.brake_prs_rat = 80
        elif int_value_brake_prs < 87:
            self.brake_prs_rat = 85
        else:
            self.brake_prs_rat = 100

        if int_value_frt_tyre_prs > 22:
            self.frt_tyre_prs_rat = 85
        else:
            self.frt_tyre_prs_rat = 100

        if int_value_rear_tyre_prs > 22:
            self.rear_tyre_prs_rat = 90
        elif int_value_rear_tyre_prs < 22:
            self.rear_tyre_prs_rat = 85
        else:
            self.rear_tyre_prs_rat = 100

        global set_up_rat
        global driver_conf
        set_up_rat = self.frt_wing_rat + self.rear_wing_rat + self.brake_prs_rat + self.frt_tyre_prs_rat + self.rear_tyre_prs_rat
        driver_conf = set_up_rat // 5

    def ovr_driver_stat(self):

        if driver['Cornering Style'] == 'F':
            driver_style_ovr = 90
        elif driver['Cornering Style'] == 'M':
            driver_style_ovr = 95
        else:
            driver_style_ovr = 85
        global driver_OVR
        driver_OVR = int(driver['Rating']) + int(driver['Race-pace']) + int(driver['Carefulness']) + int(driver['Wet-weather Driving']) + driver_style_ovr

    def UltimateRacePace(self):
        global tip
        if set_up_rat > 490:                # perfect set up is 34,76,87,22,22
            self.tip_menu.win_from_set_up()
            self.lap_fin_menu.set_tip_lbl()
        elif raining == False and driver_OVR > 450:
            self.tip_menu.winning()
            self.lap_fin_menu.set_tip_lbl()
        elif raining == True and driver_OVR > 450 and set_up_rat >= 470:
            self.tip_menu.loss_due_to_rain()
            self.lap_fin_menu.set_tip_lbl()
        elif raining == True and driver_OVR > 450 and set_up_rat < 470:
            self.tip_menu.set_up_crash()
            self.lap_fin_menu.set_tip_lbl()
        elif raining == True and driver_OVR < 450:
            self.tip_menu.driver_ovr_crash()
            self.lap_fin_menu.set_tip_lbl()
        elif raining == False and driver_OVR < 450 and set_up_rat > 470:
            self.tip_menu.podium()
            self.lap_fin_menu.set_tip_lbl()
        else:
            pass


class Tip_Selection_Menu:
    def win_from_set_up(self):
        global tip
        tip = "You should sign yourself up to work in F1, you set-up the car so beautifully, no matter what weather " \
              "it was and what driver you were, you still won the race! "

    def loss_due_to_rain(self):
        global tip
        tip = "Unlucky buddy, these things happen in the unpredictable world of F1, it rained which means your driver " \
              "span out, he recovered it due to your set up choice but he didn't win like he could have. "

    def winning(self):
        global tip
        tip = "Well done you won! You got lucky however, it wasn't raining and your driver is very skilled, " \
              "as a result of this, he won the race without your help, but next time you should set up the car better. "

    def set_up_crash(self):
        global tip
        tip = "Oh no, your driver was skilled enough in the rain but your car was not set-up in the correct way, " \
              "so he crashed out of the race, leading to his rival winning. "

    def driver_ovr_crash(self):
        global tip
        tip = "It was raining, and your driver wasn't skilled enough in the rain to drive, so crashed out, no matter " \
              "how you set up the car "

    def podium(self):
        global tip
        tip = "Your driver isn't skilled enough to get the win, but the car was set up so well that you managed to " \
              "get your driver a podium. "


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.setFixedWidth(SCREENWIDTH)
    win.setFixedHeight(SCREENHEIGHT)
    app.exec_()
    sys.exit(app.exec_())


window()


