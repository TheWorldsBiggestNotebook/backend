from rest_framework import serializers

from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source="author.username")

	class Meta:
		model = Answer
		fields = ["id", "question", "content", "author", "created_at", "updated_at"]
		read_only_fields = ["id", "created_at", "updated_at", "author", "question"]


class QuestionSerializer(serializers.ModelSerializer):
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
