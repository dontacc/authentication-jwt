from django.urls import path
from core.authentication.views import refresh_jwt_token, verify_jwt_token
from .views import LoginAPI

urlpatterns = [
    # path("access-token/", obtain_jwt_token),
    path("refresh-token/", refresh_jwt_token),
    path("verify-token/", verify_jwt_token),
    path("login/", LoginAPI.as_view(), name="login")
]
