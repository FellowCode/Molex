from .helper import SMS
from Molex.celery import app


@app.task
def sendConfirmOrderSMS(order_id):
    text = 'MOLEX: Поступил заказ #' + str(order_id)
    sms = SMS(text, to_admins=True)
    sms.send()