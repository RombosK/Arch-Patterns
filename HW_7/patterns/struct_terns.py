from time import time


# структурный паттерн - "Decorator"
class AppRoute:
    def __init__(self, routes, url):
        """
        Сохраняем значение переданного параметра
        """
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        """
        Декоратор
        """
        self.routes[self.url] = cls()


# структурный паттерн "Decorator"
class Debug:

    def __init__(self, name):

        self.name = name

    def __call__(self, cls):
        """
        Декоратор
        """

        # Вспомогательная функция, декорирующая каждый отдельный метод класса
        def timeit(method):
            """
            Метод для того, чтобы декоратор класса wrapper обернул в timeit
            каждый метод декорируемого класса
            """
            def timed(*args, **kw):
                start = time()
                result = method(*args, **kw)
                finish = time()
                delta = finish - start

                print(f'debug --> {self.name} выполнялся {delta:2.2f} ms')
                return result

            return timed

        return timeit(cls)


