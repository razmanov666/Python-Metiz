class Settings():
    """
    Класс для хранения всех настроек игры 'Alien Invasion'
    """
    def __init__(self):
        """
        Инициализирует настройки игры
        """
        # Настройки корабля
        self.ship_speed_factor = 3

        # Параметры пули
        self.bullet_speed = 7
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (250 , 60, 0)
        self.bullets_allowed = 3

        # Параметры экрана
        self.screen_width = 1366
        self.screen_height = 720
<<<<<<< HEAD
        self.bg_color = (0 , 60, 70)
=======
        self.screen_height = 740
        self.bg_color = (0, 0, 0)
>>>>>>> a7f71e8... clean
=======
        self.bg_color = (0 , 60, 70)
>>>>>>> b0c51c1... Revert "Merge branch 'master' into modifed"
