START_HELP_TEXT = (f'<b>Сервис регистрации транспорта на таможенном пункте «Чернышевское»!</b>\n'
                   '🤖 <i>Список команд бота</i> 🤖\n'
                   '---------------------------------\n'
                   '/start - справочная информация\n'
                   '/upd - обновить данные\n'
                   '/form - управление заявками\n'
                   '/auto - статус тягача\n'
                   '---------------------------------\n'
                   'Желаем приятного использования!\n\n'
                   '<b>❗️ Техподдержка ❗️</b>\n'
                   '➡️ t.me/@srvgo_support ⬅️')

DATA_GET_ERROR = '✖️ Отказано в доступе ✖️'
CHECK_AUTO_PLATE = ('🚛 Отправьте номер тягача для проверки\n'
                    '<b>❗️ Используйте /upd для получения актуальной информации</b>')
PLACE_NOT_RESERVED = 'Место для машины не забронировано'

NO_PLACES = '✖️ Нет мест ✖️'

INPUT_LOG_PASS = ('Введите логин и пароль в формате\n'
                  '«login - password»')
INCORRECT_LOG_PASS = ('Пожалуйста, введите логин и пароль в формате\n'
                      '«login - password»')

SUCCESSFUL_AUTHORIZATION = '✔️Данные обновлены ✔️'
ERROR_AUTHORIZATION = ('✖️Неизвестная ошибка ✖️\n'
                       'Попробуйте ещё раз...')
ERROR_LOG_PASS = '✖️Неверный логин или пароль ✖️'
DENIED_ACCESS = '✖️Отказано в доступе ✖️'
NO_CAR_INFO = '❗️ Тягач не найден в базе ❗️'
SETTINGS_RESET = 'Настройки доступа сброшены'
WAIT_AUTHORIZATION = '⏳ Обновляем информацию... ⏳'
ALREADY_LOGIN = '✔️Вы уже авторизованы ✔️'

STATUSES = ['Активная', 'Исполнена', 'Отменена', 'Не исполнена', 'Перенесена заявителем']

SUCCESSFUL_FORM = ('\n✔️Заявка успешно создана! ✔️\n'
                     '🚛 Тягач: {}\n'
                     '📦 Прицеп: {}\n'
                     '⚙️ Тип перевозки: {}\n'
                     '⚙️ Вид перевозки: {}\n'
                     '🗓️ Дата: {}\n'
                     '🕰️ Время: {}\n'
                     'Время отправки заявки: {}\n')

ERROR_NO_TIME_FORM = ('\n✖️Нет доступного времени ✖️\n'
                      '🕰️Время попытки: {}')

ERROR_FORM = (f'✖️Ошибка создания заявки ✖️\n'
                f'🔄Повторите попытку 🔄')

FORM_TEXT = ('<b>Заявка №{}</b>\n'
             '🚛 Тягач: {}\n'
             '📦 Прицеп: {}\n'
             '⚙️ Тип перевозки: {}\n'
             '⚙️ Вид перевозки: {}\n'
             '❗️ Особый груз: {}\n'
             '🗓️ Дата: {}\n\n')

HELP_TEXT = ('<b>❗️ Правила создания заявки ❗️</b>\n'
             'Сообщение о добавлении заявки <b>должно начинаться с /plus</b>\n'
             'Каждый следующий параметр заявки пишется с новой строки:\n'
             '💻 /plus\n'
             '🚛 Номер тягача\n'
             '📦 Номер прицепа\n'
             '⚙️ Тип перевозки\n'
             '⚙️ Вид перевозки\n'
             '❗️ Тип особого груза\n'
             '🗓️ Дата\n\n'
             'Ниже приведён пример <b>правильно</b> оформленной заявки. \n'
             '------------------------------\n'
             '<code>/plus\n'
             'C078TC39\n'
             'AB955739 / *пустая строка*\n'
             'Экспорт / Транзит\n'
             'Перевозка грузов / Порожний\n'
             'Скоропортящийся груз / Живой скот / Опасный груз / Другой особый груз / *пустая строка*\n'
             '01.01.2025</code>\n'
             '------------------------------\n'
             '<b>❗️ Обратите внимание</b> ❗️\n'
             '<b>Параметр «Тип особого груза» заполнятся, только если выбрана «Перевозка грузов»!</b>\n\n')

HELP_TEXT_EDIT = ('==========================\n'
                  '<b>❗️ Правила изменения даты ❗️</b>\n'
                  'Сообщение об изменении даты\n'
                  '<b>должно начинаться с /date</b>\n'
                  '- Номер заявки\n'
                  '- Новая дата (дд.мм.гггг)\n\n'
                  '<b>Пример изменения даты</b>.\n'
                  '--------------\n'
                  '<code>/date\n'
                  '2\n'
                  '01.01.2025</code>\n'
                  '--------------\n')
