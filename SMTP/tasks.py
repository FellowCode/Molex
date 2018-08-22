from django.core.mail import EmailMultiAlternatives
from Molex.celery import app

admin_email = ['sergo79_f1@mail.ru', 'pipiecvk@mail.ru']

@app.task
def sendConfirmOrderMail(userEmail, order_id):
    subject, from_email = 'Заказ принят', 'info@molex79.ru'
    text_content = 'Ваш заказ #' + str(order_id) + ' принят.\n'
    text_content += 'Мы свяжемся с вами для уточнения заказа, а также как только заказанная вами продукция придет. Обычно срок доставки не превышает 30 дней.\n'
    text_content += 'Если вы получили письмо по ошибке, вы можете его проигнорировать.\n'
    text_content += 'Задать вопрос можно на почту: support@molex79.ru\n'
    text_content += 'Телефон для справок: 89841284264'

    html_content = '<p>Ваш заказ #' + str(order_id) + ' принят.</p>'
    html_content += '<p>Мы свяжемся с вами для уточнения заказа, а также как только заказанная вами продукция придет. Обычно срок доставки не превышает 30 дней.</p>'
    html_content += '<p>Если вы получили письмо по ошибке, вы можете его проигнорировать.</p>'
    html_content += '<p>Задать вопрос можно на почту: <b>support@molex79.ru</b></p>'
    html_content += '<p>Телефон для справок: <b>89841284264</b></p>'

    msg = EmailMultiAlternatives(subject, text_content, from_email, [userEmail])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=True)

    subject, from_email = 'Поступил заказ', 'info@molex79.ru'
    text_content = 'Поступил заказ ' + str(order_id) + '\n'
    text_content += 'Подробные данные заказа: http://molex79.ru/admin/Products/order/' + str(order_id) + '/change/\n'
    text_content += 'Список заказов: http://molex79.ru/products/orders/\n'

    html_content = '<p>Поступил заказ <b>' + str(order_id) + '</b></p>'
    html_content += '<p>Подробные данные заказа: http://molex79.ru/admin/Products/order/' + str(order_id) + '/change/</p>'
    html_content += '<p>Список заказов: http://molex79.ru/products/orders/</p>'

    msg = EmailMultiAlternatives(subject, text_content, from_email, admin_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=True)

@app.task
def sendSupportMsg(userEmail, text):
    subject, from_email = 'Заявка в техподдержку', 'info@molex79.ru'

    text_content = 'Поступила заявка.\n'
    text_content += 'Email: ' + userEmail + '\n'
    text_content += 'Текст заявки:\n'
    text_content += text

    html_content = '<p>Поступила заявка.</p>'
    html_content += '<p><b>Email:</b> ' + userEmail + '</p>'
    html_content += '<p><b>Текст заявки:</b></p>'
    html_content += '<p>' + text + '</p>'

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['support@molex79.ru'])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=True)