from django.contrib import admin

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        [
            'Main',{
                'fields': ['username'],
        }
        ],
        [
            'Advance',{
                'classes': ('collapse',),
                'fields': ['score',],
            }
        ]
    )
