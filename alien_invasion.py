import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
import game_functions as gf
from scoreboard import Scoreboard


def run_game():
    #screen object
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #create instance to store game statistics
    stats=GameStats(ai_settings)
    #create scoreboard
    sb=Scoreboard(ai_settings,screen,stats)
    #make ship
    ship=Ship(ai_settings,screen)
    #make group of bullets
    bullets=Group()
    #make aliens
    aliens=Group()

    #fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #make play button
    play_button=Button(ai_settings,screen,"Play")

    pygame.mixer.music.load("music/music.mp3")
    pygame.mixer.music.play(-1)

    #loop of game
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
