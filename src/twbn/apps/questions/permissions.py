from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Allow read access to anyone. Write access only to the object's owner,
	or to admins/moderators. I believe this to be very volatile and subject
	to change as I add more features, but it should be good enough for now.
	"""

	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True

		return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		# Admins and moderators can edit anything
		if request.user.role in ("ADMIN", "MODERATOR"):
			return True

		# Everyone else can only touch their own objects
		return obj.author == request.user
