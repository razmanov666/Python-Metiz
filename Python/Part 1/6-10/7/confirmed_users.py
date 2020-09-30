unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
for user in confirmed_users:
    print(user.title())
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Верефицированный пользователь: ' + current_user.title())
    confirmed_users.append(current_user)
print('\nПроверенные пользователи:\n')
for user in confirmed_users:
    print(user.title())