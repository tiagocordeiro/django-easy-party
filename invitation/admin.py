from django.contrib import admin

from .models import Invite, GuestInvite


class GuestsInline(admin.StackedInline):
    model = GuestInvite
    extra = 0


class InviteAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'date', 'maximum_guests')
    inlines = [
        GuestsInline,
    ]


admin.site.register(Invite, InviteAdmin)
