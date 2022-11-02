from django.contrib import admin
#from home.models import Register
# Register your models here.
#admin.site.register(Register)

from .models import *

admin.site.register(Course)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(Question)
admin.site.register(ScoreBoard)
admin.site.register(FilesAdmin)
admin.site.register(NotificationAdmin)
admin.site.register(TestProfile)
admin.site.register(Attendance)
admin.site.register(Lecture)
admin.site.register(Testattendance)
admin.site.register(Atten)