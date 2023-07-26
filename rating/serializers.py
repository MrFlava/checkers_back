from django.contrib.auth.models import User
from rest_framework import serializers

from checkers_statistics.models import Statistics


class UsersListSerializer(serializers.ModelSerializer):
    won_games = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "won_games")

    def get_won_games(self, obj):
        won_games = Statistics.objects.filter(winner=obj).count()

        return won_games
