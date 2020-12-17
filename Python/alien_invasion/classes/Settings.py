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
        self.ship_limit = 3

        # Параметры пули
        self.bullet_speed = 7
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (250 , 60, 0)
        self.bullets_allowed = 3

        # Параметры экрана
        self.screen_width = 1366
        self.screen_height = 720
        self.bg_color = (10, 10, 10)

        # Настройка пришельцев
        self.start_alied_speed_factor = 1 
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        self.speed_increment = 1.25
        # fleet_direction = 1 обозначает движение вправо, а -1 влево.
        self.fleet_direction = 1
