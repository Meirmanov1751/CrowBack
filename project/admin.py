from django.contrib import admin

# Register your models here.
from .models import Project,Categorie,Relations
admin.site.register(Categorie)

admin.site.register(Relations)


class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('published_data','update_date')


admin.site.register(Project,RatingAdmin)





