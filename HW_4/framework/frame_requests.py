# get запросы.
class GetRequests:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            # делим параметры запроса через "&"
            params = data.split('&')
            for item in params:
                # делим ключ и значение через "="
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        # получаем параметры запроса.
        query_string = environ['QUERY_STRING']
        # трансформируем параметры в словарь.(dict)
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


# post запросы.
class PostRequests:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            # делим параметры запроса через "&"
            params = data.split('&')
            for item in params:
                # делим ключ и значение через "="
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        # получаем длину тела запроса.
        content_length_data = env.get('CONTENT_LENGTH')
        # приводим к int(type)
        content_length = int(content_length_data) if content_length_data else 0
        print(content_length)
        # считываем данные, если они есть,если нет-возвращаем 0.
        # env['wsgi.input'] -> <class '_io.BufferedReader'>
        # запускаем режим чтения.

        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b'' # если данных нет-возвращаем пустую байтовую строку.
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            # декодируем данные запроса,
            data_str = data.decode(encoding='utf-8')
            print(f'строка после декодирования - {data_str}')
            # собираем данные в словарь,
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        # получаем данные запроса,
        data = self.get_wsgi_input_data(environ)
        # трансформируем данные в словарь,
        data = self.parse_wsgi_input_data(data)
        return data







