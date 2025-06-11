from django.shortcuts import render
from .models import SurveyResponse

def home(request):
    responses = SurveyResponse.objects.filter() # правильное имя переменной
    context = {
        'responses': responses

    }
    return render(request, 'home.html', context)
