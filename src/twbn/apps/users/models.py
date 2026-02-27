from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	class Role(models.TextChoices):
		ADMIN = "ADMIN", "Admin"
		MODERATOR = "MODERATOR", "Moderator"
		MEMBER = "MEMBER", "Member"
		GUEST = "GUEST", "Guest"

	role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
	bio = models.TextField(
		blank=True, help_text="Short bio or description of the user."
	)

	def __str__(self):
		return self.username
