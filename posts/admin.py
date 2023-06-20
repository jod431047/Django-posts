from django.contrib import admin

# Register your models here.
from .models import post , Author

admin.site.register(post)
admin.site.register(Author)