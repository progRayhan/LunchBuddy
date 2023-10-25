from django.utils import timezone

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from menu.models import MenuModel
from menu.serializers.current_day_menu import CurrentDayMenuSerializer
from utils.utils import CustomPagination


class CurrentDayMenuView(ListAPIView):
    """User can find current day restaurant menu."""

    permission_classes = [IsAuthenticated]
    serializer_class = CurrentDayMenuSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        current_date = timezone.now().date()
        queryset = MenuModel.objects.filter(created_at__date=current_date)
        return queryset
