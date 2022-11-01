from django.contrib import admin
from .models import Comment,CommentRelasions
# Register your models here.



class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('creted_date','update_date')


admin.site.register(Comment,RatingAdmin)
admin.site.register(CommentRelasions)
