from django.contrib import admin
from .models import *

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)
admin.site.register(Result)
admin.site.register(CategotyQuiz)