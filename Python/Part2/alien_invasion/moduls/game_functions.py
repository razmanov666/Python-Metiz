import sys
import pygame
sys.path.append('/home/kurama/Документы/Training/Python/Part2/alien_invasion/classes')
from Bullet import Bullet

def check_keydown_events(event, ship, screen, ai_settings, bullets):
    """
    Реагирует на нажитие клавиш.
    """
    # print('event is ' + str(type(event)))
    # print('ship is ' + str(type(ship)))
    # print('ai_settings is ' + str(type(ai_settings)))
    # print('screen is ' + str(type(screen)))
    # print('bullets is ' + str(type(bullets)))
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True 
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    if event.key == pygame.K_SPACE:
        # Создание новой пули и включение ее в группу
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """
    Реагирует на отпускание клавиш.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    

def check_events(ai_settings, screen, ship, bullets):
    """
    Обрабатывает нажатия клавиш и движение мыши.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, screen, ai_settings, bullets)
        

def update_screen(ai_settings, screen, ship, bullets):
    """
    Отрисовывает изображение на экране.
    """
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    # Все пули отрисовываются позади изображений корабля и пришельцев.
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    # hero.blitme()
    # Отображаение последнего прорисованного экрана.
    pygame.display.flip()