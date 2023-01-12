from framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', contact='+7999XXX5555')


class Page:
    def __call__(self, request):
        return '200 OK', render('page.html', date=request.get('date', None))


class AnotherPage:
    def __call__(self, request):
        return '200 OK', render('another_page.html', another_page='Description')


class Examples:
    def __call__(self, request):
        return '200 OK', render('examples.html', examples='Description')
