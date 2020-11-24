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

    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()