from django.urls import path

from auth_app.views import (
    LoginView,
    LogoutView,
    CurrentUserView,
    CurrentUserUpdateView,
    RegisterView,
    RefreshTokenView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
    path('current-user-update/', CurrentUserUpdateView.as_view(), name='current-user-update'),
    path('refresh-token/', RefreshTokenView.as_view(), name='refresh-token'),
]
