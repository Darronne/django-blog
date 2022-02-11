from django.contrib import admin
from .models import Post, Partition, Region

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"url": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Partition)
admin.site.register(Region)