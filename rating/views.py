from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from online_users.models import OnlineUserActivity

from auth_app.authentication import TokenAuthentication
from rating.serializers import UsersListSerializer


class UsersRatingView(ListAPIView):
    serializer_class = UsersListSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user_activity_objects = OnlineUserActivity.get_user_activities()
        queryset = [user.user for user in user_activity_objects]

        return queryset
