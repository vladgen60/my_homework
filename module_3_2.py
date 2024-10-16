
def send_email(message, recipient,*, sender = 'university.help@gmail.com'): # Создаем функцию.
        if ('@' or '.com' or '.ru' or '.net') not in (recipient or sender):     # Определяем условия при которых письма отправить нельзя.
                print('Невозможно отправить письмо с адреса {} на адрес {}.'.format(sender, recipient)) # Выводим на экран сообщение при котором нельзя
                                                                                                        # отправлять сообщения.
        elif sender != 'university.help@gmail.com':     # Определяем условия при котором письмо отправлено не с нужного адреса.
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {} на адрес {}.'.format(sender, recipient)) # Выводим на экран информацию 
                                                                                        # с предупреждением откуда и куда было отправлено письмо.
        elif sender == recipient:       # Определяем условие при котором  
                print('Нельзя отправить письмо самому себе!')   # выводится сообщение, что нельзя отправлять письма самому себе.
        else:
            if sender == 'university.help@gmail.com':   # Определяем условие, при котором письмо отправляется.
                print('Это сообщение для проверки связи', 'vasyok1337@gmail.com') # Выводим сообщение, что письмо отправлено.

         # Примеры для проверки всех условий.

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Напоминаю самому себе о вебинаре', 'university.help@gmail.com', sender='university.help@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.teachermail.ru', sender='urban.teacher@mail.ru')