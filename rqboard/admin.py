from django.contrib import admin
from .models import Question
# Register your models here.

#1
# admin.site.register(Question)


#2
# 관리자 화면에서 제목으로 질문을 검색할수 있는 기능
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question,QuestionAdmin)