from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import MenuModel
from vote.serializers.voting_menu import VotingMenuSerializer
from winner_restaurant.serializers.winner_restaurant import WinnerRestaurantSerializer


class VotingMenuView(APIView):
    """User can give vote for restaurant menu."""

    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        menu = request.data.get("menu")
        vote = request.data.get("vote")
        employee_phone_number = request.data.get("employee_phone_number")

        voting_data = {
            "menu": menu,
            "vote": vote,
            "employee_phone_number": employee_phone_number,
        }

        vote_data = VotingMenuSerializer(data=voting_data)
        vote_data.is_valid(raise_exception=True)

        get_restaurant_id = get_object_or_404(MenuModel, id=menu).restaurant.id
        create_restaurant = WinnerRestaurantSerializer(
            data={"restaurant": get_restaurant_id}
        )
        create_restaurant.is_valid(raise_exception=True)

        with transaction.atomic():
            vote_data.save()
            create_restaurant.save()

        return Response({"detail": "Vote done"}, status=status.HTTP_200_OK)
