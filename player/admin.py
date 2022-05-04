from django.contrib import admin
from .models import player,team,invitation

# Register your models here.
admin.site.register(team)
admin.site.register(player)
admin.site.register(invitation)
