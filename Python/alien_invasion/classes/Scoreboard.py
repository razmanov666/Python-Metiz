import pygame.font

class Scoreboard():
    """Класс для вывода игровой информации."""
    def __init__(self, ai_setting, screen, stats):
        """Инициализирует атрибуты подсчета очков."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.ai_settings = ai_setting

        # Настройка шрифта для вывода счета.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка исходного изображения.
        self.prep_score()
    
    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        rounded_score = int(round(self.stats.score, -3))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                    self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top
    
    def show_score(self):
        """Выводит счет на экран."""
        self.screen.blit(self.score_image, self.score_rect)