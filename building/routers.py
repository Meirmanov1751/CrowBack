from django.conf import settings
from rest_framework.routers import DefaultRouter
from transaction.views import ProjectPlanViewSet,ProjectBackedViewSet
from project.views import ProjectListViewSet,CategorieViewSet,RelationsProfileDetailView
from django.urls import path,include
from django.conf.urls.static import static
from comment.views import CommentViewset,CommentRelViewset

router = DefaultRouter()

router.register(r'project',ProjectListViewSet ,basename=1)
router.register(r'categories',CategorieViewSet )
router.register(r'relations',RelationsProfileDetailView )

router.register(r'project_plan',ProjectPlanViewSet ,basename=2)
router.register(r'project_plan_backed',ProjectBackedViewSet )


router.register(r'comment',CommentViewset )
router.register(r'comment_relations',CommentRelViewset )

urlpatterns = [
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)