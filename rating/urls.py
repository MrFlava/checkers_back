from django.urls import path

from rating.views import UsersListView

app_name = "statistics"

urlpatterns = [
    path('users-list/', UsersListView.as_view(), name='users-list'),
]
