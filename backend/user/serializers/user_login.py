from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user_info):
        token = super().get_token(user_info)

        token["id"] = user_info.id
        token["phone_number"] = user_info.phone_number
        token["user_type"] = user_info.user_type
        token["employee_id"] = user_info.employee_id
        token["company_phone_number"] = user_info.company_phone_number
        token["is_active"] = user_info.is_active
        token["is_staff"] = user_info.is_staff

        return token
