from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-create'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
