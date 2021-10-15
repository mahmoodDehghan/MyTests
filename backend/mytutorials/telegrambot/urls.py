from django.urls import path
from .views import start_bot, end_bot

urlpatterns = [
  path('startbot/', start_bot),
  path('endbot/', end_bot),
]