from django.contrib import admin
from django.apps import apps
from django.contrib.auth.models import Group, User

from .models import Image, Offer

admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
models = apps.get_models()

for model in models:
    admin.site.register(model)

admin.site.unregister(Offer)


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
