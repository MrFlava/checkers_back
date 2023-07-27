from django.contrib.auth.models import User
from rest_framework import serializers
from django.db.models import Q

from checkers_statistics.models import Statistics


class UsersListSerializer(serializers.ModelSerializer):
    won_games = serializers.SerializerMethodField()
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "won_games", "total_score")

    def get_won_games(self, obj):
        won_games = Statistics.objects.filter(winner=obj).count()

        return won_games

    def get_total_score(self, obj):
        scores = Statistics.objects.filter(Q(player_1=obj) | Q(player_2=obj)).values_list('score', flat=True)
        return sum(scores)
