import sys
import pygame
sys.path.insert(0, 'classes')
sys.path.insert(1, 'moduls')
from Settings import Settings
from Ship import Ship
from Character import Character
import game_functions as gf


def run_game():
    """Инициализирует pygame, setting и объект экрана"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание объектов
    ship = Ship(ai_settings ,screen)
    hero = Character(screen)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, hero)

run_game()