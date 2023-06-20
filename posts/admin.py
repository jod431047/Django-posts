from django.contrib import admin

# Register your models here.
from .models import post , Author


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','publish_date']
    list_filter = ['Author','tags','publish_date']

admin.site.register(post,PostAdmin)
admin.site.register(Author)