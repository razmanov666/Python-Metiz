class User():
    """Класс хранящий данные о пользователе"""
    def __init__(self, first_name='1', last_name='1',
                 username='1', password='1'):
        self.first = first_name
        self.last = last_name
        self.username = username
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        """Вывод данных хранящихся в экземпляре"""
        print ("Name is " + self.first.title() + ' ' + self.last.title() + 
                '\nLogin is: ' + "'" + self.username + "'" + 
                ', password is: ' + "'" + self.password + "'\n")
        
    def greet_user(self):
        """Приветствие пользователя"""
        print (self.first.title() + ", nice to meet you!")

    def incriment_login_attepmts(self):
        """"Увеличение количества попыток входа"""
        self.login_attempts += 1

    def reset_login_attepmts(self):
        """Обнуление попыток входа"""
        self.login_attempts = 0    