import sys
import pygame
sys.path.insert(0, 'classes')
sys.path.insert(1, 'moduls')
import game_functions as gf
from Character import Character
from pygame.sprite import Group
from Ship import Ship
from Alien import Alien
from Settings import Settings
from Game_stats import GameStats
from Button import Button
from Scoreboard import Scoreboard
from time import sleep


def run_game():
    """Инициализирует pygame, setting и объект экрана."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
                    (ai_settings.screen_width, ai_settings.screen_height) 
                                        #,pygame.FULLSCREEN
                                        )
    pygame.display.set_caption("Alien Invasion")

    # Создание объектов.
    ship = Ship(ai_settings, screen)

    # Создание группы хранения пуль.
    bullets = Group()
    #hero = Character(screen)

    # Создание пришельца.
    #alien = Alien(ai_settings, screen)
    aliens = Group()

    # Создание экземпляра игровой статистики и счета.
    stats = GameStats(ai_settings) 
    sb = Scoreboard(ai_settings, screen, stats)

    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "PLAY")

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, stats, sb, screen, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, 
                                            ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, stats, sb, screen, ship, bullets, aliens, 
            play_button)

run_game()