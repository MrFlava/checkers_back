from rest_framework.serializers import ModelSerializer

from checkers_statistics.models import Statistics


class StatisticsSerializer(ModelSerializer):

    class Meta:
        model = Statistics
        fields = ("player_1", "player_2", "score", "winner")
