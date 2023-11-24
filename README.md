# Referral_System
Простая реферальная система с авторизацией по номеру телефона. Проект доступен по ip: 127.0.0.1:8000.

Команды:

- docker-compose up --build - запуск проекта.

API:

- Авторизация по номеру телефона.
POST http://127.0.0.1:8000/users/auth/ - нужно указать номер телефона с ключом "number" в JSON формате. 
Имитируется отправка смс на телефон(код виден в консоли) для авторизации;

- Подтверждение кода.
POST http://127.0.0.1:8000/users/auth/verify/ - нужно указать номер телефона с ключом "number" и 
полученный код с ключом "verify_code" в JSON формате. Ответ предоставляется в виде "access_token", для
распознвания системой пользователя, который был авторезирован;

- Запрос на профиль пользователя.
GET http://127.0.0.1:8000/users/profile/user_id/ - на месте user_id нужно указать id авторизированного пользователя.
Если зайти на профиль не авторезированным или авторезированным, но на чужой профиль, то в доступе будет отказано.
В профиле выводятся номер телефона, личный инвайт-код, инвайт-код, который принадлежит другому пользователю(пригласившему),
если он был введен, список номеров приглашенных пользователей по личному инвайт-коду;

- Ввод чужого инвайт-кода.
POST http://127.0.0.1:8000/users/profile/user_id/ - на месте user_id нужно указать id авторизированного пользователя и
указать в JSON формате инвайт-код другого пользователя по ключу "referral_code" в теле запроса.

- Документация: redoc - http://127.0.0.1:8000/redoc/; swagger - http://127.0.0.1:8000/docs/.