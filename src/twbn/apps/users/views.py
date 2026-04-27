from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializers import RegistrationSerializer, UserSerializer

User = get_user_model()


class RegistrationView(generics.CreateAPIView):
	"""
	API view to register a new user.
	"""

	queryset = User.objects.all()
	serializer_class = RegistrationSerializer
	permission_classes = [permissions.AllowAny]


class UserMeView(generics.RetrieveUpdateAPIView):
	"""
	API view to retrieve or update the authenticated user's profile.
	"""

	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_object(self):
		"""
		Returns the currently authenticated user.

		Returns:
			User: The request.user instance.
		"""
		return self.request.user


class UserDetailView(generics.RetrieveAPIView):
	"""
	API view to retrieve public details of a specific user by username.

	Restricted to users with the 'MEMBER' role.
	"""

	queryset = User.objects.filter(role=User.Role.MEMBER)
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]
	lookup_field = "username"
