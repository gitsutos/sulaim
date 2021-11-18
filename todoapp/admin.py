from django.contrib import admin
from .models import Costlist

class Costadmin(admin.ModelAdmin):
    search_fields = ["user__username", "user__email"]
    class Meta:
        model = Costlist


admin.site.register(Costlist, Costadmin)

