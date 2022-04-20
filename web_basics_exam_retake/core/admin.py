from django.contrib import admin

# Register your models here.
from web_basics_exam_retake.core.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass