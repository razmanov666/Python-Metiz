import pygame

class Character():
    """
    Класс персонажа.
    """
    def __init__(self, screen):
        """
        Инициализирует и задает начальную позицию персонажа.
        """
        self.screen = screen

        # Загрузка изображения Сашки
        self.image = pygame.image.load("images/hero_sashka.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Сашка появляется по центру
        self.rect.center = self.screen_rect.center
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        """
        Рисует Сашку в текущей позиции.
        """
        self.screen.blit(self.image, self.rect)