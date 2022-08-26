from django.urls import path
from . import views
urlpatterns=[
        path('blrtrip/',views.Hook.as_view()),
        ]
