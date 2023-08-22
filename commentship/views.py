from django.shortcuts import render
from textblob import TextBlob
from django.contrib import admin
from django.http import JsonResponse

def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        
        blob = TextBlob(text)
        translation = blob.translate(from_lang="pl", to="en")
        sentiment = translation.sentiment
        
        if sentiment.polarity > 0:
            emocje = "To jest miły komentarz!"
        elif sentiment.polarity < 0:
            emocje = "Komentarz nie jest na miejscu"
        else:
            emocje = "Komentarz nie ma nic szczególnego"
        
        response_data = {
            'sentiment': emocje
        }
        
        return JsonResponse(response_data)
