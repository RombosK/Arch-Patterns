# from datetime import datetime
from views import Index, Contact, Category_List, Course_List, Create_Category, Create_Course, Study_Programs, Copy_Course
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
    '/category_list/': Category_List(),
    '/course_list/': Course_List(),
    '/create_category/': Create_Category(),
    '/create_course/': Create_Course(),
    '/study_programs/': Study_Programs(),
    '/copy_course/': Copy_Course(),
}


