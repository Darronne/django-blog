from django.contrib import admin
from .models import Post, Partition, Region

admin.site.register(Post)
admin.site.register(Partition)
admin.site.register(Region)