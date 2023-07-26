from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from auth_app.authentication import TokenAuthentication
from rating.serializers import UsersListSerializer


class UsersRatingView(ListAPIView):
    serializer_class = UsersListSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        return queryset
