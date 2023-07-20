from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from borrowing.models import Borrowing
from borrowing.serializers import (
    BorrowingReadSerializer,
    BorrowingCreateSerializer,
    BorrowingReturnSerializer,
)


class BorrowingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Borrowing.objects.select_related("book", "user")
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        permission_classes = super().get_permissions()

        if self.action == "return_borrowing":
            permission_classes = [IsAdminUser]

        return permission_classes

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_staff:
            return queryset.filter(user=self.request.user)

        user_id = self.request.query_params.get("user_id")
        is_active = self.request.query_params.get("is_active")

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        if is_active:
            queryset = queryset.filter(actual_return_date=None)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BorrowingReadSerializer
        elif self.action == "create":
            return BorrowingCreateSerializer
        elif self.action == "return_borrowing":
            return BorrowingReturnSerializer
        return BorrowingReadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
