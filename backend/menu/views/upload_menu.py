from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.serializers.upload_menu import UploadMenuSerializer


class UploadMenuView(APIView):
    """Admin can upload menu for restaurants."""

    permission_classes = [IsAdminUser]

    def post(self, request):
        upload_menu = UploadMenuSerializer(data=request.data)
        upload_menu.is_valid(raise_exception=True)
        upload_menu.save()
        return Response(
            {"detail": "Menu successfully uploaded"}, status=status.HTTP_201_CREATED
        )
