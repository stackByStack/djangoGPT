import os
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import openai


@csrf_exempt
def gpt3_request(request): 
    if request.method == 'POST' :
        prompt = request.POST.get('prompt', '')
        # Call the OpenAI GPT-3 API
        # Replace 'YOUR_API_KEY' with your actual OpenAI API key
        openai.api_key = os.environ.get('API_KEY')
        response = openai.Completion.create(
            engine='gpt-3.5-turbo',
            prompt=prompt,
            max_tokens=1024,
            n = 1,
            stop=None,
            temperature=0.7,
        )

        return JsonResponse({'result': response.choices[0].text})
    return JsonResponse({'error': 'Invalid request method'})
