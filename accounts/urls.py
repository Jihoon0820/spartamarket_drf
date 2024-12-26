from django.urls import path
from .views import SignUpView, CustomAuthToken, UserProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('<str:username>/', UserProfileView.as_view(), name='profile'),
]