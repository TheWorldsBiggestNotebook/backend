from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializers import RegistrationSerializer, UserSerializer

User = get_user_model()


class RegistrationView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegistrationSerializer
	permission_classes = [permissions.AllowAny]


class UserMeView(generics.RetrieveUpdateAPIView):
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_object(self):
		return self.request.user


class UserDetailView(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]
	lookup_field = "username"
