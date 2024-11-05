from django.urls import path
from . import views

urlpatterns = [
    path('', views.live_llm, name='live_llm'),
]