from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(QuizInfo)
class QuizInfoadmin(admin.ModelAdmin):
    list_display=('topic','desc')
    
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display=('question','get_quiz')
    list_filter=('question',)
    def get_quiz(self, obj):
        return obj.quiz.topic
    get_quiz.short_description = "topic"


admin.site.register(Question, QuestionAdmin)
@admin.register(AnsCheck)
class AnswerAdmin(admin.ModelAdmin):
    list_display=('choice','question','quiz')   
     
@admin.register(UserResponse)
class UserResponseadmin(admin.ModelAdmin):
     list_display=('quiz','question','choice')
