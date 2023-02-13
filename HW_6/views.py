from framework.templator import render
from datetime import date
from patterns.gen_patterns import Engine, Logger
from patterns.struct_terns import AppRoute, Debug
from patterns.behave_patterns import EmailNotifier, SmsNotifier, CreateView, \
    BaseSerializer, ListView


site = Engine()
logger = Logger('main')

routes = {}

email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()

# Контроллеры:
# Главная
@AppRoute(routes=routes, url='/')
class Index:
    @Debug(name='index')
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None), objects_list=site.categories)


# Расписание курсов
@AppRoute(routes=routes, url='/study_programs/')
class Study_Programs:
    @Debug(name='study_programs')
    def __call__(self, request):
        return '200 OK', render('study_programs.html', date=date.today())

# Контакты
@AppRoute(routes=routes, url='/contacts/')
class Contact:
    @Debug(name='contact')
    def __call__(self, request):
        return '200 OK', render('contact.html', contact='+7999XXX5555', date=request.get('date', None))

# Создание категорий
@AppRoute(routes=routes, url='/create_category/')
class Create_Category:
    @Debug(name='create_category')
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category_id = data.get('category_id')
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
            new_category = site.create_category(name, category)
            site.categories.append(new_category)

            return '200 OK', render('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html', categories=categories)

# Список категорий
@AppRoute(routes=routes, url='/category_list/')
class Category_List:
        def __call__(self, request):
            logger.log('Список категорий')
            return '200 OK', render('category_list.html', date=request.get('date', None), objects_list=site.categories)


# Создание курсов
@AppRoute(routes=routes, url='/create_course/')
class Create_Course:
    category_id = -1
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))
                course = site.create_course('record', name, category)
                course.observers.append(email_notifier)
                course.observers.append(sms_notifier)
                site.courses.append(course)

            return '200 OK', render('course_list.html', objects_list=category.courses, name=category.name, id=category.id)
        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create_course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'Not added'



# Список курсов
@AppRoute(routes=routes, url='/course_list/')
class Course_List:
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return '200 OK', render('course_list.html', objects_list=category.courses, name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'Not added'


# Копирование курсов
@AppRoute(routes=routes, url='/copy_course/')
class Copy_Course:
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', render('course_list.html', objects_list=site.courses, name=new_course.category.name)
        except KeyError:
            return '200 OK', 'Not added'

# Страница не найдена
class NotFound404:
    @Debug(name='NotFound404')
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


# Список студентов
@AppRoute(routes=routes, url='/student_list/')
class StudentListView(ListView):
    queryset = site.students
    template_name = 'student_list.html'

# Создание студентов
@AppRoute(routes=routes, url='/create_student/')
class StudentCreateView(CreateView):
    template_name = 'create_student.html'

    def create_obj(self, data: dict):
        name = data['name']
        name = site.decode_value(name)
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)
    
# Добавление студента на курс
@AppRoute(routes=routes, url='/add_student/')
class AddStudentByCourseCreateView(CreateView):
    template_name = 'add_student.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        context['students'] = site.students
        return context

    def create_obj(self, data: dict):
        course_name = data['course_name']
        course_name = site.decode_value(course_name)
        course = site.get_course(course_name)
        student_name = data['student_name']
        student_name = site.decode_value(student_name)
        student = site.get_student(student_name)
        course.add_student(student)

# Api для взаимодействия и отображение данных
@AppRoute(routes=routes, url='/api/')
class CourseApi:
    @Debug(name='CourseApi')
    def __call__(self, request):
        return '200 OK', BaseSerializer(site.courses).save()






