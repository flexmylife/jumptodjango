from django import forms
from rqboard.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:  #내부 클래스/ 사용할 모델과 모델의 속성을 적어야함
        model = Question
        fields = ['subject', 'content']
#장고의 폼은 일반폼과 모델폼이 있다.
#모델폼은 모델과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할 수 있게 된다.
