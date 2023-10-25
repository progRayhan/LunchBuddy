from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers.create_employee import CreateEmployeeSerializer


class AdminCreateEmployeeView(APIView):
    """Admin can create employee for a particular company."""

    permission_classes = [IsAdminUser]

    def post(self, request):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        user_type = request.data.get("user_type")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        employee_id = request.data.get("employee_id")
        company = request.data.get("company")
        company_phone_number = request.data.get("company_phone_number")
        position = request.data.get("position")
        gender = request.data.get("gender")
        password = request.data.get("password")

        password_hash = make_password(password)

        employee_data = {
            "phone_number": phone_number,
            "email": email,
            "user_type": user_type,
            "first_name": first_name,
            "last_name": last_name,
            "employee_id": employee_id,
            "company": company,
            "company_phone_number": company_phone_number,
            "position": position,
            "gender": gender,
            "password": password_hash,
        }

        create_employee = CreateEmployeeSerializer(data=employee_data)
        create_employee.is_valid(raise_exception=True)
        create_employee.save()
        return Response(
            {"detail": "Employee successfully created"}, status=status.HTTP_201_CREATED
        )
