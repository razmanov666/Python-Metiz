class Settings(object):
    """
    Класс для хранения всех настроек игры 'Alien Invasion'
    """
    def __init__(self):
        """
        Инициализирует настройки игры
        """
        # Настройки корабля
        self.ship_speed_factor = 1.5

        # Параметры экрана
        self.screen_width = 1366
        self.screen_height = 710
        self.bg_color = (0, 100, 255)