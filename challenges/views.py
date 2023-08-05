from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseRedirect

MONTHLY_CHALLENGES = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walt for at least 20 minutes every dat',
    'march': 'Learn a new programming language',
    'april': 'Service your car',
    'may': 'Swimming challenge with your friends',
    'june': 'BBQ day out challenge',
    'july': 'Win a game',
    'august': 'Fitness challenge',
    'september': 'Read two books',
    'october': 'Learn something new',
    'november': 'Help someone',
    'december': 'Christmas decoration'
}


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    if not month:
        return HttpResponseBadRequest('Month not defined')

    if month.lower() in MONTHLY_CHALLENGES:
        return HttpResponse('Monthly challenge for {} is : {}'.format(month, MONTHLY_CHALLENGES[month.lower()]))
    return HttpResponseNotFound()


def monthly_challenges_by_index(request: HttpRequest, index: int) -> HttpResponse:
    if 1 <= index <= 12:
        # return monthly_challenge(request, list(MONTHLY_CHALLENGES.keys())[index - 1])
        return HttpResponseRedirect('/challenges/{}'.format(list(MONTHLY_CHALLENGES.keys())[index - 1]))
    else:
        return HttpResponseBadRequest('Invalid month index range')

