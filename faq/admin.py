from django.contrib import admin # type: ignore
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'language')

admin.site.register(FAQ, FAQAdmin)
