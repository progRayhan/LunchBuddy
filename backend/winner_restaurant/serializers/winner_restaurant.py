from rest_framework.serializers import ModelSerializer

from winner_restaurant.models import WinnerRestaurantModel


class WinnerRestaurantSerializer(ModelSerializer):
    class Meta:
        model = WinnerRestaurantModel
        fields = ["restaurant"]
