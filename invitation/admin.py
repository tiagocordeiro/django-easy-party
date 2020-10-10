from django.contrib import admin

from .models import Invite, GuestInvite, InviteTemplate, InviteCategory


class GuestsInline(admin.StackedInline):
    model = GuestInvite
    extra = 0


class InviteAdmin(admin.ModelAdmin):
    list_display = ('name', 'invite_template', 'age', 'date', 'maximum_guests')
    inlines = [
        GuestsInline,
    ]


class InviteTemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)


class InviteCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Invite, InviteAdmin)
admin.site.register(InviteTemplate, InviteTemplateAdmin)
admin.site.register(InviteCategory, InviteTemplateAdmin)
