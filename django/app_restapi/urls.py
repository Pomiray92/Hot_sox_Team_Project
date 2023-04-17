from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken.views import obtain_auth_token

# Swagger configuration
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.urls import path
from . import views


app_name = "app_restapi"
urlpatterns = [
    # Swagger and ReDoc Documentation
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="app_restapi:schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="app_restapi:schema"),
        name="redoc",
    ),
    # authentication django token
    path("django-token/", obtain_auth_token, name="api_token_auth"),
    # authentication (JWT)
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Users
    path("users/", views.ApiGetUsers.as_view(), name="api_user_list"),
    path(
        "user/<int:pk>/",
        views.ApiGetPutDeleteUser.as_view(),
        name="api_user_detail",
    ),
    path(
        "user/",
        views.ApiCreateUser.as_view(),
        name="api_user_create",
    ),
    path("user/mails/", views.ApiGetMails.as_view(), name="api_mail_list"),
    path("user/mail/<int:pk>/", views.ApiGetMail.as_view(), name="api_mail_detail"),
    path("user/chats/", views.ApiGetChats.as_view(), name="api_chats_list"),
    path("user/chat/<int:pk>/", views.ApiGetChat.as_view(), name="api_chat_detail"),
    # Socks
    path("user/socks/", views.ApiGetSocks.as_view(), name="api_sock_list"),
    path("user/sock/<int:pk>/", views.ApiGetSock.as_view(), name="api_sock_detail"),
]
