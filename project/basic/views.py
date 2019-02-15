from django.shortcuts import render
from .models import Questions, Submissions, UserProfile, User
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
import os
path = 'data/codes'


def question(request, question_id):
    if request.method == 'POST':
        user = request.user
        #if not os.path.exists('{}/{}'.format(path, user)):
            #attempts = 0
        for i in range(1, 7):
            os.system('mkdir {}/{}/question{}'.format(path, user, i))
        #attempts += 1
#        f = open('{}/{}/question{}/{}.cpp'.format(path, user, question_id, attempts))
        code = request.POST.get('code')
 #       f.write(code)
  #      f.close()
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
        #return HttpResponseRedirect(reverse('index'))
    return render(request, 'basic/Login.html')


def welcome(request):
    return render(request, 'basic/Welcome.html')
