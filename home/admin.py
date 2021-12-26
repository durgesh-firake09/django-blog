from django.contrib import admin
from home.models import Comment, Contact, SignedUp, Post

# Register your models here.
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(SignedUp)
admin.site.register(Comment)
