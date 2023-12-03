from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Question, Answer
from datetime import datetime


def paginate(objects, page_num, per_page=10):
    paginator = Paginator(objects, per_page)
    return paginator.get_page(page_num)


def index(request):
    questions = Question.objects.new_questions_list()
    page_num = request.GET.get('page')
    return render(request, 'index.html', {'items': paginate(questions, page_num), 'type': 'new'})


def search(request, tag_name):
    questions = Question.objects.find_by_tag(tag_name)
    page_num = request.GET.get('page')
    return render(request, 'index.html', {'items': paginate(questions, page_num), 'type': 'search', 'tag': tag_name})


def show_hot(request):
    questions = Question.objects.hot_questions_list()
    page_num = request.GET.get('page')
    return render(request, 'index.html', {'items': paginate(questions, page_num), 'type': 'hot'})


def question(request, question_id):
    item = get_object_or_404(Question.objects.all(), pk=question_id)
    page_num = request.GET.get('page')
    answers = Answer.objects.answers_list(question_id)
    return render(request, 'question.html', {'question': item,
                                             'items': paginate(answers, page_num)})


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
