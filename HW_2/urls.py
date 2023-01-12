# from datetime import datetime
from views import Index, Contact, Page, AnotherPage, Examples
from datetime import date

# front controller
def secret_front(request):
    # request['date'] = datetime.now().strftime('%H:%M - %d.%m.%Y года')
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/contact/': Contact(),
    '/page/': Page(),
    '/another_page/': AnotherPage(),
    '/examples/': Examples(),
}


