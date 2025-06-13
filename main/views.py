from django.db.models import Count, Avg, IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render
from .models import SurveyResponse, Professor

def home(request):
    return  render(request, 'home.html', {})

def singleRating(request):
    selected_professor_id = request.GET.get("professor")
    professors = Professor.objects.all()

    responses = SurveyResponse.objects.all()
    if selected_professor_id:
        responses = responses.filter(professor_id=selected_professor_id)
    else:
        # Если преподаватель не выбран, можно либо показывать пустую статистику, либо всех
        responses = SurveyResponse.objects.none()

    # Подсчёт количества ответов по оценкам (приводим content к IntegerField)
    rating_counts = (
        responses
        .annotate(score=Cast('content', IntegerField()))
        .values('score')
        .annotate(count=Count('anonymous_id'))
        .order_by('score')
    )

    # Инициализация словаря с нулями для оценок 1-5
    chart_data = {str(i): 0 for i in range(1, 6)}
    for entry in rating_counts:
        rating = str(entry['score'])
        if rating in chart_data:
            chart_data[rating] = entry['count']

    return render(request, 'singleRating.html', {
        'professors': professors,
        'selected_professor_id': selected_professor_id,
        'chart_data': chart_data,
        'responses': responses,
    })



def overallRating(request):
    # Средний балл по каждому преподавателю
    average_ratings = (
        SurveyResponse.objects
        .annotate(score=Cast('content', IntegerField()))
        .values('professor_id', 'professor__name')
        .annotate(avg_score=Avg('score'))
        .order_by('professor__name')
    )

    # Добавляем преподавателей без оценок (с avg_score=0)
    all_professors = Professor.objects.all()
    prof_dict = {prof['professor_id']: prof for prof in average_ratings}

    # Формируем итоговый список, включая преподавателей без ответов
    result = []
    for prof in all_professors:
        data = prof_dict.get(prof.id)
        avg = round(data['avg_score'], 2) if data and data['avg_score'] is not None else 0
        result.append({
            'professor_id': prof.id,
            'professor__name': prof.name,
            'avg_score': avg
        })

    return render(request, 'overallRating.html', {
        'average_ratings': result,
    })
