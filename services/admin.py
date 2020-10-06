from django.contrib import admin

from services.models import Wordpress_comment, Html_Css_Javascript, PythonandDjango

# Register your models here.

admin.site.register(Wordpress_comment)
admin.site.register(Html_Css_Javascript)
admin.site.register(PythonandDjango)