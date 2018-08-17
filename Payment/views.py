from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from . import settings as PaySettings
from Products.models import Order
from .helper import Yandex

################################
#######ROBOKASSA

@csrf_exempt
def RobokassaResult(request):
    if request.method == 'GET':
        sum = request.GET['OutSum']
        inc_sum = request.GET['IncSum']
        id = request.GET['InvId']
        email = request.GET['EMail']
        signatureValue = request.GET['SignatureValue']
        value = '{0}:{1}:{2}'.format(sum, id, PaySettings.password2)
        signatureValueGen = hashlib.md5()
        signatureValueGen.update(str.encode(value))
        if str(signatureValueGen.hexdigest()).upper() == signatureValue:
            order = Order.objects.get(id=id)
            if float(sum) == order.payment_amount:
                order.isPaid = True
            order.person_pay = float(inc_sum)
            order.person_pay_email = email
            order.save()
        return render(request, 'payment.html', {'id': id})

@csrf_exempt
def RobokassaSuccess(request):
    if request.method == 'POST':
        return render(request, 'Payment/Success.html', {'post': str(request.POST)})

@csrf_exempt
def RobokassaFail(request):
    if request.method == 'POST':
        return render(request, 'Payment/Fail.html', {'post': str(request.POST)})


##########################################
########  YANDEX

@csrf_exempt
def YandexResult(request):
    if request.method == 'POST':
        sha1 = request.POST['sha1_hash']
        operation_id = request.POST['operation_id']
        amount = request.POST['amount']
        withdraw_amount = request.POST['withdraw_amount']
        id = request.POST['label']

        notification_type = request.POST['notification_type']
        currency = request.POST['currency']
        datetime = request.POST['datetime']
        sender = request.POST['sender']
        codepro = request.POST['codepro']

        value = notification_type+'&'+operation_id+'&'+amount+'&'+currency+'&'+datetime+'&'+sender+'&'+codepro+'&'+Yandex.secret+'&'+id

        signature = hashlib.sha1()
        signature.update(str.encode(value))

        if signature.hexdigest() == sha1:
            order = Order.objects.get(id=id)
            order.payment_method = 'Yandex'
            order.person_pay = float(withdraw_amount)
            if float(amount) == order.payment_amount:
                order.isPaid = True
            order.person_payment_account = sender
            order.payment_datetime = datetime
            order.payment_operation_id = operation_id
            order.save()
        return HttpResponse('')

def YandexSuccess(request):
    return render(request, 'Products\OrderConfirm.html')


