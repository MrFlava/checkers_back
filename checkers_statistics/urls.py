from django.urls import path

from checkers_statistics.views import StatisticsCreateView, MyStatisticsView

app_name = "statistics"

urlpatterns = [
    path('create/', StatisticsCreateView.as_view(), name='create-game-statistics'),
    path('my-statistics/', MyStatisticsView.as_view(), name='my-statistics')
]
