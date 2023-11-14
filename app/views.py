from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator

QUESTIONS = [
    {
        'id': i,
        'title': f'Вопрос {i + 1}',
        'text': f'Что из себя представляет исключение Null Pointer Exception (java.lang.NullPointerException)\
                и почему оно может происходить? Какие методы и средства использовать, чтобы определить причину\
                возникновения этого исключения, приводящего к преждевременному прекращению работы приложения?',
        'user_name': 'Username',
        'date': 'Вопрос задан 30 сентября 2023 г. в 13:47',
        'tags': ['Java', 'Указатели'],
        'answers_num': 15
    } for i in range(100)
]


def paginate(objects, page_num, per_page=10):
    paginator = Paginator(objects, per_page)
    return paginator.get_page(page_num)


def index(request):
    page_num = request.GET.get('page')
    return render(request, 'index.html', {'items': paginate(QUESTIONS, page_num)})


def question(request, question_id):
    item = QUESTIONS[question_id]
    page_num = request.GET.get('page')
    answers = [
        {
            'id': i,
            'text': f'Когда вы объявляете переменную ссылочного типа, на самом деле вы создаете ссылку на объект\
                    данного типа. Рассмотрим следующий код для объявления переменной типа int\
                    int x\
                    x = 10\
                    В этом примере переменная x имеет тип int и Java инициализирует её как 0. Когда вы присвоите\
                    переменной значение 10 (вторая строка), это значение сохранится в ячейке памяти, на которую\
                    ссылается x.',
            'user_name': 'JavaUser',
            'date': 'Ответ дан 30 сентября 2023 г. в 19:32'
        } for i in range(15)
    ]
    return render(request, 'question.html', {'question': item,
                                             'items': paginate(answers, page_num)})


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
