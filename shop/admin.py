from django.contrib import admin
from .models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display=('id','Name','Email','Mobile','Message')
admin.site.register(contact,contactusAdmin)


class categoryAdmin(admin.ModelAdmin):
    list_display=('id','Name','CPic')
admin.site.register(category,categoryAdmin)


class maincateAdmin(admin.ModelAdmin):
    list_display=('id','Name','picture','cdate')
admin.site.register(maincate,maincateAdmin)


class productAdmin(admin.ModelAdmin):
    list_display=('id','mcategory','pcategory','pprice','dprice','psize','pcolor','pdes','pdel','ppic','pdate')
admin.site.register(myproduct,productAdmin)


class registerAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile','ppic','passwd','address')
admin.site.register(register,registerAdmin)


class mcartAdmin(admin.ModelAdmin):
    list_display=('id','userid','pid','cdate','status')
admin.site.register(mcart,mcartAdmin)


class morderAdmin(admin.ModelAdmin):
    list_display=('id','userid','pid','remarks','odate','status')
admin.site.register(morder,morderAdmin)
