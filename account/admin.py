from django.contrib import admin

@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ("Change Avatar", {
            'fields': ['avatar']
        }),
    )