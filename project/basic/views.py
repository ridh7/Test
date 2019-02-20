from django.shortcuts import render
from .models import Questions, Submissions, UserProfile, User
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
import os
path = 'data\\codes'

global attempts


def question(request, question_id):
    if request.method == 'POST':
        user = request.user
        user1 = UserProfile.objects.get(user=request.user)
        if not os.path.exists('{}/{}'.format(path, user)):
            for i in range(1, 7):
                os.system('mkdir {}\\{}\\question{}'.format(path, user, i))
        user1.attempts = user1.attempts + 1
        user1.save()
        f = open('{}\\{}\\question{}\\{}.cpp'.format(path, user, question_id, user1.attempts), 'w')
        code = request.POST.get('code')
        f.write(code)
        f.close()
        a = Submissions(user=request.user, code=code)
        a.save()
        return HttpResponse("hahahahah")
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
        return index(request)
    return render(request, 'basic/Login.html')


def welcome(request):
    return render(request, 'basic/Welcome.html')


def e_login(request):
    if request.method == 'POST':
        admin_password = '1'
        username = request.POST.get('user')
        password = request.POST.get('pass')
        _password = request.POST.get('pass1')
        user = authenticate(username=username, password=password)

        if user is not None and _password is admin_password:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('question'))

        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'basic/e_login.html', {})
