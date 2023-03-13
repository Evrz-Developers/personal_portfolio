from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Project, Skill


class CustomModelAdmin(ModelAdmin):
    actions = ['copy_record']

    def copy_record(self, request, queryset):
        for obj in queryset:
            obj.pk = None
            obj.save()

    copy_record.short_description = "Duplicate selected record"


admin.site.register(Skill)
admin.site.register(Project)
admin.site.unregister(Project)
admin.site.register(Project, CustomModelAdmin)
