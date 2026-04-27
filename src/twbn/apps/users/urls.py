from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
	path("register/", views.RegistrationView.as_view(), name="register"),
	# TODO: add docs for this endpoint and consider implementing a custom view to return user details along with the token
	path("login/", obtain_auth_token, name="api_token_auth"),
	path("users/me/", views.UserMeView.as_view(), name="user-me"),
	path("users/<str:username>/", views.UserDetailView.as_view(), name="user-detail"),
]
