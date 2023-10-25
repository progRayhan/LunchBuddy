from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from vote.serializers.voting_menu import VotingMenuSerializer


class VotingMenuView(APIView):
    """User can give vote for restaurant menu."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        vote_data = VotingMenuSerializer(data=request.data)
        vote_data.is_valid(raise_exception=True)
        vote_data.save()
        return Response({"detail": "Vote done"}, status=status.HTTP_200_OK)
