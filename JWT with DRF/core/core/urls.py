
from django.contrib import admin
from django.urls import path, include

##################################imported for JWT#####################################33333333333333333333333333333333333333333333
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),


    path("", include("home.urls")),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #to get JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # to refresh token
]
