from rest_framework.serializers import ModelSerializer

from restaurant.models import RestaurantModel


class CreateRestaurantSerializer(ModelSerializer):
    class Meta:
        model = RestaurantModel
        fields = [
            "restaurant_id",
            "restaurant_name",
            "phone_number",
            "location_latitude",
            "location_longitude",
            "website",
            "opening_hour",
            "closing_hour",
        ]
