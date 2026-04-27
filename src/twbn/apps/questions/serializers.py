from rest_framework import serializers

from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
	"""Serializer for the Answer model."""

	author = serializers.ReadOnlyField(source="author.username")

	class Meta:
		model = Answer
		fields = ["id", "question", "content", "author", "created_at", "updated_at"]
		read_only_fields = ["id", "created_at", "updated_at", "author", "question"]


class QuestionSerializer(serializers.ModelSerializer):
	"""
	Serializer for the Question model.

	Includes nested answers for the question.
	"""

	author = serializers.ReadOnlyField(source="author.username")
	answers = AnswerSerializer(many=True, read_only=True)

	class Meta:
		model = Question
		fields = [
			"id",
			"title",
			"content",
			"author",
			"answers",
			"created_at",
			"updated_at",
		]
		read_only_fields = ["id", "created_at", "updated_at", "author"]
