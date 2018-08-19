from .helper import SMS

def sendConfirmOrderSMS(order_id):
    text = 'MOLEX: Поступил заказ #' + str(order_id)
    sms = SMS(text, to_admins=True)
    sms.send()


