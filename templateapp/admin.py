from django.contrib import admin
from models import CategoryModel, TextModel, CommentModel

admin.site.register(CategoryModel)

@admin.register(TextModel)
class TextsAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    list_display = ('title', 'create_date', 'edit_date')
@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('writer__username', 'text', 'comment')
    list_display = ('writer','text', 'create_date', 'edit_date')