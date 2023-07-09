from django.contrib import admin

# Register your models here.

from .models import User, Category, Quiz, Question, Answer, Result

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
