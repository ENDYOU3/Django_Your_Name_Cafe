"""YourName URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("app_general.urls", "app_general"), namespace="app_general")),
    path("products/", include(("app_product.urls", "app_product"), namespace="app_product")),
    path("login/", auth_views.LoginView.as_view(template_name="app_general/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="app_general/logout.html"), name="logout")
]

# Path upload photo
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
