from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from auth_app.authentication import TokenAuthentication
from checkers_statistics.serializers import StatisticsSerializer
from checkers_statistics.models import Statistics


class StatisticsCreateView(CreateAPIView):
    serializer_class = StatisticsSerializer


class MyStatisticsView(ListAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        queryset = Statistics.objects.filter(Q(player_1=self.request.user) | Q(player_2=self.request.user))
        return queryset
