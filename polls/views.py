import time
import random

from django.http.response import HttpResponse
from django.shortcuts import render

from polls.helpers import calculate_sum


def index_view(request):
    user_agent = request.META['HTTP_USER_AGENT']

    return HttpResponse('Your user agent is: {}'.format(user_agent))


def contact_us_view(request):
    welcome_text = 'You opened page'
    result = None
    circles = []

    if request.method == 'POST':
        welcome_text = 'You have submitted form'
        number_a = int(request.POST['number_a'])
        number_b = int(request.POST['number_b'])

        result = calculate_sum(number_a, number_b)

        random_color = lambda: random.randint(0, 255)

        for n in range(result):
            color = 'rgb({r}, {g}, {b})'.format(
                r=random_color(),
                g=random_color(),
                b=random_color()
            )
            circles.append({
                'name': '#%s' % n,
                'color': color
            })

    context = {
        'current_time': time.strftime('%H:%M:%S %A'),
        'welcome_text': welcome_text,
        'result': result,
        'circles': circles
    }

    return render(request, 'contact_us.html', context=context)


def questions(request):
    from polls.models import Question
    from datetime import datetime

    q = Question(question_text='How do you feel today?', pub_date=datetime.utcnow())
    q.save()

    questions = Question.objects.all()

    return render(request, 'questions.html', context={'questions': questions})