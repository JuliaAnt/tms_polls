from django.contrib import admin

from polls.models import Question, Choice

admin.site.register(Question, admin.ModelAdmin)
admin.site.register(Choice, admin.ModelAdmin)