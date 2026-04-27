from django.conf import settings
from django.db import models


class Question(models.Model):
	"""
	Represents a question asked by a user.
	"""

	title = models.CharField(max_length=255)
	content = models.TextField()
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="questions"
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		"""Returns the title of the question."""
		return self.title


class Answer(models.Model):
	"""
	Represents an answer to a specific question.
	"""

	question = models.ForeignKey(
		Question, on_delete=models.CASCADE, related_name="answers"
	)
	content = models.TextField()
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="answers"
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		"""Returns a string representation of the answer."""
		return f"Answer to {self.question.title} by {self.author}"
