from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from wallet.views import add_bal, send
urlpatterns = [
    path('', views.index),
    path('signup/', views.Signup, name="Signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', views.profile),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add/', add_bal, name="add"),
    path('send/', send, name="send")
]
