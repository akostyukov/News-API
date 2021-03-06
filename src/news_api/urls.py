"""news_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(openapi.Info(title="News API", default_version="v1"))

v1_urls = [
    path("", include("news.v1.urls")),
    path("docs/", schema_view.with_ui()),
    path("auth/", include("accounts.v1.urls")),
]

api_version = [
    path("v1/", include(v1_urls)),
]

urlpatterns = [
    path("api/", include(api_version)),
    path("admin/", admin.site.urls),
    path("silk/", include("silk.urls")),
]
