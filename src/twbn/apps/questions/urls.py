from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AnswerViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)
router.register(r"answers", AnswerViewSet)

urlpatterns = [
	path("", include(router.urls)),
]
