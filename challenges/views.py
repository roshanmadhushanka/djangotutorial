from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    _monthly_challenge = None
    if month == 'january':
        _monthly_challenge = 'Complete 2 coding projects'
    elif month == 'february':
        _monthly_challenge = 'Learn a programming language'
    elif month == 'march':
        _monthly_challenge = 'Workout month'
    else:
        return HttpResponseNotFound()
    return HttpResponse("Weekly challenge : {}".format(_monthly_challenge))


def monthly_challenges_by_index(request: HttpRequest, index: int) -> HttpResponse:
    return HttpResponse('Month index is : {}'.format(index))

