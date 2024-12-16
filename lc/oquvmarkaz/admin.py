from django.contrib import admin
from .models import Curs,Lesson

# Register your models here.
from django.contrib import admin
from .models import Curs, Lesson

class LessonsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'curs')
    list_display_links = ('pk',)  # 'curs'ni olib tashladik
    list_editable = ('curs',)  # To'g'ri formatda yozildi
    list_filter = ('curs', 'name')
    search_fields = ('pk', 'name')  # 'lesson'ni 'name' bilan almashtirdik
    list_per_page = 2

admin.site.register(Curs)
admin.site.register(Lesson, LessonsAdmin)
