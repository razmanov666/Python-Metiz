import pygame
from time import sleep

class Ship():
    """
    A class to manage the ship.
    """

    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.settings = ai_settings
        self.screen_rect = screen.get_rect()

        # Загрузка изображения корабля.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.centerx = float(self.rect.x)
        self.centery = float(self.rect.y)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        # Обновляется атрибут center, не rect.
        self.update_icon()
        self.screen_rect = self.screen.get_rect()
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def update_icon(self):
        """Изменение иконки для имитации анимации."""
        if self.moving_right:
            if self.moving_up:
                self.image = pygame.image.load('images/ship_move_up_right.bmp')
            elif self.moving_down:
                self.image = pygame.image.load(
                    'images/ship_move_down_right.bmp')
            else:
                self.image = pygame.image.load('images/ship_move_right.bmp')

        if self.moving_left:
            if self.moving_up:
                self.image = pygame.image.load('images/ship_move_up_left.bmp')
            elif self.moving_down:
                self.image = pygame.image.load(
                    'images/ship_move_down_left.bmp')
            else:
                self.image = pygame.image.load('images/ship_move_left.bmp')
        if (self.moving_down and self.moving_right == False
                and self.moving_left == False):
            self.image = pygame.image.load('images/ship_move_down.bmp')
        elif (self.moving_up and self.moving_right == False
              and self.moving_left == False):

            self.image = pygame.image.load('images/ship.bmp')

    # def restore_icon(self):
    #     """
    #     Возвращение иконки для имитации анимации.
    #     """
    #     self.image = pygame.image.load('images/ship.bmp')

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def reset_pos_ship(self):
        self.midbottom = self.screen_rect.midbottom

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.image = pygame.image.load('images/ship.bmp')
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - 700

