from django.contrib import admin
from apps.post.models import Post, Category, PostImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at',
                    'updated_at', 'allow_comments')
    search_fields = ('title', 'content',
                     'author__username', 'author__id', 'id')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'allow_comments')
    ordering = ('-created_at',)


class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'active')
    search_fields = ('post__title', 'post__id', 'image', 'id')
    list_filter = ('active',)
    ordering = ('-created_at',)

    def activate_images(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(
            request, f"{updated} imagenes fueron activadas correctamente")
    activate_images.short_description = "Activar imagenes seleccionadas"

    def deactivate_images(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(
            request, f"{updated} imagenes fueron desactivadas correctamente")
    deactivate_images.short_description = "Desactivar imagenes seleccionadas"

    actions = [activate_images,
               deactivate_images]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostImage, PostImageAdmin)