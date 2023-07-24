from django.urls import path

from checkers_statistics.views import StatisticsCreateView

app_name = "statistics"

urlpatterns = [
    path('create/', StatisticsCreateView.as_view(), name='create-game-statistics'),
]
