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


def run_game():
    """Инициализирует pygame, setting и объект экрана."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
                (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание объектов.
    ship = Ship(ai_settings, screen)

    # Создание группы хранения пуль.
    bullets = Group()
    hero = Character(screen)

    # Создание пришельца.
    alien = Alien(ai_settings, screen)
    aliens = Group()

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()