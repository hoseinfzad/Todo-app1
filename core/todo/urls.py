from django.urls import path, include
from . import views 



urlpatterns = [
    path("", views.index, name="task_list"),
    path("update/<str:pk>/", views.update_task, name="update_task"),
    path("complete/<str:pk>/", views.complete_task, name="complete_task"),
    path("delete/<str:pk>/", views.delete_task, name="delete_task"),
    path('api/v1/', include('todo.api.v1.urls')),
]
