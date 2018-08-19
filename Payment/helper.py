from . import settings as PaySettings
import hashlib
import json
from .settings import Yandex
from urllib import parse

def getRobokassaPaymentUrl(order):
    value = '{0}:{1}.00:{2}:{3}'.format(PaySettings.login, order.payment_amount, order.id, PaySettings.password1)
    signatureValue = hashlib.md5()
    signatureValue.update(str.encode(value))
    src = 'https://auth.robokassa.ru/Merchant/PaymentForm/FormMS.js?MerchantLogin={0}&OutSum={1}.00&InvoiceID={2}&Description={3}&SignatureValue={4}&IsTest={5}'.format(
        PaySettings.login, order.payment_amount, order.id, PaySettings.inv_desc, signatureValue.hexdigest(),
        PaySettings.isTest)
    return src

def getYandexPaymentUrl(order):
    url = 'https://money.yandex.ru/quickpay/confirm.xml'
    params = {
        'receiver': Yandex.receiver,
        'quickpay-form': Yandex.quickpayform,
        'successURL': Yandex.successURL,
        'formcomment': Yandex.formcomment,
        'shortdest': Yandex.shortdest,
        'targets': Yandex.targets,
        'paymentType': Yandex.paymentType,
        'sum': order.payment_amount,
        'label': order.id
    }
    url += '?' + parse.urlencode(params)
    return url