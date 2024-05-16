from django.contrib import admin

# Register your models here.
from .models import SchoolData

class SchoolAdim(admin.ModelAdmin):
    list_display=("id","name","age","StudentClass")
# Register your models here.
admin.site.register(SchoolData,SchoolAdim)
