from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Allow read access to anyone. Write access only to the object's owner,
	or to admins/moderators.
	"""

	def has_permission(self, request, view):
		"""
		Check global permissions for the request.

		Args:
			request: The incoming request.
			view: The view being accessed.

		Returns:
			bool: True if access is granted, False otherwise.
		"""
		if request.method in permissions.SAFE_METHODS:
			return True

		return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		"""
		Check object-level permissions.

		Allows read-only access to anyone, and write access only to
		the author or administrative roles.

		Args:
			request: The incoming request.
			view: The view being accessed.
			obj: The object being checked.

		Returns:
			bool: True if access is granted, False otherwise.
		"""
		if request.method in permissions.SAFE_METHODS:
			return True

		# Admins and moderators can edit anything
		if request.user.role in ("ADMIN", "MODERATOR"):
			return True

		# Everyone else can only touch their own objects
		return obj.author == request.user
