from rest_framework.serializers import ModelSerializer

from menu.models import MenuModel


class UploadMenuSerializer(ModelSerializer):
    class Meta:
        model = MenuModel
        fields = ["item_id", "food_name", "description", "price", "restaurant"]
