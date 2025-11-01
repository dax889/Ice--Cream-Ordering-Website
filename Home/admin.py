from django.contrib import admin
from Home.models import Contact,LoginRecord, SignupRecord,FeedbackForm,Product



# Register your models here.
admin.site.register(Contact)
admin.site.register(FeedbackForm)
admin.site.register(LoginRecord)
admin.site.register(SignupRecord)
admin.site.register(Product)