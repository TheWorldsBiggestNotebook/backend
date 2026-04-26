from django.contrib.auth import get_user_model
from rest_framework import serializers

# Later: uncomment this for password validation
# from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			"id",
			"username",
			"email",
			"first_name",
			"last_name",
			"role",
			"bio",
			"date_joined",
		)
		read_only_fields = ("role", "date_joined")

	def to_representation(self, instance):
		data = super().to_representation(instance)
		request = self.context.get("request")

		# Hide email unless the requester is viewing their own profile
		if not request or request.user != instance:
			data.pop("email", None)

		return data


class RegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ("username", "email", "password", "first_name", "last_name")

	# Later: uncomment this for password validation
	# def validate_password(self, value):
	# 	validate_password(value)
	# 	return value

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)
