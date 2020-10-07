import sys
import pygame
sys.path.insert(0, 'classes')
sys.path.insert(1, 'moduls')
from Settings import Settings
from Ship import Ship
from pygame.sprite import Group
from Character import Character
import game_functions as gf


def run_game():
    """Инициализирует pygame, setting и объект экрана"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
<<<<<<< HEAD
                (ai_settings.screen_width, ai_settings.screen_height)
                            ,pygame.FULLSCREEN)
=======
                (ai_settings.screen_width, ai_settings.screen_height), 
                                pygame.FULLSCREEN)
>>>>>>> d8d5ea5... Revert "Merge pull request #7 from razmanov666/master"
        
    pygame.display.set_caption("Alien Invasion")

    # Создание объектов
    ship = Ship(ai_settings, screen)

    # Создание группы хранения пуль
    bullets = Group()
    hero = Character(screen)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
<<<<<<< HEAD
        gf.update_screen(ai_settings, screen, ship, bullets, hero)
=======
        gf.update_screen(ai_settings, screen, ship, bullets)
>>>>>>> d8d5ea5... Revert "Merge pull request #7 from razmanov666/master"

run_game()