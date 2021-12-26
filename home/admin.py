from django.contrib import admin
from home.models import Contact, SignedUp, Post

# Register your models here.
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(SignedUp)
