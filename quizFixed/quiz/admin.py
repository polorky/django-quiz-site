from django.contrib import admin
from quiz.models import Answer, Round, Quiz, UserProfileInfo

# Register your models here.
admin.site.register(Answer)
admin.site.register(Round)
admin.site.register(Quiz)
admin.site.register(UserProfileInfo)
