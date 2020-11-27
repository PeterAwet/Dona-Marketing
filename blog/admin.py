from django.contrib import admin
from .models import Category, Post
from users.models import Signup

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	# Admin view for category..
	list_display = ('title','slug',)
	prepopulated_fields = {'slug':('title',)}
admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
	#Admin view for product...
	list_display = ('title','slug','category','created','updated',)
	list_filter = ('created','updated',)
	#list_editable = ('price','stock','available',)
	prepopulated_fields = {'slug':('title','category',)}
admin.site.register(Post,PostAdmin)

#admin.site.register(Post)

admin.site.register(Signup)
