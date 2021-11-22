from rest_framework import viewsets
from .serializers import TodoSerializers
from .models import Todo


class todoviewsets(viewsets.ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()
    http_method_names = ['get',]