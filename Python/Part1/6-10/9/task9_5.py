from task9_3_class import *

kurama666 = User('alexey', 'razmanov', 'kurama666', '1234')
print(kurama666.login_attempts)
kurama666.incriment_login_attepmts()
kurama666.incriment_login_attepmts()
kurama666.incriment_login_attepmts()
kurama666.incriment_login_attepmts()
print(kurama666.login_attempts)
kurama666.reset_login_attepmts()
print(kurama666.login_attempts)