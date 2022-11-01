from rest_framework.routers import DefaultRouter
from .views import ExampleRelatedModelViewSet, ExampleViewSet
router = DefaultRouter()
router.register(r'^example/example', ExampleViewSet)
router.register(r'^example/example-related', ExampleRelatedModelViewSet)
