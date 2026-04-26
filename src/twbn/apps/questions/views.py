from rest_framework import permissions, viewsets

from .models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all().order_by("-created_at")
	serializer_class = QuestionSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
	queryset = Answer.objects.all().order_by("created_at")
	serializer_class = AnswerSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)
