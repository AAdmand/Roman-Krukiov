def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not sender.endswith((".com", ".ru", ".net")) or not sender.endswith((".com", ".ru", ".net")):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif sender == recipient:
        print("Нельзя отправть письмо самому себе!")
    elif sender != recipient:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
