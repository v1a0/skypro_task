from django.urls import path, include
from django.contrib.auth import views
from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from resume.views import ResumeView


schema_view = get_schema_view(
    openapi.Info(title="SkyPro-task API", default_version='v1'),
    public=True, permission_classes=[permissions.AllowAny],
)


app_name = 'rest_framework'


urlpatterns = [
    path('resume/', ResumeView.as_view(), name='resume'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
