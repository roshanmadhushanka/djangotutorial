from django.urls import path
from . import views

urlpatterns = [
    path('<int:index>', views.monthly_challenges_by_index),
    path('<str:month>', views.monthly_challenge),

]
