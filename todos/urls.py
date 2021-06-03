
from rest_framework.routers import SimpleRouter

from .views import TodoViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', TodoViewSet)

urlpatterns = router.urls