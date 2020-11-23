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


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """
    Обновление пуль на экране.
    """

    bullets.update()
    # Удаление пуль вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, aliens, ship, bullets)


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

def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет кол-во рядов, помещающихся на экране."""
    available_space_y = (ai_settings.screen_height -
                        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    #alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление кол-ва пришельцев в ряду.
    #ai_settings.alien_speed_factor *= ai_settings.speed_increment
    alien = Alien(ai_settings, screen)
    number_aliens_x = 1
    number_rows = 1

    # Создание флота пришельцев.
    # for row_number in range(number_rows):
    #     for alien_number in range(number_aliens_x):
    #         # Создание пришельца и размещение его в ряду.
    aliens.empty()
    create_alien(ai_settings, screen, aliens, 1, 1)

def check_bullet_alien_collisions(ai_settings, screen, aliens, ship, bullets):
    """Обработка коллизий пуль с пришельцами."""
    # Проверка попадания в пришельцев.
    # При обнаружениии попадания удалить пулю и пришельца.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if not aliens:
        # Удаление пуль и пришельцев участвующих в коллизиях.
        # Уничтожение существующих пуль и создание новго флота.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def сheck_fleet_edges(ai_settings, screen, ship, aliens):
    """Реагирует на достижение пришельцем края экрана."""
    for alien in aliens.sprites():
        if alien.check_edges() or alien.rect.bottom == ship.rect.top:
            create_fleet(ai_settings, screen, ship, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Опускает весь флот и меняет направление  флота."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, screen, ship, aliens):
    """
    Проверяет достиг ли флот края экрана,
    после чего обновляет позицию всех пришельцев во флоте.
    """
    сheck_fleet_edges(ai_settings, screen, ship, aliens)
    aliens.update()