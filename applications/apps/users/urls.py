from django.urls import path
from apps.users.views import RegistrationApiView ,UserEditApiView ,LoginApiView , UserLogout





urlpatterns = [
    path('registration/', RegistrationApiView.as_view()),
    path('edit_user/<int:pk>/', UserEditApiView.as_view()),
    path('login/',LoginApiView.as_view()),
    path('logout/',UserLogout.as_view()),


]