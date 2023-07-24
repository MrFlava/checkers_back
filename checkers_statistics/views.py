from rest_framework.generics import CreateAPIView, ListAPIView
from django.db.models import Q

from checkers_statistics.serializers import StatisticsSerializer
from checkers_statistics.models import Statistics


class StatisticsCreateView(CreateAPIView):
    serializer_class = StatisticsSerializer


class MyStatisticsView(ListAPIView):
    serializer_class = StatisticsSerializer

    def get_queryset(self):
        queryset = Statistics.objects.filter(Q(player_1=self.request.user) | Q(player_2=self.request.user))
        return queryset
