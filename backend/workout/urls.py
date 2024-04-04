from django.urls import path
from . import views


urlpatterns = [
    path(
        "exercise/",
        views.ExerciseSetViewSet.as_view({"get": "list", "post": "create"}),
        name="exercise-list",
    ),
    path(
        "exercise/<int:pk>/",
        views.ExerciseSetViewSet.as_view({"get": "retrieve"}),
        name="exercise-detail",
    ),
]
