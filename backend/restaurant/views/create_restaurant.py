from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.serializers.create_restaurant import CreateRestaurantSerializer


class AdminCreateRestaurantView(APIView):
    """Admin can create restaurant."""

    permission_classes = [IsAdminUser]

    def post(self, request):
        create_restaurant = CreateRestaurantSerializer(data=request.data)
        create_restaurant.is_valid(raise_exception=True)
        create_restaurant.save()
        return Response(
            {"detail": "Restaurant successfully created"},
            status=status.HTTP_201_CREATED,
        )
