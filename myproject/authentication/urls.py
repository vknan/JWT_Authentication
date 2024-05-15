from django.urls import path
from . import views

urlpatterns = [
    path('api/auth/register/', views.RegisterView.as_view(), name='register'),
    path('api/auth/login/', views.LoginView.as_view(), name='login'),
    path('api/auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('api/token/refresh/', views.CustomTokenObtainPairView.as_view(), name='token_refresh'),
]
