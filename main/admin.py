from django.contrib import admin
from .models import (
    AnalyticsQuestion, AnalyticsStudent, AnalyticsSurvey, AnalyticsSurveyresponse,
    Course, CourseAssignment, Professor,
    Student, StudentCourse,
    Survey, SurveyQuestion, SurveyResponse
)

@admin.register(AnalyticsQuestion)
class AnalyticsQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'survey')
    search_fields = ('text',)

@admin.register(AnalyticsStudent)
class AnalyticsStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faculty', 'academic_year')
    search_fields = ('name', 'faculty')

@admin.register(AnalyticsSurvey)
class AnalyticsSurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    search_fields = ('name',)

@admin.register(AnalyticsSurveyresponse)
class AnalyticsSurveyresponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'response', 'question', 'student')
    list_filter = ('response',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'professor', 'created_at')
    search_fields = ('name', 'professor__name')
    list_filter = ('created_at',)

@admin.register(CourseAssignment)
class CourseAssignmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'faculty', 'academic_year', 'study_mode')
    list_filter = ('faculty', 'academic_year', 'study_mode')
    search_fields = ('course__name',)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'avatar_url', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'faculty', 'academic_year', 'mode_of_study', 'created_at')
    list_filter = ('gender', 'faculty', 'academic_year', 'mode_of_study')
    search_fields = ('faculty',)

@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    list_filter = ('enrolled_at',)
    search_fields = ('student__name', 'course__name')

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')

@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'text', 'question_type', 'question_category', 'question_order', 'created_at')
    search_fields = ('text', 'survey__name')
    list_filter = ('question_type', 'question_category')

@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('anonymous_id', 'question', 'survey', 'response_at')
    search_fields = ('anonymous_id', 'question__text', 'survey__name')
    list_filter = ('response_at',)
