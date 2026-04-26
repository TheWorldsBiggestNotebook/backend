from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	class Role(models.TextChoices):
		ADMIN = "ADMIN", "Admin"
		MODERATOR = "MODERATOR", "Moderator"
		MEMBER = "MEMBER", "Member"

	role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
	bio = models.TextField(
		blank=True, help_text="Short bio or description of the user."
	)

	def save(self, *args, **kwargs):
		"""
		Automatically set the role based on is_superuser and is_staff flags.
		Moderators are created manually by admins (for now), so they won't be set here.
		"""
		if self.is_superuser:
			self.role = self.Role.ADMIN
		else:
			self.role = self.Role.MEMBER
		super().save(*args, **kwargs)

	def __str__(self):
		return self.username
