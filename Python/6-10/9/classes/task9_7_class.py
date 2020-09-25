import sys
sys.path.insert(0, '/home/kurama/Документы/Training/Python/6-10/9/classes')
from task9_3_class import *

class Privileges():
    """Привилегии пользователя."""
    def __init__(self):
      self.privileges = [
                        'разрешено добавлять сообщения',
                        'разрешено удалять пользователей', 
                        'разрешено банить пользователей'
                        ]
    def show_privileges(self):
        print(self.privileges)
    
class Admin(User):
    """Класс представляющий администратора"""
    def __init__(self, first_name='1', last_name='1',
                 username='1', password='1'):
        super().__init__(first_name, last_name, username, password)
        self.privileges = Privileges()
    
