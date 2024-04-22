from django.urls import path
from .views import CreateUser, UserDetail, UserUpdate
from django.contrib.auth.views import LogoutView, LoginView


app_name = "users"

urlpatterns = [
    path("signup/", CreateUser.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("detail/<int:pk>/", UserDetail.as_view(), name="detail"),
    path("update/<int:pk>/", UserUpdate.as_view(), name="update"),
]
