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
        self.image = pygame.image.load("images/hero_sashka_small.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Сашка появляется по центру
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    def blitme(self):
        """
        Рисует Сашку в текущей позиции.
        """
        self.screen.blit(self.image, self.rect)