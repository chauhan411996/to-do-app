from django.urls import path, include
from.views import TodoListView,TodoDeleteView,TodoCreateView,TodoUpdateView


urlpatterns = [
    path('to-do-list/', TodoListView.as_view(), name='to_do_list'),
    path('to-do-delete/<int:pk>/', TodoDeleteView.as_view(), name='to_do_delete'),
    path('to-do-add/', TodoCreateView.as_view(), name='to_do_add'),
    path('to-do-update/<int:pk>/', TodoUpdateView.as_view(), name='to_do_update'),

]
