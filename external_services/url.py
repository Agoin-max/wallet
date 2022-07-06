from django.urls import path
from external_services.kingdee import views_kingdee

urlpatterns = [
    path('register', views_kingdee.RegisterView.as_view()),
]
