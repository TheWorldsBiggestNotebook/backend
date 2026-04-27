from rest_framework import permissions, viewsets

from .models import Answer, Question
from .permissions import IsOwnerOrReadOnly
from .serializers import AnswerSerializer, QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
	"""
	ViewSet for viewing and editing questions.
	"""

	queryset = Question.objects.all().order_by("-created_at")
	serializer_class = QuestionSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		"""
		Assigns the current user as the author of the question.

		Args:
			serializer: The serializer instance containing validated data.
		"""
		serializer.save(author=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
	"""
	ViewSet for viewing and editing answers.

	Allows users to create, retrieve, update, and delete answers.
	Write operations are restricted to the author or staff.
	"""

	queryset = Answer.objects.all().order_by("created_at")
	serializer_class = AnswerSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		"""
		Assigns the current user as the author of the answer.

		Args:
			serializer: The serializer instance containing validated data.
		"""
		serializer.save(author=self.request.user)
