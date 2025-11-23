from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    ShowSession,
    Reservation,
    Ticket,
    PlanetariumDome
)
from planetarium.pagination import (
    ShowSessionPagination,
    ReservationPagination
)
from planetarium.permissions import IsAdminOrIfAuthenticatedReadOnly
from planetarium.serializers import (
    AstronomyShowSerializer,
    ShowThemeSerializer,
    ShowSessionSerializer,
    ReservationSerializer,
    TicketSerializer,
    PlanetariumDomeSerializer
)


class AstronomyShowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
    pagination_class = ReservationPagination
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)



class ShowThemeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
    pagination_class = ReservationPagination
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)



class ShowSessionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = ShowSession.objects.select_related(
        "astronomy_show", "planetarium_dome"
    ).prefetch_related("ticket_set")
    serializer_class = ShowSessionSerializer
    pagination_class = ShowSessionPagination
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)



class PlanetariumDomeViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
    pagination_class = ReservationPagination
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)



class ReservationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    pagination_class = ReservationPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    pagination_class = ReservationPagination
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

