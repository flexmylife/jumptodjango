#1 
# from django.shortcuts import render
# from django.http import HttpResponse
#2
#from .models import Question
#3
#from django.shortcuts import render, get_object_or_404

#4
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
            # Create your views here.
#1
# def index(request):
#    return HttpResponse("안녕하세요 수리신고 게시판에 오신것을 환영합니다.")
#2
def index(request):
    """
    rqboard 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'rqboard/question_list.html',context)

#detail page 함수 추가
def detail(request, question_id):
    """
    rqboard 내용 출력
    """
    #2 
    # question = Question.objects.get(id=question_id)
    #3
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'rqboard/question_detail.html', context)

def answer_create(request, question_id):
    """
    rqboard 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('rqboard:detail', question_id=question.id)

