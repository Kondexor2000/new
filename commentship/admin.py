from textblob import TextBlob
from django.contrib import admin
from django.http import HttpResponse

# Register your models here.

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'analyze_sentiment']
    actions = ['analyze_selected_comments']

    def analyze_selected_comments(self, request, queryset):
        for comment in queryset:
            blob = TextBlob(comment.content)
            translation = blob.translate(from_lang="pl", to="en")
            sentiment = translation.sentiment

            if sentiment.polarity > 0:
                emocje = "To jest miły komentarz!"
            elif sentiment.polarity < 0:
                emocje = "Komentarz nie jest na miejscu"
            else:
                emocje = "Komentarz nie ma nic szczególnego"

            comment.sentiment = emocje
            comment.save()

    analyze_selected_comments.short_description = "Analyze selected comments"

admin.site.register(Comment, CommentAdmin)