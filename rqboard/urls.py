from django.urls import path
from . import views

#네임스페이스변수지정(다른 앱에서 동일한 url별칭 사용시 중복 방지)
app_name='rqboard'

urlpatterns = [
    path('', views.index),
    
    #http://localhost:8000/rqboard/1 이 동작하도록 수정
    #path('<int:question_id>/', views.detail),

    #링크의 주소 대신 별칭 사용
    path('<int:question_id>/', views.detail, name='detail'),

    #답변등록 기능path추가
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    #질문등록  {% url 'rqboard:question_create'%}
    path('question/create/', views.question_create, name='question_create'),
]