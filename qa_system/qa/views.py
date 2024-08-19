from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Model ve tokenizer'ı yükleyin
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def index(request):
    return render(request, 'index.html')  # Ana sayfanızın şablonu

@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        
        # Soruyu direkt olarak modelle işleyin
        inputs = tokenizer(question, return_tensors="pt")
        # Model ile tahmin yapın, daha fazla çeşitlilik ve detay eklemek için parametreleri değiştirin
        outputs = model.generate(inputs["input_ids"], max_length=150, num_return_sequences=1, do_sample=True, top_k=50, top_p=0.9, temperature=1.2, early_stopping=True)
        # Yanıtı decode edin
        beautified_answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return JsonResponse({'answer': beautified_answer})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
