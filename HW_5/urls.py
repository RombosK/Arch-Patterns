# from datetime import datetime

from datetime import date

# front controller
def secret_front(request):
    # request['date'] = datetime.now().strftime('%H:%M - %d.%m.%Y года')
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]



