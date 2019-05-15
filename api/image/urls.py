from django.conf.urls import url, include

from image.views import ImageViewSet

from rest_framework.routers import SimpleRouter

app_name = 'image'

router = SimpleRouter()
router.register(r'image', ImageViewSet)

urlpatterns = []
urlpatterns += router.urls
