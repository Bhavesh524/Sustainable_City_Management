from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from api_handling.models import Bike


def index(request):
    latest_question_list = Bike.objects.create(name='Shep', data={'breed': 'collie'})
    template = loader.get_template('api_handling/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
