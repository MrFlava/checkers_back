from rest_framework.generics import CreateAPIView


from checkers_statistics.serializers import StatisticsSerializer


class StatisticsCreateView(CreateAPIView):
    serializer_class = StatisticsSerializer
