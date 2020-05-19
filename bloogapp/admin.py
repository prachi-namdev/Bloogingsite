from django.contrib import admin
from bloogapp.models import blog,POSTBLOG
# Register your models here.
class Admin(admin.ModelAdmin):
    list_display=['username','password','emailaddress','firstname','lastname']
admin.site.register(blog,Admin)
admin.site.register(POSTBLOG)
