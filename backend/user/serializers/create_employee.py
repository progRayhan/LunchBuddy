from rest_framework.serializers import ModelSerializer

from user.models import UserAccount


class CreateEmployeeSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            "phone_number",
            "email",
            "user_type",
            "first_name",
            "last_name",
            "employee_id",
            "company",
            "company_phone_number",
            "position",
            "gender",
            "password",
        ]
