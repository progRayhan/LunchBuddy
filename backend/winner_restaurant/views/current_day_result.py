from django.db.models import Count
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from winner_restaurant.models import WinnerRestaurantModel


class CurrentDayWinnerResultView(APIView):
    """User & admin can get current day winner result."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_date = timezone.now().date()
        winner_restaurant = (
            WinnerRestaurantModel.objects.filter(created_at__date=current_date)
            .values("restaurant__restaurant_name")
            .annotate(total_vote=Count("restaurant__restaurant_name"))
        )
        return Response(winner_restaurant, status=status.HTTP_200_OK)
