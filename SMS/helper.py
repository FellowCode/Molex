import requests
from Molex.settings import *

class SMS:
    admin_phones = ['79241544424']
    url = 'http://api.1000sms.ru/'

    method = 'push_msg'
    email = SMS_LOGIN
    password = SMS_PASSWORD
    text = ''
    phones = None
    phone = None
    sender_name = SMS_SENDER_NAME
    to_admins = False
    error = False

    def get_full_dict(self):
        dict = {
            'method': self.method,
            'email': self.email,
            'password': self.password,
            'text': self.text,
            'phone': self.phone,
            'sender_name': self.sender_name,
        }
        return dict

    def __init__(self, text, phones=None, to_admins=False):
        self.text = text
        self.to_admins = to_admins
        if type(phones) is list:
            self.phones = phones
        elif type(phones) is str:
            self.phone = phones
        elif not to_admins:
            self.error = True

    def send(self):
        if not self.error:
            r = None
            if self.phones is not None:
                for phone in self.phones:
                    self.phone = phone
                    params = self.get_full_dict()
                    r = requests.get(self.url, params=params)
            elif self.phone is not None:
                params = self.get_full_dict()
                r = requests.get(self.url, params=params)
            if self.to_admins:
                for phone in self.admin_phones:
                    self.phone = phone
                    params = self.get_full_dict()
                    r = requests.get(self.url, params=params)
            print(str(r.content))
        else:
            print('error')