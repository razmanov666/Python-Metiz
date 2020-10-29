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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                (ai_settings.screen_width, ai_settings.screen_height)
                            ,pygame.FULLSCREEN)
=======
                (ai_settings.screen_width, ai_settings.screen_height), 
                                pygame.FULLSCREEN)
>>>>>>> d8d5ea5... Revert "Merge pull request #7 from razmanov666/master"
=======
                (ai_settings.screen_width, ai_settings.screen_height)
                            ,pygame.FULLSCREEN)
>>>>>>> e076e80... feat: add alien & fix git trouble
=======
                (ai_settings.screen_width, ai_settings.screen_height), 
                                pygame.FULLSCREEN)
>>>>>>> 20360ec... Revert "Merge pull request #7 from razmanov666/master"
=======
                (ai_settings.screen_width, ai_settings.screen_height)
                            ,pygame.FULLSCREEN)
>>>>>>> 1f7a2aa... feat: add alien & fix git trouble
=======
                (ai_settings.screen_width, ai_settings.screen_height))
<<<<<<< HEAD
>>>>>>> b38a3e9... fix FULLscr problem
=======
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
>>>>>>> a7f71e8... clean
=======
>>>>>>> b0c51c1... Revert "Merge branch 'master' into modifed"
        
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        gf.update_screen(ai_settings, screen, ship, bullets, hero)
=======
=======
>>>>>>> 20360ec... Revert "Merge pull request #7 from razmanov666/master"
        gf.update_screen(ai_settings, screen, ship, bullets)
>>>>>>> d8d5ea5... Revert "Merge pull request #7 from razmanov666/master"
=======
        gf.update_screen(ai_settings, screen, ship, bullets, hero)
>>>>>>> e076e80... feat: add alien & fix git trouble
=======
        gf.update_screen(ai_settings, screen, ship, bullets, hero)
<<<<<<< HEAD
>>>>>>> 1f7a2aa... feat: add alien & fix git trouble
=======
        # ship.restore_icon()
>>>>>>> e086ba9... add: some move animation

run_game()