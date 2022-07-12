from django.urls import path
from .views import FileView

urlpatterns = [
    path('',FileView.as_view()),
    path('api/', FileView.as_view())
]