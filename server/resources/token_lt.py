from resources.database.database import LTDatabase
import hashlib
import base64
import time
import base64
import time

valid_time = 7 * 24 * 3600


def check_token(token):
    text = base64.b64decode(token.encode()).decode()
    tt = text.split()
    _username = tt[0]
    _duty = tt[1]
    time_token = int(tt[2])
    time_now = round(time.time())
    time_delta = time_now - time_token
    if time_delta <= valid_time:
        return _username, _duty
    else:
        return 0



def accio_token(id, duty):
    text = id + ' ' + duty + ' ' + str(round(time.time()))
    token = base64.b64encode(text.encode())
    return token.decode()


def hash(text):
    return hashlib.md5(text.encode()).hexdigest()

if __name__ == '__main__':
    print(check_token('bGpqangxOTk3IDE0ODY0OTI2ODY='))