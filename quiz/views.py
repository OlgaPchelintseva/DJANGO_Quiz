from django.shortcuts import render, redirect
from .questions import QUESTIONS

def start(request):
    if request.method == 'POST':
        request.session['score'] = 0
        request.session['current_question_index'] = 0
        request.session.modified = True
        return redirect('quiz')
    return render(request, 'quiz/start_quiz.html')

def questions(request):
    if 'current_question_index' not in request.session:
        return redirect('start_quiz')
    
    index = request.session['current_question_index']
    if index >= len(QUESTIONS):
        return redirect('result_quiz')
    
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer == QUESTIONS[index]['answer']:
            request.session['score'] += 1
        request.session['current_question_index'] += 1
        request.session.modified = True
        return redirect('quiz')

    else: 
        question = QUESTIONS[index]['question']
        options = QUESTIONS[index]['options']
        context = {
            'index': index,
            'question': question,
            'options': options,
            'all_questions': len(QUESTIONS),
        }
        return render(request, 'quiz/quiz.html', context)

def result(request):
    context = {
        'score': request.session.get('score', 0),
        'all_questions': len(QUESTIONS),
    }

    if request.method == 'POST':
        request.session.flush()
        return redirect('start_quiz')

    return render(request, 'quiz/result_quiz.html', context)