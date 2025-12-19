from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include
from demoapp.views import UserSerializerView, simple_page, student_api,ProfileAPI
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .api.v1.v1 import UserProfileV1
from .api.v2.v2 import UserProfileV2
router = DefaultRouter()
router.register(r'users', UserSerializerView)

urlpatterns = [
    path('', views.hello, name='hello'),
    path('hello_post', views.hello_post_api, name='hello_post_api'),
    path('echo', views.echo, name='echo'),
    path('update_echo', views.update_echo, name='update_echo'),
    path('delete_echo', views.delete_echo, name='delete_echo'),

    path('dispatch_echo', views.SimplePostView.as_view(), name='dispatch_echo'),
    path('drf', views.DRFView.as_view(), name='drf'),
    path("", include(router.urls)),
    path('simple-products/', simple_page),
    path('student/', student_api),
    path('login/', views.login_page),
    path('home/', views.home),
    path('profile/',views.ProfileAPI.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path("jwt/login/", TokenObtainPairView.as_view()),
    path("jwt/refresh/", TokenRefreshView.as_view()),
    # adding version api

    path('v1/profile', UserProfileV1.as_view()),
    path('v2/profile', UserProfileV2.as_view()),
]