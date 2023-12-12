# Test_CRUD_Web_APP
This is CRUD app for interview.
- [Импорт проекта](#Импорт)
## Импорт проекта из GitHub и развертывание с помощью docker-compose

### Шаг 1: Клонирование проекта с GitHub

git clone https://github.com/VRameew/Test_CRUD_Web_APP.git

### Шаг 2: Подготовка файлов окружения

1. Перейдите в папку проекта.
2. Создайте файл .env и откройте его в текстовом редакторе.
3. Укажите следующие переменные окружения в файле .env и установите их значения для вашей системы:

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=db
DB_PORT=5432

*Примечание:* Проверьте, что значения переменных DB_NAME, DB_USER и DB_PASSWORD соответствуют вашим настройкам PostgreSQL.

### Шаг 3: Развертывание с помощью docker-compose

1. Убедитесь, что Docker и docker-compose установлены на вашем компьютере.
2. В командной строке или терминале перейдите в папку проекта, где находится файл docker-compose.yml.
3. Выполните следующую команду для запуска проекта:

docker-compose up -d

После успешного выполнения команды проект будет доступен по адресу [http://localhost:8000/](http://localhost:8000/).

---

Теперь вы успешно импортировали проект с GitHub и развернули его с использованием docker-compose. Вы готовы использовать проект для разработки или тестирования на вашем локальном компьютере.


## Описание принципа работы

## Описание маршрутов

### CRUD\urls.py
Данный код представляет собой основной файл настройки маршрутов веб-приложения на основе фреймворка Django. Файл urls.py содержит список URL-адресов и соответствующих им обработчиков запросов.

1. from django.contrib import admin - импорт модуля admin из пакета django.contrib, который позволяет использовать административный интерфейс Django.

2. from django.urls import path, include - импорт функций path и include из пакета django.urls. Функция path используется для определения URL-шаблонов, а include для включения URL-шаблонов из других приложений.

3. from users.views import home - импорт функции home из модуля views пакета users. home - это обработчик запроса для домашней страницы.

4. urlpatterns - переменная, которая содержит список URL-шаблонов и соответствующих им обработчиков запросов.

   - path('admin/', admin.site.urls) - URL для доступа к административному интерфейсу Django.

   - path('', home, name='home') - URL для домашней страницы приложения, где home является обработчиком запроса, а name='home' - имя URL-шаблона.

   - path('users/', include('users.urls')) - URL для включения URL-шаблонов из приложения users. Все URL-адреса, начинающиеся с users/, будут переданы в обработчик запроса из приложения users.

   - path('tasks/', include('tasks.urls')) - URL для включения URL-шаблонов из приложения tasks. Все URL-адреса, начинающиеся с tasks/, будут переданы в обработчик запроса из приложения tasks.

## users\urls

В данном коде определены следующие маршруты для обработки запросов:

- registration - URL для регистрации нового пользователя. Связан с функцией register и назван registration.
- login - URL для входа пользователя в систему. Связан с функцией user_login и назван login.
- user_data_update - URL для обновления данных пользователя. Связан с функцией user_update и назван user_data_update.
- change_password - URL для изменения пароля пользователя. Связан с функцией change_password и назван change_password.
- logout - URL для выхода пользователя из системы. Связан с функцией logout_view и назван logout.
- success - URL для отображения страницы успешного действия. Связан с функцией success и назван success.


## taks\urls

В данном коде заданы следующие маршруты для обработки запросов:

- tasks_list - URL для просмотра списка задач. Связан с функцией tasks_list и назван tasks_list.
- create_task - URL для создания новой задачи. Связан с функцией create_task и назван create_task.
- edit_task/<int:task_id>/ - URL для редактирования задачи с определенным идентификатором задачи (task_id). Связан с функцией edit_task и назван edit_task.
- task_data/<int:task_id> - URL для просмотра данных задачи с определенным идентификатором задачи (task_id). Связан с функцией task_data и назван task_data.
- delete_task/<int:task_id>}/ - URL для удаления задачи с определенным идентификатором задачи (task_id). Связан с функцией delete_task и назван delete_task.
- create_comment/<int:task_id>/ - URL для создания нового комментария к задаче с определенным идентификатором задачи (task_id). Связан с функцией create_comment и назван create_comment.
- edit_comment/<int:comment_id> - URL для редактирования комментария с определенным идентификатором комментария (comment_id). Связан с функцией edit_comment и назван edit_comment.
- delete_comment/<int:comment_id> - URL для удаления комментария с определенным идентификатором комментария (comment_id). Связан с функцией delete_comment и назван delete_comment.

## Описание моделей

В данном коде определены следующие модели для работы с базой данных:

### Модель Task

- text - текстовое поле с максимальной длиной 300 символов, представляющее название задачи.
- author - внешний ключ на модель пользователя get_user_model(), связанный с полем tasks_author, который представляет автора задачи.
- date_created - поле типа DateTimeField, автоматически заполняющееся текущей датой и временем при создании задачи.

### Модель TaskStatus

- task - внешний ключ на модель Task, связанный с полем task_status_index_name_idx, который представляет задачу, соответствующую статусу.
- status - текстовое поле с максимальной длиной 15 символов, представляющее статус задачи. Допустимые значения указаны в кортеже tasks_status. Значение по умолчанию - "Не приступали".

### Модель Comments

- task - внешний ключ на модель Task, связанный с полем task_comments_index_name_idx, который представляет задачу, к которой относится комментарий.
- text - текстовое поле, представляющее содержание комментария.
- date_created - поле типа DateTimeField, автоматически заполняющееся текущей датой и временем при создании комментария.

У каждой модели определено свойство str, которое возвращает текстовое представление модели. Также для каждой модели указаны индексы для оптимизации поиска по полям text, author, status и связанным с ними полям.

### Модель UserManager

- create_user(email, password=None) - метод для создания пользователя. Принимает email и пароль (по умолчанию None), проверяет, что email не пустой и создает пользователя с заданным email. Пароль установлен с помощью функции set_password. После создания пользователя, он сохраняется в базе данных и возвращается.
- create_superuser(email, password, user_name) - метод для создания суперпользователя. При создании суперпользователя вызывается метод create_user для создания пользователя с заданным email и паролем. Затем устанавливаются дополнительные атрибуты is_superuser=True и is_staff=True. После этого суперпользователь сохраняется в базе данных и возвращается.

### Модель UserModel

- email - поле типа EmailField с максимальной длиной 255 символов, представляющее адрес электронной почты пользователя. Уникальное поле с индексом для оптимизации поиска.
- user_name - поле типа CharField с максимальной длиной 25 символов, представляющее имя пользователя. Уникальное поле с индексом для оптимизации поиска.
- first_name - поле типа CharField с максимальной длиной 30 символов, представляющее имя пользователя.
- last_name - поле типа CharField с максимальной длиной 30 символов, представляющее фамилию пользователя.
- date_joined - поле типа DateTimeField, автоматически заполняющееся текущей датой и временем при регистрации пользователя.
- is_active - поле типа BooleanField, указывающее на активность пользователя. По умолчанию установлено значение True.

У модели UserModel указано свойство objects, которое представляет объект менеджера пользователя UserManager.

Также определен метод get_full_name(), который возвращает полное имя пользователя, состоящее из полей first_name и last_name.

Для модели UserModel указаны индексы для оптимизации поиска по полям email, user_name, first_name и last_name.

## Описание форм

## Описание users\forms
В данном коде определены следующие формы для работы с данными пользователей:

### Форма UserRegistrationForm

- Поля:
    - email - поле типа EmailField, представляющее адрес электронной почты пользователя.
    - user_name - поле типа CharField, представляющее имя пользователя.
    - password - поле типа CharField, представляющее пароль пользователя.
    - first_name - поле типа CharField, представляющее имя пользователя.
    - last_name - поле типа CharField, представляющее фамилию пользователя.
- Методы:
    - clean() - метод для проверки корректности данных формы. Проверяет, что пароль не пустой.
    - save(commit=True) - метод для сохранения данных пользователя. Возвращает сохраненного пользователя.

### Форма LoginForm

- Поля:
    - email - поле типа EmailField, представляющее адрес электронной почты пользователя.
    - password - поле типа CharField, представляющее пароль пользователя.
- Методы:
    - clean() - метод для проверки корректности данных формы. Проверяет, что введенный email и пароль соответствуют существующему пользователю.

### Форма UserUpdateForm

- Поля:
    - email - поле типа EmailField, представляющее актуальный адрес электронной почты пользователя.
    - user_name - поле типа CharField, представляющее актуальное имя пользователя.
    - first_name - поле типа CharField, представляющее актуальное имя пользователя.
    - last_name - поле типа CharField, представляющее актуальную фамилию пользователя.

### Форма NewPasswordChangeForm

- Наследуется от формы SetPasswordForm.
- Поля:
    - new_password1 - поле типа CharField, представляющее новый пароль пользователя.
    - new_password2 - поле типа CharField, представляющее подтверждение нового пароля пользователя.
- Методы:
    - clean_new_password1() - метод для проверки нового пароля на наличие заглавной буквы и цифры.
    - clean() - метод для проверки корректности данных формы. Проверяет, что новые пароли совпадают.

## Описание tasks\forms

В данном коде определены следующие формы для работы с данными задач и комментариев:

### Форма TaskForm

- Поля:
    - text - поле типа CharField, представляющее название задачи.
- Мета:
    - model - модель Task, с которой форма связана.
    - fields - список полей, отображаемых в форме (text).
    - labels - словарь, в котором заданы названия полей формы.

### Форма TaskEditForm

- Поля:
    - text - поле типа CharField, представляющее название задачи.
    - status - поле типа ChoiceField, представляющее статус задачи (выбор из списка TaskStatus.tasks_status).
- Мета:
    - model - модель Task, с которой форма связана.
    - fields - список полей, отображаемых в форме (text, status).
    - labels - словарь, в котором заданы названия полей формы.

### Форма TaskDeleteForm

- Мета:
    - model - модель Task, с которой форма связана.
    - fields - пустой список полей.

### Форма CommentsForm

- Методы:
    - init(*args, **kwargs) - метод инициализации формы. Блокирует поле task_comments_index_name_idx для редактирования.
- Мета:
    - model - модель Comments, с которой форма связана.
    - fields - список полей, отображаемых в форме (task_comments_index_name_idx, text).
    - labels - словарь, в котором заданы названия полей формы.

### Форма CommentsEditForm

- Мета:
    - model - модель Comments, с которой форма связана.
    - fields - список полей, отображаемых в форме (task_comments_index_name_idx, text).
    - labels - словарь, в котором заданы названия полей формы.

### Форма CommentsDeleteForm

- Мета:
    - model - модель Comments, с которой форма связана.
    - fields - пустой список полей.

## Описание представлений
В данном коде определены следующие представления (views) для обработки запросов:

## users\views

### Представление home

- Функция home отображает главную страницу приложения.
- Использует класс HabrReader для чтения новостей с сайта Habr.
- Возвращает отрендеренный шаблон home.html со списком новостей.

### Представление register

- Функция register обрабатывает запросы для регистрации нового пользователя.
- Если запрос методом POST, создается экземпляр формы UserRegistrationForm и проверяется на валидность. Если форма валидна, происходит сохранение пользователя и перенаправление на страницу success.
- Если запрос не методом POST, отображается пустая форма UserRegistrationForm.

### Представление user_login

- Функция user_login обрабатывает запросы для входа пользователя.
- Если запрос методом POST, создается экземпляр формы LoginForm и проверяется на валидность. Если форма валидна, происходит аутентификация пользователя с помощью функции authenticate и функции login, после чего происходит перенаправление на страницу success.
- Если запрос не методом POST, отображается пустая форма LoginForm.

### Представление user_update

- Функция user_update обрабатывает запросы для обновления данных пользователя.
- Если запрос методом POST, создается экземпляр формы UserUpdateForm с текущим пользователем в качестве экземпляра, и проверяется на валидность. Если форма валидна, происходит сохранение данных пользователя и перенаправление на страницу success.
- Если запрос не методом POST, отображается форма UserUpdateForm с предварительно заполненными данными текущего пользователя.

### Представление change_password

- Функция change_password обрабатывает запросы для изменения пароля пользователя.
- Если запрос методом POST, создается экземпляр формы NewPasswordChangeForm с текущим пользователем в качестве аргумента request.user, и проверяется на валидность. Если форма валидна, происходит изменение пароля пользователя и перенаправление на страницу success.
- Если запрос не методом POST, отображается форма NewPasswordChangeForm с предварительно заполненными данными текущего пользователя.

### Представление logout_view

- Функция logout_view обрабатывает запросы для выхода пользователя из системы.
- Вызывается функция logout для выхода пользователя.
- После выхода происходит перенаправление на главную страницу home.

### Представление success

- Функция success представляет страницу успешного действия.
- Возвращает отрендеренный шаблон success.html.

Все представления используют различные формы и модели из файлов forms.py и models.py.
## tasks\views

### Представление create_task

- Функция create_task обрабатывает запросы для создания новой задачи.
- Если запрос методом POST, создается экземпляр формы TaskForm и проверяется на валидность. Если форма валидна, создается новая задача, привязанная к текущему пользователю, и сохраняется в базе данных. Затем создается или обновляется объект TaskStatus для задачи.
- Если запрос не методом POST, отображается пустая форма TaskForm.

### Представление edit_task

- Функция edit_task обрабатывает запросы для редактирования задачи.
- Получает объект задачи по заданному идентификатору task_id. Если текущий пользователь не является автором задачи, происходит перенаправление на страницу tasks_list.
- Если запрос методом POST, создается экземпляр формы TaskEditForm с данными из запроса и соответствующим объектом задачи. Если форма валидна, сохраняются изменения по задаче и статусу, обновляется форма с новыми значениями и происходит перенаправление на страницу task_data.
- Если запрос не методом POST, отображается форма TaskEditForm с предзаполненными данными и актуальным статусом задачи.

### Представление delete_task

- Функция delete_task обрабатывает запросы для удаления задачи.
- Получает объект задачи по заданному идентификатору task_id. Если текущий пользователь не является автором задачи, происходит перенаправление на страницу tasks_list.
- Если запрос методом POST, создается экземпляр формы TaskDeleteForm с данными из запроса и соответствующим объектом задачи. Если форма валидна, задача удаляется и происходит перенаправление на страницу tasks_list.
- Если запрос не методом POST, отображается форма TaskDeleteForm с данными задачи.

### Представление create_comment

- Функция create_comment обрабатывает запросы для создания нового комментария к задаче.
- Получает объект задачи по заданному идентификатору task_id.
- Если запрос методом POST, создается экземпляр формы CommentsForm с данными из запроса. Если форма валидна, создается новый комментарий, привязанный к текущему пользователю и задаче, и сохраняется в базе данных.
- Если запрос не методом POST, отображается форма CommentsForm с предзаполненными данными по задаче.

### Представление edit_comment

- Функция edit_comment обрабатывает запросы для редактирования комментария.
- Получает объект комментария по заданному идентификатору comment_id.
- Если запрос методом POST, создается экземпляр формы CommentsEditForm с данными из запроса и соответствующим объектом комментария. Если форма валидна, сохраняются изменения и происходит перенаправление на страницу task_data.
- Если запрос не методом POST, отображается форма CommentsEditForm с предзаполненными данными комментария.

### Представление delete_comment

- Функция delete_comment обрабатывает запросы для удаления комментария.
- Получает объект комментария по заданному идентификатору comment_id.
- Если запрос методом POST, создается экземпляр формы CommentsDeleteForm с данными из запроса и соответствующим объектом комментария. Если форма валидна, комментарий удаляется и происходит перенаправление на страницу task_data.
- Если запрос не методом POST, отображается форма CommentsDeleteForm с данными комментария.

Все представления используют модели и формы из файлов models.py и forms.py.

### Представление delete_comment

- Функция delete_comment обрабатывает запросы для удаления комментария.
- Получает объект комментария по заданному идентификатору comment_id.
- Если запрос методом POST, создается экземпляр формы CommentsDeleteForm с данными из запроса и соответствующим объектом комментария. Если форма валидна, комментарий удаляется и происходит перенаправление на страницу tasks_list.
- Если запрос не методом POST, отображается форма CommentsDeleteForm с данными комментария.

### Представление tasks_list

- Функция tasks_list отображает список задач, соответствующих текущему пользователю.
- Получает все задачи, отфильтрованные по полю author (текущий пользователь), и передает их в шаблон tasks_list.html.

### Представление task_data

- Функция task_data отображает данные задачи, комментарии и статус задачи.
- Получает задачу по заданному идентификатору task_id. Затем получает статус задачи и комментарии, связанные с этой задачей.
- Возвращает отрендеренный шаблон task_data.html с передачей объектов задачи, статуса и комментариев в шаблон.

Все представления используют модели и формы из файлов models.py и forms.py. Они также используют декоратор login_required для проверки аутентификации пользователя.

## Описание тестов

В данном коде определены следующие тесты для проверки моделей и форм:

## users\tests

### Тест класса UserModelTest

- test_create_user - тест на создание пользователя. Проверяет, что созданный пользователь имеет правильные значения атрибутов.
- test_create_superuser - тест на создание суперпользователя. Проверяет, что созданный суперпользователь имеет правильные значения атрибутов, включая флаги is_superuser и is_staff.
- test_get_full_name - тест метода get_full_name(). Проверяет, что метод возвращает полное имя пользователя, состоящее из полей first_name и last_name.
- test_user_model_fields - тест полей модели UserModel. Проверяет, что поля имеют правильные названия, уникальность и индексы, а также проверяет наличие определенных флагов, таких как auto_now_add и значение по умолчанию.

### Тест класса UserRegistrationFormTest

- test_valid_form - тест на валидную форму регистрации пользователя. Проверяет, что форма с правильными данными является валидной.
- test_invalid_form_existing_email - тест на невалидную форму с существующим email. Создает пользователя с таким же email и проверяет, что форма с этим email является невалидной и содержит ошибку.
- test_invalid_form_existing_user_name - тест на невалидную форму с существующим user_name. Создает пользователя с таким же user_name и проверяет, что форма с этим user_name является невалидной и содержит ошибку.
- test_invalid_form_missing_fields - тест на невалидную форму с отсутствующими полями. Проверяет, что форма с отсутствующими полями является невалидной и содержит ошибки для полей user_name и password.

Все тесты осуществляют проверку правильности значений атрибутов, индексов и флагов моделей, а также проверку валидности форм с правильными, неправильными или недостающими данными.

## tasks\tests

### Тест класса TaskModelTest

- test_task_text - проверяет, что текст задачи соответствует ожидаемому значению
- test_task_author - проверяет, что автор задачи соответствует ожидаемому значению

### Тест класса TaskStatusModelTest

- test_task_status_task - проверяет, что задача для статуса задачи соответствует ожидаемому значению
- test_task_status_status - проверяет, что статус задачи соответствует ожидаемому значению

### Тест класса CommentsModelTest

- test_comment_task - проверяет, что задача для комментария соответствует ожидаемому значению
- test_comment_text - проверяет, что текст комментария соответствует ожидаемому значению

### Тест класса TaskFormTest

- test_task_form_fields - проверяет, что поля формы для создания задачи соответствуют ожидаемым значениям

### Тест класса TaskEditFormTest

- test_task_edit_form_fields - проверяет, что поля формы для редактирования задачи соответствуют ожидаемым значениям

### Тест класса TaskDeleteFormTest

- test_task_delete_form_fields - проверяет, что поля формы для удаления задачи соответствуют ожидаемым значениям


## Описание метода получения данных из RSS HABR

Данный метод осуществляет получение данных из RSS ленты HABR. Он использует библиотеки asyncio, aiohttp и feedparser для асинхронного выполнения запросов и разбора полученных данных.

### Метод fetch_rss

Метод fetch_rss выполняет асинхронный GET-запрос к URL RSS ленты HABR и возвращает текст ответа в формате XML. Он использует aiohttp.ClientSession для отправки запроса и получения ответа.

### Метод parse_feed

Метод parse_feed принимает объект feed, который представляет одну запись из RSS ленты HABR, и проводит разбор этой записи. Он извлекает информацию о заголовке, ссылке, описании, дате публикации и категориях записи. Результат разбора записи возвращается в виде словаря.

### Метод main

Метод main является основным методом класса HabrReader. Он использует aiohttp.ClientSession для создания сессии, отправки запроса RSS ленты и получения текста ответа в формате XML. Затем метод feedparser.parse разбирает полученный XML и возвращает объекты feedparser.FeedParserDict, представляющие разобранные записи из ленты.

Для асинхронной обработки каждой записи используется asyncio.gather вместе с методом parse_feed. Результаты разбора записей собираются в список parsed_feeds, который в итоге возвращается.

### Использование метода

Для использования метода необходимо создать экземпляр класса HabrReader и вызвать метод main с использованием asyncio.run:

reader = HabrReader()
parsed_feeds = asyncio.run(reader.main())

В результате будет получен список, содержащий разобранные записи из RSS ленты HABR, представленные в виде словарей с информацией о заголовке, ссылке, описании, дате публикации и категориях записи.

