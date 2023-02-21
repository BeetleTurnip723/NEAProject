'''
NEA Year 12 Project
Author: Joe Sykes
Date Started: 9/9/22
Idea:
My idea for my NEA is to make a formula one set-up simulator where you get randomised a track, and either if it is raining or not, and you choose your driver and try to create the perfect set-up for them to win the race
'''
# automake the other drivers set-ups and then give a recommendation to the reader to say what they can do better
import PyQt5
import pygame

# for cornering, F is for fast cornering, M is for medium cornering, S is for slow cornering

drivers = {
    "Mercedes": {
        "Lewis Hamilton": {
            "95",               # OVR
            "96",               # Pace
            "96",               # Carefulness
            "92",               # Wet-weather Driving
            "F"                 # Cornering Style
        },
        "George Russell": {
            "89",               # OVR
            "93",               # Pace
            "84",               # Carefulness
            "90",               # Wet-weather Driving
            "M"                 # Cornering Style
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
        }
    },


}
