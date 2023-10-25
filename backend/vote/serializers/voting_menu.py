from rest_framework.serializers import ModelSerializer

from vote.models import VoteModel


class VotingMenuSerializer(ModelSerializer):
    class Meta:
        model = VoteModel
        fields = [
            "menu",
            "vote",
            "employee_phone_number",
        ]
