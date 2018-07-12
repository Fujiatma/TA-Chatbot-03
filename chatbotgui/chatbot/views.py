from django.shortcuts import render
from. import chatbot
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

def home(request):
    content = {
        'test': chatbot.chat('good morning')

    }
    return render(request, 'index.html', content)


@csrf_exempt
def chat(request):
    if (request.method == 'POST'):
        q = request.POST['q']
        data = {'answer': chatbot.chat(q)}
        return JsonResponse(data)