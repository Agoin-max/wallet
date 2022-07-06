from django.urls import path

from user import views

from user.kingdee import views_kingdee

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('token/check', views.LoginView.as_view()),
    path('token/init', views_kingdee.RegisterView().as_view())
]
