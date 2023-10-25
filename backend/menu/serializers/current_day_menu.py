from rest_framework.serializers import ModelSerializer

from menu.models import MenuModel


class CurrentDayMenuSerializer(ModelSerializer):
    class Meta:
        model = MenuModel
        fields = [
            "id",
            "item_id",
            "food_name",
            "description",
            "price",
            "vote_count",
            "restaurant",
            "created_at",
        ]
