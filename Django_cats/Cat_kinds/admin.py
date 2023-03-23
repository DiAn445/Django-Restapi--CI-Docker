from django.contrib import admin
from .models import CatKinds


class CatKindsAdmin(admin.ModelAdmin):
    list_display = ('british', 'likes')
    list_display_links = ('british', 'likes')
    search_fields = ('british',)
    list_filter = ('likes', 'british',)

admin.site.register(CatKinds, CatKindsAdmin)
