from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# `scripts` klasöründen `read_logs` modülünü import edin
from scripts.read_logs import process_query

def index(request):
    return render(request, 'index.html')  # Ana sayfanızın şablonu

@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        # Soruyu `read_logs.py`'deki fonksiyonla işleyin
        response = process_query(question)
        return JsonResponse({'answer': response})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
