import sys
import pygame
sys.path.append('classes')
from Alien import Alien
from Bullet import Bullet


def check_keydown_events(event, ship, screen, ai_settings, bullets):
    """
    Реагирует на нажитие клавиш.
    """
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
        fire_bullet(ai_settings, screen, ship, bullets)


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


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """
    Отрисовывает изображение на экране.
    """
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    # Все пули отрисовываются позади изображений корабля и пришельцев.
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # hero.blitme()
    # Отображаение последнего прорисованного экрана.
    pygame.display.flip()


def update_bullets(bullets):
    """
    Обновление пуль на экране.
    """
    bullets.update()
    # Удаление пуль вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """
    Выпускает пулю, если максимум еще не достигнут.
    """
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)   

def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет кол-во пришельцев в ряду."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление кол-ва пришельцев в ряду.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    # Создание первого ряда пришельцев.
    for alien_number in range(number_aliens_x):
        # Создание пришельца и размещение его в ряду.
        create_alien(ai_settings, screen, aliens, alien_number)
     