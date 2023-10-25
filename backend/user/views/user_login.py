from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializers.user_login import UserLoginSerializer


class LoginView(TokenObtainPairView):
    """User can login their account by using phone_number & password."""

    serializer_class = UserLoginSerializer
