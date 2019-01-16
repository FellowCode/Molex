import requests, json
from Molex.settings import RE_CAPTCHA_SECRET

def GETStringToJSON(getString):
    json = {}
    values = getString.split('&')
    for value in values:
        key, param = value.split('=')
        json[key] = param
    return json

def checkReCaptcha(response):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': RE_CAPTCHA_SECRET,
        'response': response
    }
    r = requests.post(url, data)
    content = r.content
    rdata = json.loads(content)
    success = rdata['success']
    return success