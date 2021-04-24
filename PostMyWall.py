# Приложение отправляет пост длиной не более 140 символов на Вашу стену Вконтакте
# Для работы приложения необходимо создать свое Standalone приложение Вконтакте на сайте https://vk.com/dev

import requests

method = 'https://api.vk.com/method/wall.post'
profile_id = ID
token = 'VK_TOKEN'  # токен приложения Вконтакте
txt = input("Введите текст поста\n")
version = '5.130'

if len(txt) > 140:
    print("Ошибка! Длина сообщения больше 140 символов.")
else:
    data = dict(owner_id=profile_id, access_token=token, message=txt, v=version)
    r = requests.post(method, data).json()
    print(r)
    print('Пост', txt, 'опубликован')
