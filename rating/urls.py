from django.urls import path

from rating.views import UsersRatingView

app_name = "statistics"

urlpatterns = [
    path('users-rating/', UsersRatingView.as_view(), name='users-rating'),
]
