from .viewsets import todoviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', todoviewsets)