from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="bitrix24/index.html"), name="index"),
    path('users/', include("users.urls", namespace="users")),
]
