from django.shortcuts import render
from .models import Questions, Submissions, UserProfile, User
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def question(request, question_id):
    if request.method == 'POST':
        code = request.POST.get('code')
        a = Submissions.objects.create(code=code)
        a.save()
    else:
        try:
            question = Questions.objects.get(id=question_id)
        except ObjectDoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'basic/questionHub.html', {'question': question})


def index(request):
    all_questions = Questions.objects.all()
    context = {'all_questions': all_questions}
    return render(request, 'basic/questions.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        a = User.objects.create_user(username=username, password=password)
        a.save()
        login(request, a)
        b = UserProfile()
        b.user = a
        b.save()
        all_questions = Questions.objects.all()
        context = {'all_questions': all_questions}
        return render(request, 'basic/questions.html', context)
    return render(request, 'basic/Login.html')
