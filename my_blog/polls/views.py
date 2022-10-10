from django.shortcuts import render, get_object_or_404
from .models import Question

def get_question_list(request):
    question = Question.objects.all()
    context = {
        "question": question
    }
    return render(template_name='question_list.html', request=request, context=context)

def get_question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        "question": question
    }
    return render(template_name='question_detail.html', request=request, context=context)

