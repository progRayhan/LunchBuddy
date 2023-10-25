from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers.create_employee import CreateEmployeeSerializer


class AdminCreateEmployeeView(APIView):
    """Admin can create employee for a particular company."""

    permission_classes = [IsAdminUser]

    def post(self, request):
        create_employee = CreateEmployeeSerializer(data=request.data)
        create_employee.is_valid(raise_exception=True)
        create_employee.save()
        return Response(
            {"detail": "Employee successfully created"}, status=status.HTTP_201_CREATED
        )
