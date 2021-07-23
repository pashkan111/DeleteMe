from ..config import PASSWORD, HOST, EMAIL_FROM, EMAILS_TO
from asgiref.sync import sync_to_async



def make_html(name=None, surname=None, patronymic=None, phone=None, telegram=None, city=None, date_of_birth=None, words=None):
    html = f'<html><body><h2>Оповещение из системы заказов @deletememonitoring мониторинг</h2>\
            <p>Имя: {name}</p>\
            <p>Фамилия: {surname}</p>\
            <p>Отчество: {patronymic}</p>\
            <p>Телефон: {phone}</p>\
            <p>Телеграм: {telegram}</p>\
            <p>Город: {city}</p>\
            <p>Дата рождения: {date_of_birth}</p>\
            <p>Ключевые слова для поиска: {words}</p></body></html>'
    return html


@sync_to_async
def post_data_to_email(data, keywords, HOST=HOST, FROM=EMAIL_FROM, TO=EMAILS_TO, PASSWORD=PASSWORD):
    try:
        words = keywords
        # words = list(map(lambda a: a.strip(), keywords.split(',')))
        name = data['name']
        surname = data['surname']
        patronymic = data['patronymic']
        phone = data['phone']
        telegram = data['telegram_id']
        city = data['city']
        date_of_birth = data['date_of_birth']
    except KeyError as ke:
        return ke
    SUBJECT = make_html(name, surname, patronymic, phone, telegram, city, date_of_birth, words)
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Заказ"
    msg['From'] = FROM
    for mail in TO:
        msg['To'] = mail
        body = MIMEText(SUBJECT, 'html')
        msg.attach(body)
        try:
            server = smtplib.SMTP_SSL(HOST)
            server.login(FROM, PASSWORD)
            server.sendmail(FROM, mail, msg.as_string())
            server.quit()
        except Exception:
            return 400
    return True

