from django.contrib import admin
from authentication.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(User)