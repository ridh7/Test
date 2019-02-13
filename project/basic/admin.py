from django.contrib import admin
from .models import Questions, UserProfile, Submissions
# Register your models here.
admin.site.register(Questions)
admin.site.register(UserProfile)
admin.site.register(Submissions)
