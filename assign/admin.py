from django.contrib import admin

from .models import about_us, social

class aboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = about_us.objects.count()
        if count == 0:
            return True  # Allow adding if there are no existing entries
        return False  # Prevent adding if there is already an entry

# Register your models here.
admin.site.register(about_us, aboutAdmin)
admin.site.register(social)
