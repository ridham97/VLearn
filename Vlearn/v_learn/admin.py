from django.contrib import admin
from v_learn.models import Course, Topic, Mcq, VlearnUser
# Register your models here.

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Mcq)
admin.site.register(VlearnUser)
