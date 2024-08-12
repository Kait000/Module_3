def send_email(message, recipient, *, sender='university.help@gmail.com'):
    list_domen = ('.ru', '.com', 'net')
    if not ('@' in recipient and '@' in sender and
            recipient.lower().endswith(list_domen) and
            sender.lower().endswith(list_domen)):
        return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    if recipient == sender:
        return 'Нельзя отправить письмо самому себе!'
    if sender == 'university.help@gmail.com':
        return f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'
    return f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}'


print(send_email('Сообщение 1', 'xsel@Rambler.Ru'))
print(send_email('Сообщение 2', 'xsel@Rambler.Ru', sender='urban@mail.ru'))
print(send_email('Сообщение 3', 'xsel@Rambler.uk', sender='urban@mail.ru'))
print(send_email('Сообщение 4', 'xsel@Rambler.Ru', sender='xsel@Rambler.Ru'))
